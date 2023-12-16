from bottle import default_app, get, run, static_file, post
import git

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
import routes.community
import routes.create_collection
import routes.create_recipe
import routes.error404
import routes.favourites
import routes.home
import routes.login
import routes.log_out
import routes.profile
import routes.recipe
import routes.recipes
import routes.recipe_catalogue
import routes.register
import routes.reset_password

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
import apis.api_follow
import apis.api_delete
import apis.api_search_user
import apis.api_search_recipe



##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


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




###################################
# Run in AWS
# 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
try:
    import production # If this production is found, the next line should run
    print("Server running on AWS") # You will never see this line in your own computer - only on amazon
    application = default_app()
# Run in local computer
except Exception as ex:    
    print("Server running locally")
    run(host="127.0.0.1", port=3000, debug=True, reloader=True) #If it cant run it will run locally

 
###################################
# Continously interation from Github to python anywhere
@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./recipe_catalogue')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return ""
