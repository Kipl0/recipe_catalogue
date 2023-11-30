from bottle import get, run, static_file

# utilities
import utilities.hash_password  # bruges kun til udvikling
import utilities.csrf

# Static files
import routes.images

##############################
#     Routes
import routes.about_us
import routes.admin
import routes.contact
import routes.collections
import routes.create_collection
import routes.create_recipe
import routes.home
import routes.login
import routes.log_out
import routes.profile
import routes.recipe
import routes.recipes
import routes.recipe_catalogue
import routes.register
import routes.reset_password
import routes.favourites
import routes.error404

##############################
#         Bridges
import bridges.login

##############################
#     API's
import apis.api_register
import apis.api_create_recipe
import apis.api_create_collection
import apis.api_update_profile
import apis.api_like_recipe


# #############################
#         css
@get("/app.css")
def _():
    return static_file("app.css", root="")


# #############################
#         JS
@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")


print("Server running locally")
run(host="127.0.0.1", port=3000, debug=True, reloader=True)
