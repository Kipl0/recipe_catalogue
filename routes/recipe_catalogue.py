from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


# home page
@get("/opskriftskatalog")
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
            # Hent alle opskrifter med information om, hvorvidt de er 'liket' af brugeren
            all_recipes_query = """
                SELECT recipes.*,
                    CASE WHEN recipes_liked_by_users.recipes_liked_by_users_user_fk
                    IS NOT NULL THEN 1 ELSE 0 END AS is_liked
                FROM recipes
                LEFT JOIN recipes_liked_by_users
                ON recipes.recipe_id = recipes_liked_by_users.recipes_liked_by_users_recipe_fk
                AND recipes_liked_by_users.recipes_liked_by_users_user_fk = ?
                WHERE recipe_visibility = TRUE
            """
            all_recipes = db.execute(all_recipes_query, (user_cookie['user_id'],)).fetchall()  # noqa
        else:
            print("Ingen bruger er logget ind.")
            all_recipes = db.execute("SELECT * FROM recipes").fetchall()

        


        return template(
            "recipeCatalogue",
            title="Opskriftskatalog",
            all_recipes=all_recipes,
            user_cookie=user_cookie,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
