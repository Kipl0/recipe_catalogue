from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/opret-bruger")
def _():
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        # Brugeren skal ikke være på login siden, hvis brugeren
        # er logget ind allerede. Brugeren burde ikke kunne få adgang
        # via knapper, men har adgang via manuelt indskrevet end-point
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
            if user_cookie['user_role'] == 'admin':
                admin = True
        else:
            admin = False
            print("Ingen bruger er logget ind.")


        if user_cookie:
            response.status = 303  # fordi 303 bruges til redirecting
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
            user_cookie=user_cookie,
            admin=admin,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(ex)
        return {"error :", str(ex)}

    finally:
        if "db" in locals():
            db.close()
