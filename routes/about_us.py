from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/om-os")
def _():
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        if user_cookie['user_role'] == 'admin':
            admin = True
        else:
            admin = False

        return template(
            "about_us",
            title="Om os",
            admin=admin,
            user_cookie=user_cookie
        )

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
