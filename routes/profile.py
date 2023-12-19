# flake8: noqa
from bottle import get, request, response, template, HTTPError
import x
from utilities.csp import get_csp_directives


@get("/<user_username>")
def _(user_username):
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        db = x.db()

        check_user = db.execute("SELECT * FROM users WHERE user_username = ?",(user_username, )).fetchone()  # noqa
        # Til 404 error handling, hvis ikke brugeren findes
        if check_user is None:
            raise Exception

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
            # Hent alle opskrifter med information om,
            # hvorvidt de er 'liket' af brugeren
            if user_cookie['user_username'] == user_username:
                recipes = """
                    SELECT recipes.*,
                    CASE WHEN recipes_liked_by_users.recipes_liked_by_users_user_fk
                    IS NOT NULL THEN 1 ELSE 0 END AS is_liked
                    FROM recipes
                    LEFT JOIN recipes_liked_by_users
                    ON recipes.recipe_id = recipes_liked_by_users.recipes_liked_by_users_recipe_fk
                    AND recipes_liked_by_users.recipes_liked_by_users_user_fk = ?
                    WHERE recipes.recipe_user_fk = ?
                    LIMIT 2
                """
                recipes = db.execute(recipes, (check_user['user_id'], check_user['user_id'])).fetchall()  # noqa
            else:
                recipes = """
                    SELECT recipes.*,
                    CASE WHEN recipes_liked_by_users.recipes_liked_by_users_user_fk
                    IS NOT NULL THEN 1 ELSE 0 END AS is_liked
                    FROM recipes
                    LEFT JOIN recipes_liked_by_users
                    ON recipes.recipe_id = recipes_liked_by_users.recipes_liked_by_users_recipe_fk
                    AND recipes_liked_by_users.recipes_liked_by_users_user_fk = ?
                    WHERE recipes.recipe_user_fk = ?
                    AND recipe_visibility = TRUE
                    LIMIT 2
                """
                recipes = db.execute(recipes, (check_user['user_id'], check_user['user_id'])).fetchall()  # noqa
        else:
            print("Ingen bruger er logget ind.")
            recipes = """
                SELECT recipes.*,
                CASE WHEN recipes_liked_by_users.recipes_liked_by_users_user_fk
                IS NOT NULL THEN 1 ELSE 0 END AS is_liked
                FROM recipes
                LEFT JOIN recipes_liked_by_users
                ON recipes.recipe_id = recipes_liked_by_users.recipes_liked_by_users_recipe_fk
                AND recipes_liked_by_users.recipes_liked_by_users_user_fk = ?
                WHERE recipes.recipe_user_fk = ?
                AND recipe_visibility = TRUE
                LIMIT 2
            """
            recipes = db.execute(recipes, (check_user['user_id'], check_user['user_id'])).fetchall()  # noqa

        collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ? LIMIT 2",(check_user['user_id'],)).fetchall()  # noqa  

        return template(
            "profile",
            title="Profil",
            recipes=recipes,
            user=check_user,
            collections=collections,
            user_cookie=user_cookie,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(ex)
        raise HTTPError(404, "Brugernavn ikke fundet")

    finally:
        if "db" in locals():
            db.close()
