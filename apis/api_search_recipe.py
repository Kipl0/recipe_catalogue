from bottle import post, request, response

# normalt ville man bruge "get" fordi man skal "get" noget fra db.
# Men fordi get har det med at cache, bruger vi post
import json  # bruges for at kunne returnere en list i try
import x


@post("/search-recipe")
def _():
    try:
        db = x.db()

        search_input = request.forms.get("search_input")

        search_results = db.execute(
            f"SELECT * FROM recipes_search WHERE recipes_search MATCH 'recipe_name:{search_input}*'"  # noqa
        ).fetchall()

        # fortæller js at der returneres json - det bruges ikke endnu på js -
        # før linje 20 kunne man lave et tjek om resultatet faktisk er json
        response.set_header("Content-type", "application/json")
        return json.dumps(search_results)

    except Exception as e:
        print(e)
        pass

    finally:
        pass
