from bottle import get, request, response, template
import x
from security.csp import get_csp_directives


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
            response.status = 303 #fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return

        user_recipes = db.execute("SELECT * FROM recipes WHERE recipe_user_fk = ?", (user_cookie['user_id'],)).fetchall()
        if user_recipes is []: 
            user_recipes = "Du har ikke oprettet nogle opskrifter endnu"


        # recipes_liked_by_user_ids = db.execute("SELECT recipes_liked_by_users_recipe_fk FROM recipes_liked_by_users WHERE recipes_liked_by_users_user_fk = ?", (user_cookie['user_id'],)).fetchall()
        # if recipes_liked_by_user_ids != None :
        #     for recipes_liked_by_user_id in recipes_liked_by_user_ids :
        #         recipes_liked_by_user = db.execute("SELECT * FROM recipes WHERE recipe_id = ?", (recipes_liked_by_user_id,)).fetchall()
        # else : 
        #     user_recipes = "Du har ikke liket nogle opskrifter endnu"

        return template("create_collection", title="Opret samling", user_cookie=user_cookie, user_recipes=user_recipes)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally: 
        if "db" in locals(): db.close()
