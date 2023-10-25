from bottle import get, template
import x

@get("/opret-bruger")
def _():
    try:
        db = x.db()

        return template("register", title="Opret bruger")
    
    except Exception as ex:
        print(ex)
        return{"error :", str(ex)}
    
    finally:
        if "db" in locals() : db.close()