from bottle import get, template
import x

# recipe page
@get("/<recipe_id>")
def _(recipe_id):
   try:
       db = x.db()
       
       recipe = db.execute("SELECT * FROM recipes WHERE recipe_id = ?", (recipe_id,)).fetchone()

       return template("recipe", title="Recipe", recipe=recipe)

   except Exception as ex:
       print(x)
       return {"error": str(ex)}

   finally: 
       if "db" in locals(): db.close()
