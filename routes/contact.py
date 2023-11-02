from bottle import get, request, template
import x

@get("/kontakt")
def _():
    try:
        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        return template("contact", title="Kontakt", user_cookie=user_cookie)

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()