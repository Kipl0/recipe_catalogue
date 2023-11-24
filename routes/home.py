from bottle import get, request, template, response
import x
from security.csp import get_csp_directives

@get("/")
def _():
    try:
        # Sæt CSP 
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)
        
        db = x.db()

        suggestions = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes LIMIT 3").fetchall()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_user_jwt(user_cookie)

        if user_cookie != None :
            # Man kan kun finde user_collections hvis der er en cookie
            user_collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ?", (user_cookie['user_id'],)).fetchall()
            for user_collection in user_collections:
                print(user_collection['recipe_id'])
                print(user_collection['recipe_thumbnail'])
                print(user_collection['collection_name'])
            return template("home", title="Forside", suggestions=suggestions, user_cookie=user_cookie, user_collections=user_collections)

            


        return template("home", title="Forside", suggestions=suggestions, user_cookie=user_cookie)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()