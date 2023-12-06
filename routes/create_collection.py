from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/opret-samling")
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

        if user_cookie is None:
            response.status = 303  # fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return

        user_recipes = db.execute("SELECT * FROM recipes WHERE recipe_user_fk = ?", (user_cookie['user_id'],)).fetchall()  # noqa
        if user_recipes is []:
            user_recipes = "Du har ikke oprettet nogle opskrifter endnu"


        return template(
            "create_collection",
            title="Opret samling",
            user_cookie=user_cookie,
            user_recipes=user_recipes,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
