from bottle import get, request, template
import x

@get("/")
def _():
    try:
        db = x.db()

        suggestions = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes LIMIT 3").fetchall()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie != None :
            # Man kan kun finde user_collections hvis der er en cookie
            user_collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ?", (user_cookie['user_id'],)).fetchall()
            return template("home", title="Forside", suggestions=suggestions, user_cookie=user_cookie, user_collections=user_collections)
        
        return template("home", title="Forside", suggestions=suggestions, user_cookie=user_cookie)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()