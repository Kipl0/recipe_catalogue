from bottle import get, template
import x

@get("/reset-password")
def _():
    try:
        db = x.db()

        return template("reset_password", title="Reset password")
    
    except Exception as ex:
        print(ex)
        return{"error :", str(ex)}
    
    finally:
        if "db" in locals() : db.close()