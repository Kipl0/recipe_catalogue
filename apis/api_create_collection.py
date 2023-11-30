from bottle import post, response, request
import x
import uuid
import time
import os


@post("/opret-samling")
def _():
    try:
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        user_csrf_token = request.forms.get('csrf_token')
        if user_csrf_token != request.csrf_token:
            return {"info": "Ugyldigt CSRF-token! Handling afvist."}

        # skal bruges til redirect til side med username
        username = user_cookie['user_username']

        # Hent valideret data fra form
        collection_id = str(uuid.uuid4()).replace("-", "")
        collection_user_fk = user_cookie['user_id']
        collection_name = request.forms.get("collection_name")

        # Upload af billeder til profil
        rootdir = "C:/Users/maalm/OneDrive/Dokumenter/kea/2_semester/recipe_catalogue/"  # noqa

        # Upload thumbnail
        uploaded_thumbnail = request.files.get("collection_thumbnail_input")
        if uploaded_thumbnail is not None:
            name, ext = os.path.splitext(uploaded_thumbnail.filename)
            if ext is "":
                final_thumbnail = "default_collection.jpg"
            else:
                if ext not in (".jpg", ".jpeg", ".png"):
                    response.status = 400
                    raise Exception("Picture not allowed")
                final_thumbnail = str(uuid.uuid4().hex)
                final_thumbnail = final_thumbnail + ext
                uploaded_thumbnail.save(f"{rootdir}/images/collection_thumbnails/{final_thumbnail}")  # noqa
        else:
            final_thumbnail = "default_collection.jpg"

        # Indsæt til db
        collection = {
            "collection_id": collection_id,
            "collection_user_fk": collection_user_fk,
            "collection_name": collection_name,
            "collection_created_at": int(time.time()),
            "collection_thumbnail": final_thumbnail
        }

        values = ""
        for key in collection:
            values += f':{key},'
        values = values.rstrip(",")

        total_rows_inserted = db.execute(f"INSERT INTO collections VALUES({values})", collection).rowcount  # noqa
        db.commit()

        if total_rows_inserted != 1:  # noqa
            raise Exception("Prøv venligst igen")

        return {"info": "ok", "username": username}

    except Exception as ex:
        print(ex)
        try:  # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info": ex.args[1]}

        except Exception as ex:  # Something unknown went wrong
            # unknown scenario
            response.status = 500
            return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
