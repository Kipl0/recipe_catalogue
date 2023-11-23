from bottle import get, request, response, template
import x
from security.csp import get_csp_directives


@get("/login")
def _():
    try:
        # Sæt CSP 
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)
        
        db = x.db()

        # Brugeren skal ikke være på login siden, hvis brugeren er logget ind allerede
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie:
            response.status = 303 #fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return

        return template("login", title="Login", user_cookie=user_cookie)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()