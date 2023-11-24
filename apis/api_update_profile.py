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
        user_cookie = x.validate_user_jwt(user_cookie)

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
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    return { "info" : "Billedetype er ikke tilladt" }
                final_profile_pic = str(uuid.uuid4().hex)
                final_profile_pic = final_profile_pic + ext
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
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    return { "info" : "Billedetype er ikke tilladt" }
                final_banner = str(uuid.uuid4().hex)
                final_banner = final_banner + ext
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






















