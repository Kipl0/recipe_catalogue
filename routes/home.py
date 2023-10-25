from bottle import get, template
import x

@get("/")
def _():
    try:
        db = x.db()

        return template("home", title="Forside")

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()