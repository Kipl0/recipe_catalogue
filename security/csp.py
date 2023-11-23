def get_csp_directives():
    csp_directives = (
        "script-src 'self'; "
        "style-src 'self' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "default-src 'self'; "
        "img-src 'self' http://localhost:3000 data:;"
    )
    return csp_directives