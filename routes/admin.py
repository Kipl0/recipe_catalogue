from bottle import get, request, response, template
import x
from security.csp import get_csp_directives


@get("/admin")
def _():
    try:
        # Sæt CSP 
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)
        
        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_user_jwt(user_cookie)

        # Er der en cookie og i så fald er det admin
        if user_cookie : 
            if user_cookie['user_role'] != "admin":
                response.status = 303 #fordi 303 bruges til redirecting
                response.set_header("Location", "/")
                return
        else :
            #der var ingen cookie
            response.status = 303 #fordi 303 bruges til redirecting
            response.set_header("Location", "/")
            return 

        all_users = db.execute("SELECT * FROM users WHERE user_role != ?", ("admin",)).fetchall()

        return template("admin", title="Admin side", user_cookie=user_cookie, all_users=all_users)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()