from bottle import get, request, template
import x

@get("/<user_username>")
def _(user_username):
    try:
        db = x.db()

        # skal bruges til at få opskrifter og samlinger
        user_id = db.execute("SELECT user_id FROM users WHERE user_username = ?", (user_username, )).fetchone()
        
        recipes = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes WHERE recipe_user_fk = ? LIMIT 2",(user_id['user_id'],)).fetchall()        
        collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ? LIMIT 2",(user_id['user_id'],)).fetchall()        
        user = db.execute("SELECT * FROM users WHERE user_username = ? COLLATE NOCASE", (user_username, )).fetchone()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)


        return template("profile", title="Profil", recipes=recipes, user=user, collections=collections, user_cookie=user_cookie)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()