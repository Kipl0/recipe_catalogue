from bottle import get, request, response, template
import x

@get("/login")
def _():
    try:
        db = x.db()

        # Brugeren skal ikke være på login siden, hvis brugeren er logget ind allerede
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie:
            response.status = 303 #fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return

        return template("login", title="Login")

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()