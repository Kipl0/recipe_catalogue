from bottle import get, template
import x

# home page
@get("/")
def render_index():
   try:
       db = x.db()

       users = db.execute("SELECT * FROM users").fetchall()
       
       recipes = db.execute("SELECT * FROM recipes").fetchall()

       return template("index", title="Recipes", users=users, recipes=recipes)

   except Exception as ex:
       print(x)
       return {"error": str(ex)}

   finally: 
       if "db" in locals(): db.close()
