from bottle import get, request, response, template
import x

@get("/opret-bruger")
def _():
    try:
        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        # Brugeren skal ikke være på login siden, hvis brugeren er logget ind allerede
        # Brugeren burde ikke kunne få adgang via knapper, men har adgang via manuelt indskrevet end-point
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie:
            response.status = 303 #fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return

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