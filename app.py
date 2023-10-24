from bottle import get, run, template, static_file
import x

@get("/app.css")
def _():
    return static_file("app.css", root="")

######################## import images - jpg
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/")
def render_index():
   try:
       db = x.db()

       user = db.execute("SELECT * FROM users").fetchall()[0]
       return template("index", title="Recipes", user=user)
   
   except Exception as ex:
       print(x)
       return {"error": str(ex)}
   
   finally: 
       if "db" in locals(): db.close()



print("Server running locally")
run(host="127.0.0.1", port=3000, debug=True, reloader=True)
