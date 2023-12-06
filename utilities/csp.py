# Funktion til at holde CSP info
def get_csp_directives():
    csp_directives = (
        "script-src 'self'; "
        "style-src 'self' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "default-src 'self'; "
        "img-src 'self' http://localhost:3000 data:; "
        # "object-src 'none'; "  # Forhindrer brug af <object> tags
        # "media-src 'none'; "   # Forhindrer brug af <audio> og <video> tags
        # "child-src 'none'; "   # Forhindrer indlejring af ressourcer i <frame>, <iframe>, <object>
        # "connect-src 'self'; "  # Tillader kun forbindelser til samme origin
        # "frame-src 'none'; "   # Forhindrer brug af <frame> og <iframe>
    )
    return csp_directives