#######################################
#           UPDATE PASSWORDS 
#######################################
# koden her er blevet brugt til at opdatere de passwords der manuelt er indtastet fra main.sql, til at blive decrypted, så jeg kan logge ind correct.
# ved brug ---> husk at imorterer routen på ny i app.py


from bottle import get
import x
import bcrypt

@get("/hash_password/<user_username>")
def _(user_username):
    db = x.db()
    user_password = "123"
    user_input_password = user_password.encode('utf-8')

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(user_input_password, salt)


    update_user = db.execute("UPDATE users SET user_password=? WHERE user_username=?", (hashed_password,user_username))
    db.commit()