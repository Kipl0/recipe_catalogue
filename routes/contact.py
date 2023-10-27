from bottle import get, template
import x

@get("/kontakt")
def _():
    try:
        db = x.db()


        return template("contact", title="Kontakt")

    except Exception as ex:
        print(x)
        return {"error": str(ex)}

    finally:
        if "db" in locals() : db.close()