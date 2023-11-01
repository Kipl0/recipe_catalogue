from bottle import post, response, request, time, template
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
        # Hent valideret data fra form
        user_first_name = x.validate_first_name()
        user_last_name = x.validate_last_name()
        user_username = x.validate_username()
        user_email = x.validate_email()
        user_password = x.validate_password()
        x.validate_confirm_password()

        user_id = str(uuid.uuid4()).replace("-","")


        # bcrypt bruger en hash-funktion sammen med salt, for at generere en hash-værdi, som gemmes i db
        #bruges til at gemme adgangskoder sikkert, da du kun sammenligner hash-værdier for at bekræfte, om adgangskoden er korrekt.
        user_password_input = user_password.encode('utf') #Konverter password til bytes
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_password_input, salt)


        # Upload af billeder til profil
        rootdir = "C:/Users/maalm/OneDrive/Dokumenter/kea/2_semester/recipe_catalogue/"

        # Profil billede
        uploaded_profil_pic = request.files.get("uploaded_profil_pic") 
        if uploaded_profil_pic != None :
            name, ext = os.path.splitext(uploaded_profil_pic.filename)
            if ext == "" : 
                # Fordi formen bruger enctype, er uploaded_profil_pic ikke "none", men ext er (eller en " " )
                final_profile_pic = "unknown_user.jpg"
            else:
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    print(ext)
                    return "Venligst vælg et billede med en godkendt filtype"
                final_profile_pic = str(uuid.uuid4().hex)
                final_profile_pic = final_profile_pic + ext
                uploaded_profil_pic.save(f"{rootdir}images/profile_images/{final_profile_pic}")
                # return "Picture uploaded"
        else :
            final_profile_pic = "unknown_user.jpg"

        #Upload banner
        uploaded_banner = request.files.get("uploaded_banner") #files i formen
        if uploaded_banner != None :
            name, ext = os.path.splitext(uploaded_banner.filename)
            if ext == "" : 
                final_banner = "default_banner.png"
            else:
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    raise Exception("Picture not allowed")
                final_banner = str(uuid.uuid4().hex)
                final_banner = final_banner + ext
                uploaded_banner.save(f"{rootdir}banner/{final_banner}")
                # return "Picture uploaded"
        else :
            final_banner = "default_banner.png"


        # Indsæt til db
        user = {
            "user_id" : user_id,
            "user_email" : user_email,
            "user_username" : user_username,
            "user_first_name" : user_first_name,
            "user_last_name" : user_last_name,
            "user_birthday" : "TBD",
            "user_password" : hashed_password,
            "user_created_at" : int(time.time()),
            "user_active" : 1,
            "user_profilepic" : final_profile_pic,
            "user_banner" : final_banner,
            "user_total_followers" : 0,
            "user_total_following" : 0,
            "user_total_recipes" : 0,
            "user_total_collections" : 0
        }

        values = ""
        for key in user:
            values += f':{key},'
        values = values.rstrip(",")

        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
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
            if "user_email" in str(ex): 
                response.status = 400 
                return {"info":"user_email already exists"}

            if "user_username" in str(ex): 
                response.status = 400 
                return {"info":"user_name already exists"}

            # unknown scenario
            response.status = 500
            return {"info":str(ex)}
    
    finally:
        if "db" in locals() : db.close()