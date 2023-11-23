# Funktion til at holde CSP info
def get_csp_directives():
    csp_directives = (
        "script-src 'self'; "
        "style-src 'self';"
        "font-src 'self';"
        "default-src 'self'; "
        "img-src 'self' http://localhost:3000 data:;"
    )
    return csp_directives
