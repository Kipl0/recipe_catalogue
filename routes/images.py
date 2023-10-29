from bottle import get, static_file

##############################
#      import images - jpg
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/recipe_thumbnails/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")

##############################
#      import images - png
@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/recipe_thumbnails/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")

##############################
#      import images - png
@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/recipe_thumbnails/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")

