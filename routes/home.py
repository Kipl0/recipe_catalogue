from bottle import get, request, template
import x

@get("/")
def _():
    try:
        db = x.db()

        suggestions = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes LIMIT 3").fetchall()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        return template("home", title="Forside", suggestions=suggestions, user_cookie=user_cookie)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()