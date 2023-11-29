from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


# home page
@get("/mine-favoritter")
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
    
        recipes_liked_by_users = db.execute("SELECT * FROM recipes_liked_by_users WHERE recipes_liked_by_users_user_fk = ?",(user_cookie['user_id'],)).fetchall()

        for liked_recipe in recipes_liked_by_users:
            all_liked_recipes = db.execute("SELECT * FROM recipes WHERE recipe_id = ?",(liked_recipe['recipes_liked_by_users_recipe_fk']))

        return template("favourites", title="Mine favouritter", all_liked_recipes=all_liked_recipes, user_cookie=user_cookie)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally: 
        if "db" in locals(): db.close()
