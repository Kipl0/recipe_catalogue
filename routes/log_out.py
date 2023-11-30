from bottle import get, response
from utilities.csp import get_csp_directives


@get("/log-out")
def _():
    # Sæt CSP
    csp_directives = get_csp_directives()
    response.set_header('Content-Security-Policy', csp_directives)
    # slet cookie
    response.set_cookie("user_cookie", "", expires=0)
    # Sætter ny lokation
    response.status = 303
    response.set_header("Location", "/")
    return
