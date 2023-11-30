from bottle import post, response, request
import x


@post("/like-opskrift")
def _():
    try:
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie is not None:
            user_cookie = x.validate_user_jwt(user_cookie)
        else:
            print("Ingen bruger er logget ind.")

        if user_cookie is None:
            return {"info": "Du skal logge ind for at kunne like tweets"}

        db = x.db()
        recipe_id = request.forms.get("recipe_id")

        recipes_liked_by_user_record = db.execute("SELECT * FROM recipes_liked_by_users WHERE recipes_liked_by_users_user_fk = ? AND recipes_liked_by_users_recipe_fk = ?", (user_cookie["user_id"], recipe_id)).fetchone()  # noqa

        recipe_liked = db.execute("SELECT * FROM recipes WHERE recipe_id = ?",(recipe_id,)).fetchone()  # noqa
        recipe_total_likes = recipe_liked["recipe_total_likes"]

        # Hvis den er 0, så har de ikke liket opskriften
        if recipes_liked_by_user_record is None:
            db.execute("INSERT INTO recipes_liked_by_users VALUES(?,?)",(user_cookie["user_id"], recipe_id))  # noqa
            db.commit()

            db.execute("UPDATE recipes SET recipe_total_likes = recipe_total_likes + 1 WHERE recipe_id = ?",(recipe_id,))  # noqa
            db.commit()

            return {"info": "ok", "recipe_id": recipe_id, "recipe_total_likes": int(recipe_total_likes) + 1}  # noqa

        db.execute("DELETE FROM recipes_liked_by_users WHERE recipes_liked_by_users_recipe_fk = ?",(recipe_id,))  # noqa
        db.commit()
        db.execute("UPDATE recipes SET recipe_total_likes = recipe_total_likes - 1 WHERE recipe_id = ?",(recipe_id,))  # noqa
        db.commit()

        return {
            "info": "ok",
            "recipe_id": recipe_id,
            "recipe_total_likes": int(recipe_total_likes) - 1
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
