from bottle import get, run, template, static_file
import x

@get("/app.css")
def _():
    return static_file("app.css", root="")

######################## import images - jpg
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/recipe_thumbnails/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")


import routes.recipe
import routes.recipe_catalogue


print("Server running locally")
run(host="127.0.0.1", port=3000, debug=True, reloader=True)
