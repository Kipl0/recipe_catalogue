from bottle import get, request, template
import x

# home page
@get("/opskriftskatalog")
def _():
   try:
        db = x.db()

        users = db.execute("SELECT * FROM users").fetchall()
       
        recipes = db.execute("SELECT * FROM recipes").fetchall()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        return template("recipeCatalogue", title="Opskriftskatalog", users=users, recipes=recipes, user_cookie=user_cookie)

   except Exception as ex:
        print(x)
        return {"error": str(ex)}

   finally: 
        if "db" in locals(): db.close()
