from bottle import get, template
import x

@get("/login")
def _():
    try:
        db = x.db()

        return template("login", title="Login")

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()