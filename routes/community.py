from bottle import get, request, response, template
import x
from utilities.csp import get_csp_directives


@get("/fællesskab")
def _():
    try:
        # Sæt CSP
        csp_directives = get_csp_directives()
        response.set_header('Content-Security-Policy', csp_directives)

        db = x.db()

        # user cookie
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        if user_cookie['user_role'] == 'admin':
            admin = True
        else:
            admin = False

        users = db.execute("SELECT * FROM users WHERE user_role = ? AND user_username != ?",("member", user_cookie['user_username'] )).fetchall()  # noqa




        # Hent alle opskrifter med information om, hvorvidt de er 'liket' af brugeren
        all_users_query = """
            SELECT users.*,
                CASE WHEN follower_following.ff_following_fk
                IS NOT NULL THEN 1 ELSE 0 END AS is_followed
            FROM users
            LEFT JOIN follower_following
            ON users.user_id = follower_following.ff_following_fk
            AND follower_following.ff_follower_fk = ?
            WHERE user_role = 'member'
        """
        all_users = db.execute(all_users_query, (user_cookie['user_id'],)).fetchall()  # noqa



        return template(
            "community",
            title="Fællesskab",
            user_cookie=user_cookie,
            users=all_users,
            admin=admin,
            csrf_token=request.csrf_token
        )

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}

    finally:
        if "db" in locals():
            db.close()
