from bottle import get, request, template
import x

@get("/<user_username>/samlinger")
def _(user_username):
    try:
        db = x.db()

        user = db.execute("SELECT * FROM users WHERE user_username = ? COLLATE NOCASE", (user_username, )).fetchone()
            
        collections = db.execute("SELECT * FROM collections WHERE collection_user_fk = ?",(user['user_id'],)).fetchall()        

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)


        return template("collections", title="Samlinger", user=user, collections=collections, user_cookie=user_cookie)

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


    finally:
        if "db" in locals() : db.close()