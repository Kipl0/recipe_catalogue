from bottle import get, request, response, template
import x

@get("/nulstil-password")
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

        return template("reset_password", title="Reset password", user_cookie=user_cookie)
    
    except Exception as ex:
        print(ex)
        return{"error :", str(ex)}
    
    finally:
        if "db" in locals() : db.close()