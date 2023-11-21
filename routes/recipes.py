from bottle import get, request, template
import x

@get("/<user_username>/opskrifter")
def _(user_username):
    try:
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