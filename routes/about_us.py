from bottle import get, request, response, template
import x
from security.csp import get_csp_directives


@get("/om-os")
def _():
    try:
        # Sæt CSP 
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)
        
        db = x.db()
        
        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_user_jwt(user_cookie)

        return template("about_us", title="Om os", user_cookie=user_cookie)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()