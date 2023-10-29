from bottle import get, template
import x

# recipe page
@get("/opskrift/<recipe_id>")
def _(recipe_id):
     try:
          db = x.db()
          
          recipe = db.execute("SELECT * FROM recipes WHERE recipe_id = ?", (recipe_id, )).fetchone()
          recipe_owner = db.execute("SELECT user_username, user_first_name, user_last_name FROM users WHERE user_id = ?", (recipe['recipe_user_fk'], )).fetchone()

          ingredients = db.execute("SELECT ingredient_name FROM ingredients WHERE ingredient_recipe_fk = ? ORDER BY ingredient_order", (recipe_id, )).fetchall()
          steps = db.execute("SELECT step_description FROM steps WHERE step_recipe_fk = ? ORDER BY step_order", (recipe_id, )).fetchall()

          return template("recipe", title="Opskrift", recipe=recipe, recipe_owner=recipe_owner, ingredients=ingredients, steps=steps)

     except Exception as ex:
          print(x)
          return {"error": str(ex)}

     finally: 
          if "db" in locals(): db.close()
