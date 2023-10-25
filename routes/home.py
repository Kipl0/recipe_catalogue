from bottle import get, template
import x

@get("/")
def _():
    try:
        db = x.db()

        suggestions = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes LIMIT 3").fetchall()

        return template("home", title="Forside", suggestions=suggestions)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()