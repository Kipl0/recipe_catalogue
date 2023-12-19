from bottle import get, request, template, response
import x
from utilities.csp import get_csp_directives


@get("/")
def _():
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        db = x.db()

        suggestions = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes LIMIT 3").fetchall()  # noqa

        if user_cookie is not None:
            # Man kan kun finde user_collections, hvis der er en cookie
            user_collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ?", (user_cookie['user_id'],)).fetchall()  # noqa

            # LEFT JOIN
            recipe_not_liked_query = """
                SELECT r.recipe_id, r.recipe_name, r.recipe_thumbnail
                FROM recipes r
                LEFT JOIN recipes_liked_by_users l
                    ON r.recipe_id = l.recipes_liked_by_users_recipe_fk
                    AND l.recipes_liked_by_users_user_fk = ?
                WHERE l.recipes_liked_by_users_user_fk IS NULL
                    AND r.recipe_visibility = TRUE
                LIMIT 3;
            """

            suggestions = db.execute(recipe_not_liked_query, (user_cookie['user_id'],)).fetchall()  # noqa

            # Hvis den er 0, så har de ikke liket opskriften
            return template(
                "home",
                title="Forside",
                suggestions=suggestions,
                user_cookie=user_cookie,
                user_collections=user_collections,
                csrf_token=request.csrf_token
            )

        return template(
            "home",
            title="Forside",
            suggestions=suggestions,
            user_cookie=user_cookie,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
