import bottle
from bottle import request, response
import pathlib
import sqlite3
import re #regex
import jwt
import utilities.most_used_passwords as most_used_passwords

COOKIE_SECRET = "85b0f43b-3222-4e65-ada1-0e6ebf22bab6"

JWT_SECRET = "2747ac3f-a909-491a-bb11-28b53f0d5473"
JWT_ALGORITHM = "HS256"

def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


##############################
def db():
    try:
        # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db = sqlite3.connect("recipe.db")  
        # db.execute("PRAGMA foreign_keys=ON;")
        db.row_factory = dict_factory
        return db
    except Exception as ex:
        print(ex)
    finally:
        pass


# #############################
# Validate jwt
def validate_user_jwt(user_jwt):
  try :
    user_jwt_result = jwt.decode(user_jwt, JWT_SECRET, algorithms=JWT_ALGORITHM)
    return user_jwt_result
  except Exception as ex :
    print(ex, "We cannot verify you")
  finally:
    if "db" in locals(): db.close()





# ##############################
#    Validate user ved register
# ##############################
#-------------------------------
#   Email
#-------------------------------
EMAIL_MIN = 6
EMAIL_MAX = 100
EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
EMAIL_REGEX = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

def validate_email():
    error = f"Venligst indtast en gyldig email"
    request.forms.email = request.forms.email.strip() #strip fjerner whitespace
    if len(request.forms.email) < EMAIL_MIN : raise Exception(error)
    if len(request.forms.email) > EMAIL_MAX : raise Exception(error)
    if not re.match(EMAIL_REGEX, request.forms.email) : raise Exception(error)
    return request.forms.email




#-------------------------------
#   password og confirm password
#-------------------------------
PASSWORD_MIN = 3
PASSWORD_MAX = 15
PASSWORD_REGEX = "^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_]*$" # bogstaver og tal, mindst 1 tal, mindst 1 stort bogstav

def validate_password():
    length_error = f"Password skal være mellem {PASSWORD_MIN} og {PASSWORD_MAX} karakterer"
    regex_error = f"Password skal indeholde mindst 1 tal og mindst 1 stort bogstav"
    user_password = request.forms.password.strip()
    user_first_name = request.forms.first_name.strip()
    user_last_name = request.forms.last_name.strip()
    
    # Hvis password ikke overholder minimum og maksimum
    if len(user_password) < PASSWORD_MIN : raise Exception(length_error)
    if len(user_password) > PASSWORD_MAX : raise Exception(length_error)
    if not re.match(PASSWORD_REGEX, user_password) : raise Exception(regex_error) #ikke tjekket om virker endnu
    
    # Password må ikke indeholde for eller efternavn
    if ( user_first_name.lower() in user_password.lower() or user_last_name.lower() in user_password.lower() ): raise Exception("Password må ikke indeholde for- eller efternavn")
    
    # Password må ikke være på top 50 mest brugte passwords
    if user_password in most_used_passwords.most_used_passwords : raise Exception("Dit valgte password er ikke unikt nok")
    
    return user_password

def validate_confirm_password():
    error = f"Passwords matcher ikke"
    user_password = user_password = request.forms.password.strip()
    request.forms.confirm_password = request.forms.confirm_password.strip()
    if user_password != request.forms.confirm_password : raise Exception(error)




#-------------------------------
#      Username
#-------------------------------
USERNAME_MIN = 3
USERNAME_MAX = 20
USERNAME_REGEX = "^[a-zA-Z0-9_]*$" #kun engelske bogstaver og tallene fra 0-9

def validate_username():
    error = f"Indtast venligst et gyldigt brugernavn"
    username = request.forms.username.strip()
    if len(username) < USERNAME_MIN : raise Exception(error)
    if len(username) > USERNAME_MAX : raise Exception(error)
    if not re.match(USERNAME_REGEX, request.forms.username): raise Exception(error)
    # henter en liste over alle end points
    all_endpoints = [route.rule for route in bottle.default_app().routes]

    # Tjekker om brugernavn findes i end point
    if username in all_endpoints: raise Exception(error)
    return username




#-------------------------------
#    Fornavn og efternavn
#-------------------------------
FIRST_NAME_MIN = 2
FIRST_NAME_MAX = 20

LAST_NAME_MIN = 2
LAST_NAME_MAX = 20

def validate_first_name():
    error = f"Indtast venligst et gyldigt fornavn"
    first_name = request.forms.first_name.strip()
    if len(first_name) < FIRST_NAME_MIN or len(first_name) > FIRST_NAME_MAX:
         raise Exception(error)
    return first_name


def validate_last_name():
    error = f"Indtast venligst et gyldigt efternavn"
    last_name = request.forms.last_name.strip()
    if len(last_name) < LAST_NAME_MIN : raise Exception(error)
    if len(last_name) > LAST_NAME_MAX : raise Exception(error)
    return last_name
