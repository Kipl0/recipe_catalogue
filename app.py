from bottle import get, run, template, static_file
import x

import routes.recipe
import routes.home
import routes.recipe_catalogue
import routes.login
import routes.register
import routes.reset_password
import routes.about_us

##############################
#         css
@get("/app.css")
def _():
    return static_file("app.css", root="")

##############################
#      import images - jpg
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/recipe_thumbnails/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")


##############################
#         JS
@get("/js/<filename>") 
def _(filename):
  return static_file(filename, "js")





print("Server running locally")
run(host="127.0.0.1", port=3000, debug=True, reloader=True)
