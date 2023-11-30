from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/<user_username>/opskrifter")
def _(user_username):
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        db = x.db()

        user = db.execute("SELECT * FROM users WHERE user_username = ? COLLATE NOCASE", (user_username, )).fetchone()  # noqa

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        all_recipes_query = """
            SELECT recipes.*,
                CASE WHEN recipes_liked_by_users.recipes_liked_by_users_user_fk
                IS NOT NULL THEN 1 ELSE 0 END AS is_liked
            FROM recipes
            LEFT JOIN recipes_liked_by_users
            ON recipes.recipe_id = recipes_liked_by_users.recipes_liked_by_users_recipe_fk
            AND recipes_liked_by_users.recipes_liked_by_users_user_fk = ?
        """
        all_recipes = db.execute(all_recipes_query, (user_cookie['user_id'],)).fetchall()

        return template(
            "recipes",
            title="Opskrifter",
            user=user,
            recipes=all_recipes,
            user_cookie=user_cookie,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
