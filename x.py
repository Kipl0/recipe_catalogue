from bottle import request, response
import pathlib
import sqlite3
import re #regex


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



# ##############################
#    Validate user ved register
# ##############################

#-------------------------------
#   Email
EMAIL_MIN = 6
EMAIL_MAX = 100
EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_email():
    error = f"Venligst indtast en gyldig email"
    request.forms.email = request.forms.email.strip() #strip fjerner whitespace
    if len(request.forms.email) < EMAIL_MIN : raise Exception(400, error)
    if len(request.forms.email) > EMAIL_MAX : raise Exception(400, error)
    if not re.match(EMAIL_REGEX, request.forms.email) : raise Exception(400, error)
    return request.forms.email



#-------------------------------
#   username
USERNAME_MIN = 2
USERNAME_MAX = 20
USERNAME_REGEX = "^[a-zA-Z0-9_]*$" #kun engelske bogstaver og tallene fra 0-9

def validate_username():
    error = f"Brugernavn skal være mellem {USERNAME_MIN} og {USERNAME_MAX} tegn, og kun med tallene 0 til 9"
    request.forms.username = request.forms.username.strip() 
    if len(request.forms.username) < USERNAME_MIN: raise Exception(error)
    if len(request.forms.username) > USERNAME_MAX: raise Exception(error)
    if not re.match(USERNAME_REGEX, request.forms.username): raise Exception(error)
    return request.forms.username

#-------------------------------
#   password og confirm password
PASSWORD_MIN = 3
PASSWORD_MAX = 15
PASSWORD_REGEX = "^[a-zA-Z0-9_]*$"

def validate_password():
    error = f"Password skal være bogstaver eller tal, og skal være mellem {PASSWORD_MIN} og {PASSWORD_MAX} karakterer"
    request.forms.password = request.forms.password.strip()
    if len(request.forms.password) < PASSWORD_MIN : raise Exception(400, error)
    if len(request.forms.password) > PASSWORD_MAX : raise Exception(400, error)
    if not re.match(PASSWORD_REGEX, request.forms.password) : raise Exception(400, error) #ikke tjekket om virker endnu
    return request.forms.password

def validate_confirm_password():
    error = "Passwords matcher ikke"
    request.forms.password = request.forms.password.strip()
    request.forms.confirm_password = request.forms.confirm_password.strip()
    if request.forms.password != request.forms.confirm_password : raise Exception(400, error)


#-------------------------------
# Fornavn og efternavn
FIRST_NAME_MIN = 2
FIRST_NAME_MAX = 20

LAST_NAME_MIN = 2
LAST_NAME_MAX = 20

def validate_first_name():
    error = "Indtast venligst et fornavn"
    request.forms.first_name = request.forms.first_name.strip()
    if len(request.forms.first_name) < FIRST_NAME_MIN : raise Exception(400, error)
    if len(request.forms.first_name) > FIRST_NAME_MAX : raise Exception(400, error)
    return request.forms.first_name

def validate_last_name():
    error = "Indtast venligst et efternavn"
    request.forms.last_name = request.forms.last_name.strip()
    if len(request.forms.last_name) < LAST_NAME_MIN : raise Exception(400, error)
    if len(request.forms.last_name) > LAST_NAME_MAX : raise Exception(400, error)
    return request.forms.last_name
