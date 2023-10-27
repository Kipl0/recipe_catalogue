from bottle import get, template
import x

@get("/profil")
def _():
    try:
        db = x.db()
        
        recipes = db.execute("SELECT recipe_id, recipe_name, recipe_thumbnail FROM recipes LIMIT 3").fetchall()
        
        return template("profile", title="Profil", recipes=recipes)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()