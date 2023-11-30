from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/adminstration")
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

        # Er der en cookie og i så fald er det admin
        if user_cookie:
            if user_cookie['user_role'] != "admin":
                response.status = 303  # fordi 303 bruges til redirecting
                response.set_header("Location", "/")
                return
        else:
            # der var ingen cookie
            response.status = 303  # fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return
        
        if user_cookie['user_role'] == 'admin':
            admin = True
        else:
            admin = False

        all_users = db.execute("SELECT * FROM users WHERE user_role != ?", ("admin",)).fetchall()  # noqa

        return template(
            "admin",
            title="Admin side",
            user_cookie=user_cookie,
            admin=admin,
            all_users=all_users,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
