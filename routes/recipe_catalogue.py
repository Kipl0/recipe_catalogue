from bottle import get, template
import x

# home page
@get("/opskriftskatalog")
def _():
   try:
       db = x.db()

       users = db.execute("SELECT * FROM users").fetchall()
       
       recipes = db.execute("SELECT * FROM recipes").fetchall()

       return template("recipeCatalogue", title="Opskriftskatalog", users=users, recipes=recipes)

   except Exception as ex:
       print(x)
       return {"error": str(ex)}

   finally: 
       if "db" in locals(): db.close()
