from bottle import get, template
import x

@get("/<user_username>")
def _(user_username):
    try:
        db = x.db()

        # skal bruges til at få opskrifter og samlinger
        user_id = db.execute("SELECT user_id FROM users WHERE user_username = ?", (user_username, )).fetchone()
        
        recipes = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes WHERE recipe_user_fk = ? LIMIT 3",(user_id['user_id'],)).fetchall()        
        collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ? LIMIT 3",(user_id['user_id'],)).fetchall()        
        user = db.execute("SELECT * FROM users WHERE user_username = ? COLLATE NOCASE", (user_username, )).fetchone()

        return template("profile", title="Profil", recipes=recipes, user=user, collections=collections)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()