from bottle import put, response, request
import x
import uuid
import os


@put("/opdater-profil")
def _():
    try:
        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        user_csrf_token = request.forms.get("csrf_token")
        if user_csrf_token != request.csrf_token:
            return {"info": "Ugyldigt CSRF-token! Handling afvist."}

        user_first_name = x.validate_first_name()
        user_last_name = x.validate_last_name()

        # Upload af billeder til profil
        try:
            # If this production is found, the next line should run
            import production  # noqa

            rootdir = "/home/MajaILarsen/recipe_catalogue/"
        except Exception:
            rootdir = "C:/Users/maalm/OneDrive/Dokumenter/kea/2_semester/recipe_catalogue/"  # noqa

        # Profil billede
        uploaded_profil_pic = request.files.get("uploaded_profil_pic_input")
        if uploaded_profil_pic is not None:
            name, ext = os.path.splitext(uploaded_profil_pic.filename)
            if ext == "":
                # Fordi formen bruger enctype, er uploaded_profil_pic
                # ikke "none", men ext er (eller en " " )
                final_profile_pic = user_cookie["user_profilepic"]
            else:
                if ext not in x.picture_whitelist:
                    response.status = 400
                    return {"info": "Billedetype er ikke tilladt"}

                # Tjek filstørrelsen før upload gemmes
                if len(uploaded_profil_pic.file.read()) > x.max_profilepic_size:  # noqa
                    response.status = (
                        413  # Statuskode 413 betyder "Request Entity Too Large"  # noqa
                    )
                    return {"info": "Billede er for stort"}

                uploaded_profil_pic.file.seek(0)
                final_profile_pic = str(uuid.uuid4().hex) + ext
                uploaded_profil_pic.save(
                    f"{rootdir}images/profile_images/{final_profile_pic}"
                )  # noqa
        else:
            final_profile_pic = user_cookie["user_profilepic"]

        # Upload banner
        uploaded_banner = request.files.get("uploaded_banner_input")
        if uploaded_banner is not None:
            name, ext = os.path.splitext(uploaded_banner.filename)
            if ext == "":
                final_banner = user_cookie["user_banner"]
            else:
                if ext not in x.picture_whitelist:
                    response.status = 400
                    return {"info": "Billedetype er ikke tilladt"}

                # Tjek filstørrelsen før upload gemmes
                if len(uploaded_banner.file.read()) > x.max_banner_size:
                    response.status = (
                        413  # Statuskode 413 betyder "Request Entity Too Large"  # noqa
                    )
                    return {"info": "Billede er for stort"}

                uploaded_banner.file.seek(0)
                final_banner = str(uuid.uuid4().hex) + ext
                uploaded_banner.save(
                    f"{rootdir}images/profile_banners/{final_banner}"
                )  # noqa

        else:
            final_banner = user_cookie["user_banner"]

        # Indsæt til db
        db.execute(
            "UPDATE users SET user_first_name=?, user_last_name=?, user_profilepic=?, user_banner=? WHERE user_id = ?",  # noqa
            (
                user_first_name,
                user_last_name,
                final_profile_pic,
                final_banner,
                user_cookie["user_id"],
            ),
        )
        db.commit()

        # Redirect sker via js
        username = user_cookie["user_username"]
        return {"info": "ok", "username": username}

    except Exception as ex:
        try:  # Controlled exception, usually comming from the x file
            # response.status = 400
            print("error: ", ex)
            return {"info": str(ex)}

        except Exception as ex:  # Something unknown went wrong
            # unknown scenario
            response.status = 500
            return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
