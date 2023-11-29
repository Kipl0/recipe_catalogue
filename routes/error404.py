from bottle import error, template

@error(404)
def error404(error):
    return template("error404.html")

