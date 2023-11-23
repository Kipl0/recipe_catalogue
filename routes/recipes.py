from bottle import get, request, response, template
import x
from security.csp import get_csp_directives


@get("/<user_username>/opskrifter")
def _(user_username):
    try:
        # Sæt CSP 
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        db = x.db()

        user = db.execute("SELECT * FROM users WHERE user_username = ? COLLATE NOCASE", (user_username, )).fetchone()
            
        recipes = db.execute("SELECT * FROM recipes WHERE recipe_user_fk = ?",(user['user_id'],)).fetchall()        

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_user_jwt(user_cookie)

        return template("recipes", title="Opskrifter", user=user, recipes=recipes, user_cookie=user_cookie)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()