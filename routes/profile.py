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

        check_user = db.execute("SELECT * FROM users WHERE user_username = ?",(user_username, )).fetchone()
        # Til 404 error handling, hvis ikke brugeren findes
        if check_user is None:
            raise Exception

        
        recipes = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes WHERE recipe_user_fk = ? LIMIT 2",(check_user['user_id'],)).fetchall()        
        collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ? LIMIT 2",(check_user['user_id'],)).fetchall()        

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        return template("profile", title="Profil", recipes=recipes, user=check_user, collections=collections, user_cookie=user_cookie)


    except Exception as ex:
        print(ex)
        raise HTTPError(404, "Brugernavn ikke fundet")


    finally:
        if "db" in locals() : db.close()