from bottle import post, request, response
# normalt ville man bruge "get" fordi man skal "get" noget fra db. Men fordi get har det med at cache, bruger vi post
import json #bruges for at kunne returnere en list i try
import x

@post("/search-user")
def _() :
    try :
        db = x.db()

        search_input = request.forms.get("search_input")

        search_results = db.execute(f"SELECT * FROM users_search WHERE users_search MATCH 'user_username:{search_input}* OR user_first_name:{search_input}* OR user_last_name:{search_input}*'").fetchall()

        response.set_header("Content-type","application/json") #fortæller js at der returneres json - det bruges ikke endnu på js - før linje 20 kunne man lave et tjek om resultatet faktisk er json
        return json.dumps(search_results)

    except Exception as e :
        print(e)
        pass

    finally :
        pass