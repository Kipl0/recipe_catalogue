from bottle import get, template
import x

@get("/om-os")
def _():
    try:
        db = x.db()
        
        return template("about_us", title="Om os",)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()