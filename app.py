from bottle import get, run, static_file
import x


# Static files
import routes.images

# Pages
import routes.recipe
import routes.home
import routes.recipe_catalogue
import routes.login
import routes.register
import routes.reset_password
import routes.about_us
import routes.contact
import routes.profile

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
