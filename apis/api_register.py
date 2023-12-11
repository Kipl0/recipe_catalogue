from bottle import post, response, request
import x
import uuid
import time
import bcrypt
import os


@post("/opret-bruger")
def _():
    try:
        db = x.db()

        # User data
        user_id = str(uuid.uuid4()).replace("-", "")
        # Hent valideret data fra form
        user_first_name = x.validate_first_name()
        user_last_name = x.validate_last_name()
        user_username = x.validate_username()
        user_email = x.validate_email()
        user_password = x.validate_password()
        x.validate_confirm_password()

        user_csrf_token = request.forms.get('csrf_token')
        if user_csrf_token != request.csrf_token:
            return {"info": "Ugyldigt CSRF-token! Handling afvist."}

        # bcrypt bruger en hash-funktion sammen med salt, for at
        # generere en hash-værdi, som gemmes i db bruges til at gemme
        # adgangskoder sikkert, da du kun sammenligner hash-værdier
        # for at bekræfte, om adgangskoden er korrekt.
        user_password_input = user_password.encode('utf') #Konverter password til bytes  # noqa
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_password_input, salt)

        # Upload af billeder til profil
        rootdir = "C:/Users/maalm/OneDrive/Dokumenter/kea/2_semester/recipe_catalogue/"  # noqa

        # Profil billede
        uploaded_profil_pic = request.files.get("uploaded_profil_pic_input")  # noqa
        if uploaded_profil_pic is not None:
            name, ext = os.path.splitext(uploaded_profil_pic.filename)
            if ext == "":
                # Fordi formen bruger enctype, er uploaded_profil_pic ikke "none", men ext er (eller en " " )  # noqa
                final_profile_pic = "unknown_user.jpg"
            else:
                if ext not in x.picture_whitelist:
                    response.status = 400
                    return {"info": "Billedetype er ikke tilladt"}

                # Tjek filstørrelsen før upload gemmes
                if len(uploaded_profil_pic.file.read()) > x.max_profilepic_size:  # noqa
                    response.status = 413  # Statuskode 413 betyder "Request Entity Too Large"  # noqa
                    return {"info": "Billede er for stort"}

                uploaded_profil_pic.file.seek(0)
                final_profile_pic = str(uuid.uuid4().hex) + ext
                uploaded_profil_pic.save(f"{rootdir}images/profile_images/{final_profile_pic}")  # noqa
        else:
            final_profile_pic = "unknown_user.jpg"

        # Upload banner
        uploaded_banner = request.files.get("uploaded_banner_input")
        if uploaded_banner is not None:
            name, ext = os.path.splitext(uploaded_banner.filename)
            if ext == "":
                final_banner = "default_banner.png"
            else:
                if ext not in x.picture_whitelist:
                    response.status = 400
                    return {"info": "Billedetype er ikke tilladt"}

                # Tjek filstørrelsen før upload gemmes
                if len(uploaded_banner.file.read()) > x.max_banner_size:
                    response.status = 413  # Statuskode 413 betyder "Request Entity Too Large"  # noqa
                    return {"info": "Billede er for stort"}

                uploaded_banner.file.seek(0)
                final_banner = str(uuid.uuid4().hex) + ext
                uploaded_banner.save(f"{rootdir}images/profile_banners/{final_banner}")  # noqa

        else:
            final_banner = "default_banner.png"

        # Indsæt til db
        user = {
            "user_id": user_id,
            "user_email": user_email,
            "user_username": user_username,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_birthday": "TBD",
            "user_password": hashed_password,
            "user_created_at": int(time.time()),
            "user_active": 1,
            "user_profilepic": final_profile_pic,
            "user_banner": final_banner,
            "user_role": "member",
            "user_total_followers": 0,
            "user_total_following": 0,
            "user_total_recipes": 0,
            "user_total_collections": 0
        }

        values = ""
        for key in user:
            values += f':{key},'
        values = values.rstrip(",")

        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount  # noqa
        db.commit()

        if total_rows_inserted != 1:
            return {"info": "Prøv venligst igen"}

        # Redirect sker via js
        return {"info": "ok"}

    except Exception as ex:
        try:  # Controlled exception, usually from the x file
            print(ex)
            return {"info": str(ex)}

        except Exception as ex:  # Something unknown went wrong
            if "user_email" in str(ex):
                response.status = 400
                return {"info": "Email er optaget"}

            if "user_username" in str(ex):
                response.status = 400
                return {"info": "Brugernavn er optaget"}

            # unknown scenario
            response.status = 500
            return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
