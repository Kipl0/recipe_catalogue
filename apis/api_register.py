from bottle import post, response, request, time, template
import x
import uuid
import time
# import bcrypt
import os

@post("/opret-bruger")
def _():
    try:
        db = x.db()

        # Hent valideret data fra form
        user_first_name = x.validate_first_name()
        user_last_name = x.validate_last_name()
        user_username = x.validate_username()
        user_email = x.validate_email()
        user_password = x.validate_password()
        x.validate_confirm_password()

        user_id = str(uuid.uuid4()).replace("-","")
        user = {
            "user_id" : user_id,
            "user_email" : user_email,
            "user_username" : user_username,
            "user_first_name" : user_first_name,
            "user_last_name" : user_last_name,
            "user_birthday" : "TBD",
            "user_password" : user_password,
            "user_created_at" : int(time.time()),
            "user_active" : 1,
            "user_profilepic" : "TBD",
            "user_banner" : "TBD",
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