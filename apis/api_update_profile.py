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


        user_csrf_token = request.forms.get('csrf_token')
        if user_csrf_token != request.csrf_token:
            return {"info": "Ugyldigt CSRF-token! Handling afvist."}
        

        # user_first_name = request.forms.get("user_first_name")
        user_first_name = x.validate_first_name()
        # user_last_name = request.forms.get("user_last_name")
        user_last_name = x.validate_last_name()


        # Upload af billeder til profil
        rootdir = "C:/Users/maalm/OneDrive/Dokumenter/kea/2_semester/recipe_catalogue/"
        # Profil billede
        uploaded_profil_pic = request.files.get("uploaded_profil_pic_input") 
        if uploaded_profil_pic != None :
            name, ext = os.path.splitext(uploaded_profil_pic.filename)
            if ext == "" :
                # Fordi formen bruger enctype, er uploaded_profil_pic ikke "none", men ext er (eller en " " )
                final_profile_pic = user_cookie["user_profilepic"]
            else:
                if ext not in x.picture_whitelist:
                    response.status = 400
                    return { "info" : "Billedetype er ikke tilladt" }
                
                # Tjek filstørrelsen før upload gemmes
                if len(uploaded_profil_pic.file.read()) > x.max_profilepic_size:
                    response.status = 413  # Statuskode 413 betyder "Request Entity Too Large"
                    return { "info" : "Billede er for stort" }                

                final_profile_pic = str(uuid.uuid4().hex) + ext
                uploaded_profil_pic.save(f"{rootdir}images/profile_images/{final_profile_pic}")
        else :
            final_profile_pic = user_cookie["user_profilepic"]


        #Upload banner
        uploaded_banner = request.files.get("uploaded_banner_input") #files i formen
        if uploaded_banner != None :
            name, ext = os.path.splitext(uploaded_banner.filename)
            if ext == "" : 
                final_banner = user_cookie["user_banner"]
            else:
                if ext not in x.picture_whitelist:
                    response.status = 400
                    return { "info" : "Billedetype er ikke tilladt" }
                
                # Tjek filstørrelsen før upload gemmes
                if len(uploaded_banner.file.read()) > x.max_banner_size:
                    response.status = 413  # Statuskode 413 betyder "Request Entity Too Large"
                    return { "info" : "Billede er for stort" }
                
                final_banner = str(uuid.uuid4().hex) + ext
                uploaded_banner.save(f"{rootdir}images/profile_banners/{final_banner}")

        else :
            final_banner = user_cookie["user_banner"]


        print("#"*30)









        # Indsæt til db

        db.execute(
            "UPDATE users SET user_first_name=?, user_last_name=?, user_profilepic=?, user_banner=? WHERE user_id = ?",
            (
                user_first_name, 
                user_last_name, 
                final_profile_pic, 
                final_banner, 
                user_cookie["user_id"]
            ),           
        )
        db.commit()
        print("#"*30)
        
        # Redirect sker via js
        username = user_cookie['user_username']
        return {"info": "ok", "username":username}


    except Exception as ex:
        try: # Controlled exception, usually comming from the x file
            # response.status = 400
            print("error: ", ex)
            return {"info": str(ex)}

        except: # Something unknown went wrong
            # unknown scenario
            response.status = 500
            return {"info":str(ex)}
    
    finally:
        if "db" in locals() : db.close()






















