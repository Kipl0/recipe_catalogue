from bottle import get, response

@get("/log-out")
def _():
    #slet cookie
    response.set_cookie("user_cookie", "", expires=0) 
    # Sætter ny lokation
    response.status = 303
    response.set_header("Location", "/")
    return
