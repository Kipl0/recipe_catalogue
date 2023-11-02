from bottle import get, request, template
import x

@get("/reset-password")
def _():
    try:
        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        return template("reset_password", title="Reset password", user_cookie=user_cookie)
    
    except Exception as ex:
        print(ex)
        return{"error :", str(ex)}
    
    finally:
        if "db" in locals() : db.close()