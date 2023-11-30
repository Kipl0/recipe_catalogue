from bottle import post, response, request
import x


@post("/delete-user")
def _():
    try:
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        if user_cookie is None:
            return {"info": "Du skal logge ind for at kunne følge brugere"}

        db = x.db()
        user_id = request.forms.get("user_id")

        db.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        db.commit()

        return {"info": "ok"}

    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info": ex.args[1]}

        except Exception as ex:
            response.status = 500
            print(ex)
            return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
