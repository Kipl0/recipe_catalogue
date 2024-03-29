from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/<user_username>/samlinger")
def _(user_username):
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header("Content-Security-Policy", csp_directives)

        db = x.db()

        user = db.execute(
            "SELECT * FROM users WHERE user_username = ? COLLATE NOCASE",
            (user_username,),
        ).fetchone()  # noqa

        collections = db.execute(
            "SELECT * FROM collections WHERE collection_user_fk = ?",
            (user["user_id"],)
        ).fetchall()  # noqa

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        return template(
            "collections",
            title="Samlinger",
            user=user,
            collections=collections,
            user_cookie=user_cookie,
        )

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
