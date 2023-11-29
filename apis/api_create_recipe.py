from bottle import post, response, request, time, template
import x
import uuid
import time
import os

@post("/opret-opskrift")
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

        # User data
        # Hent valideret data fra form
        recipe_id = str(uuid.uuid4()).replace("-","")

        recipe_user_fk = user_cookie['user_id']
        recipe_name = request.forms.get("recipe_name")
        recipe_description = request.forms.get("recipe_description")
        recipe_category = request.forms.get("category")
        recipe_cooking_est = request.forms.get("est_time")
        recipe_difficulty = request.forms.get("dificulty")


        # Upload af billeder til profil
        rootdir = "C:/Users/maalm/OneDrive/Dokumenter/kea/2_semester/recipe_catalogue/"

        for key, file_item in request.files.items():
            # Print the key (file input field name)
            print(f"Key: {key}")

            # Print some information about the file
            print(f"Filename: {file_item.filename}")
            print(f"Content Type: {file_item.content_type}")
            print(f"File Size: {len(file_item.file.read())} bytes")

        #Upload banner
        uploaded_thumbnail = request.files.get("image_thumbnail_input") #files i formen
        print("First check")
        print(uploaded_thumbnail)
        if uploaded_thumbnail != None :
            name, ext = os.path.splitext(uploaded_thumbnail.filename)
            if ext == "" : 
                final_thumbnail = "default_recipe.jpg"
            else:
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    raise Exception("Picture not allowed")
                final_thumbnail = str(uuid.uuid4().hex)
                final_thumbnail = final_thumbnail + ext
                uploaded_thumbnail.save(f"{rootdir}/images/recipe_thumbnails/{final_thumbnail}")
        else :
            final_thumbnail = "default_recipe.jpg"


        # Indsæt til db
        recipe = {
            "recipe_id" : recipe_id,
            "recipe_user_fk" : recipe_user_fk,
            "recipe_name" : recipe_name,
            "recipe_description" : recipe_description,
            "recipe_category" : recipe_category,
            "recipe_cooking_est" : recipe_cooking_est,
            "recipe_difficulty" : recipe_difficulty,
            "recipe_total_likes" : 0,
            "recipe_created_at" : int(time.time()),
            "recipe_thumbnail" : final_thumbnail
        }

        values = ""
        for key in recipe:
            values += f':{key},'
        values = values.rstrip(",")

        total_rows_inserted = db.execute(f"INSERT INTO recipes VALUES({values})", recipe).rowcount
        db.commit()

        if total_rows_inserted != 1 :
            raise Exception("Prøv venligst igen")

        return {"info": "ok"}


    except Exception as ex:
        print(ex)
        try: # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}

        except: # Something unknown went wrong
            # unknown scenario
            response.status = 500
            return {"info":str(ex)}
    
    finally:
        if "db" in locals() : db.close()