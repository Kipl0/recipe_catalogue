from bottle import post, response, request
import x


@post("/follow-user")
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

        follower_following_record = db.execute(
            """SELECT * FROM follower_following
            WHERE ff_follower_fk = ?
            AND ff_following_fk = ?""",
            (user_cookie["user_id"], user_id),
        ).fetchone()  # noqa

        user_followed = db.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()  # noqa
        user_total_followers = user_followed["user_total_followers"]

        # Hvis den er 0, så har de ikke liket opskriften
        if follower_following_record is None:
            db.execute(
                "INSERT INTO follower_following VALUES(?,?)",
                (user_cookie["user_id"], user_id),
            )  # noqa
            db.commit()

            # logget ind bruger får flere following
            db.execute(
                """UPDATE users
                SET user_total_following = user_total_following + 1
                WHERE user_id = ?""",
                (user_cookie["user_id"],),
            )  # noqa
            db.commit()

            # Den anden bruger får flere followers
            db.execute(
                """UPDATE users
                SET user_total_followers = user_total_followers + 1
                WHERE user_id = ?""",
                (user_id,),
            )  # noqa
            db.commit()

            return {
                "info": "ok",
                "user_id": user_id,
                "user_total_followers": int(user_total_followers) + 1,
            }

        db.execute(
            """DELETE FROM follower_following
            WHERE ff_follower_fk = ?
            AND ff_following_fk = ?""",
            (user_cookie["user_id"], user_id),
        )  # noqa
        db.commit()

        # logget ind bruger får færre following
        db.execute(
            """UPDATE users
            SET user_total_following = user_total_following - 1
            WHERE user_id = ?""",
            (user_cookie["user_id"],),
        )  # noqa
        db.commit()

        # Den anden bruger får færre followers
        db.execute(
            """UPDATE users
            SET user_total_followers = user_total_followers - 1
            WHERE user_id = ?""",
            (user_id,),
        )  # noqa
        db.commit()

        return {
            "info": "ok",
            "user_id": user_id,
            "user_total_followers": int(user_total_followers) - 1,
        }

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
