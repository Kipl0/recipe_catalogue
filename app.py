from bottle import get, run, static_file
import x


# Static files
import routes.images

##############################
#     Routes
import routes.home
import routes.recipe
import routes.recipes
import routes.create_recipe
import routes.create_collection
import routes.recipe_catalogue
import routes.collections
import routes.login
import routes.log_out
import routes.register
import routes.reset_password
import routes.about_us
import routes.contact
import routes.profile

##############################
#         Bridges 
import bridges.login


##############################
#     API's
import apis.api_register
import apis.api_create_recipe

##############################
#         css
@get("/app.css")
def _():
    return static_file("app.css", root="")


##############################
#         JS
@get("/js/<filename>") 
def _(filename):
  return static_file(filename, "js")





print("Server running locally")
run(host="127.0.0.1", port=3000, debug=True, reloader=True)
