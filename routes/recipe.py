from bottle import get, template
import x

# recipe page
@get("/<recipe_id>")
def _(recipe_id):
   try:
        db = x.db()
       
        recipe = db.execute("SELECT * FROM recipes WHERE recipe_id = ?", (recipe_id, )).fetchone()
        recipe_owner = db.execute("SELECT user_username, user_first_name, user_last_name FROM users WHERE user_id = ?", (recipe['recipe_user_fk'], )).fetchone()

        return template("recipe", title="Opskrift", recipe=recipe, recipe_owner=recipe_owner)

   except Exception as ex:
        print(x)
        return {"error": str(ex)}

   finally: 
        if "db" in locals(): db.close()
