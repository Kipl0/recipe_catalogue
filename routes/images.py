from bottle import get, static_file


# #############################
#      import images - jpg
@get("/images/<filename:re:.*\.jpg>")  # noqa
def _(filename):
    return static_file(filename, root="./images")  # noqa


@get("/images/recipe_thumbnails/<filename:re:.*\.jpg>")  # noqa
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")  # noqa


# #############################
#      import images - png
@get("/images/<filename:re:.*\.png>")  # noqa
def _(filename):
    return static_file(filename, root="./images")  # noqa


@get("/images/recipe_thumbnails/<filename:re:.*\.png>")  # noqa
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")  # noqa


# #############################
#      import images - png
@get("/images/<filename:re:.*\.jpeg>")  # noqa
def _(filename):
    return static_file(filename, root="./images")  # noqa


@get("/images/recipe_thumbnails/<filename:re:.*\.jpeg>")  # noqa
def _(filename):
    return static_file(filename, root="./images/recipe_thumbnails")  # noqa
