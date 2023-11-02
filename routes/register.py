from bottle import get, request, template
import x

@get("/opret-bruger")
def _():
    try:
        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        return template(
            "register", 
            title="Opret bruger", 
            FIRST_NAME_MIN=x.FIRST_NAME_MIN, 
            FIRST_NAME_MAX=x.FIRST_NAME_MAX, 
            LAST_NAME_MIN=x.LAST_NAME_MIN, 
            LAST_NAME_MAX=x.LAST_NAME_MAX, 
            USERNAME_MIN=x.USERNAME_MIN, 
            USERNAME_MAX=x.USERNAME_MAX, 
            EMAIL_MIN=x.EMAIL_MIN, 
            EMAIL_MAX=x.EMAIL_MAX, 
            PASSWORD_MIN=x.PASSWORD_MIN, 
            PASSWORD_MAX=x.PASSWORD_MAX,
            user_cookie=user_cookie
        )
    
    except Exception as ex:
        print(ex)
        return{"error :", str(ex)}
    
    finally:
        if "db" in locals() : db.close()