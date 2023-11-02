from bottle import post, response, request, time, template
import x
import bcrypt

@post("/login")
def _():
    try:
        db = x.db()

        username_input = request.forms.get("username-input")
        password_input = request.forms.get("password-input")

        # Hvis password er blevet udfyld -> encode
        password_input = password_input.encode("utf-8")

        check_user = db.execute("SELECT * FROM users WHERE user_username = ? LIMIT 1", (username_input,)).fetchone()

        # Hvis brugeren ikke eksisterer i db
        if not check_user:
            raise Exception(400, "Ugyldigt login")

        # Matcher den hashede password input med password i db for user
        if not bcrypt.checkpw(password_input, check_user["user_password"]):
            raise Exception(400, "Ugyldigt login")


        # ----------------------------
        #      opret usercookie
        # ----------------------------
        cookie_expiration = int(time.time()) + 7200 #session varer 2 timer
        response.set_cookie("user_cookie", check_user, secret=x.COOKIE_SECRET, httponly=True, expires=cookie_expiration)

        
        return {"info": "ok"}
    

    except Exception as ex:
        response.status = 400
        print(ex)
        return {"info": str(ex)}


    finally:
        if "db" in locals(): db.close()
