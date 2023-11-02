from bottle import get, request, template
import x

@get("/om-os")
def _():
    try:
        db = x.db()
        
        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        return template("about_us", title="Om os", user_cookie=user_cookie)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()