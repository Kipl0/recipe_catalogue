import bottle
from bottle import request
# import pathlib
import sqlite3
import re  # regex
import jwt
import html
import utilities.most_used_passwords as most_used_passwords


# Miljø variabler
COOKIE_SECRET = "85b0f43b-3222-4e65-ada1-0e6ebf22bab6"

JWT_SECRET = "2747ac3f-a909-491a-bb11-28b53f0d5473"
JWT_ALGORITHM = "HS256"

CSRF_TOKEN = "27ca928a-63f8-4bdb-adbf-a94cea378a2f"

# Sæt maksimal filstørrelse til 2 og 5 MB
max_profilepic_size = 2 * 1024 * 1024
max_banner_size = 5 * 1024 * 1024
max_recipe_img_size = 5 * 1024 * 1024

picture_whitelist = [".jpg", ".jpeg", ".png"]


def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


##############################
def db():
    try:
        # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")  # noqa
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
    try:
        user_jwt_result = jwt.decode(user_jwt, JWT_SECRET, algorithms=JWT_ALGORITHM)  # noqa
        return user_jwt_result
    except Exception as ex:
        print(ex, "Vi kan ikke verificere dig")
    finally:
        if "db" in locals():
            db.close()


# ###########################################
#    Validate inputs, og user ved register
# ###########################################
BLACKLIST = ["'", '"', ';', '!', '?', '--', '/*', '*/', 'OR 1=1', 'OR TRUE', 'UNION', 'UNION SELECT', 'DROP', 'DELETE']  # noqa


def check_blacklist(input_str):
    for forbidden_str in BLACKLIST:
        if forbidden_str in input_str:
            raise Exception("Input må ikke indeholde specieltegn")


# -------------------------------
#   Email
# -------------------------------
EMAIL_MIN = 6
EMAIL_MAX = 100
EMAIL_REGEX = "^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"  # noqa


def validate_email():
    error = "Venligst indtast en gyldig email"
    email_input = html.escape(request.forms.email.strip())  # strip fjerner whitespace  # noqa
    check_blacklist(email_input)
    if len(email_input) < EMAIL_MIN:
        raise Exception(error)
    if len(email_input) > EMAIL_MAX:
        raise Exception(error)
    if not re.match(EMAIL_REGEX, email_input):
        raise Exception(error)
    return email_input


# -------------------------------
#   password og confirm password
# -------------------------------
PASSWORD_MIN = 8
PASSWORD_MAX = 25
PASSWORD_REGEX = "^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_]*$"  # bogstaver og tal, mindst 1 tal, mindst 1 stort bogstav  # noqa


def validate_password():
    length_error = f"Password skal være mellem {PASSWORD_MIN} og {PASSWORD_MAX} karakterer"  # noqa
    regex_error = "Password skal indeholde mindst 1 tal og mindst 1 stort bogstav"  # noqa
    user_password = html.escape(request.forms.password.strip())
    check_blacklist(user_password)
    user_first_name = request.forms.first_name.strip()
    user_last_name = request.forms.last_name.strip()

    # Hvis password ikke overholder minimum og maksimum
    if len(user_password) > PASSWORD_MAX:
        raise Exception(length_error)
    if len(user_password) < PASSWORD_MIN:
        raise Exception(length_error)
    if not re.match(PASSWORD_REGEX, user_password):
        raise Exception(regex_error)  # ikke tjekket om virker endnu

    # Password må ikke indeholde for eller efternavn
    if (user_first_name.lower() in user_password.lower() or user_last_name.lower() in user_password.lower()):  # noqa
        raise Exception("Password må ikke indeholde for- eller efternavn")

    # Password må ikke være på top 50 mest brugte passwords
    if user_password in most_used_passwords.most_used_passwords:
        raise Exception("Dit valgte password er ikke unikt nok")

    return user_password


def validate_confirm_password():
    error = "Passwords matcher ikke"
    user_password = request.forms.password.strip()
    confirm_password = html.escape(request.forms.confirm_password.strip())
    check_blacklist(confirm_password)
    if user_password != confirm_password:
        raise Exception(error)


# -------------------------------
#      Username
# -------------------------------
USERNAME_MIN = 3
USERNAME_MAX = 20
# USERNAME_REGEX = "^[a-zA-Z0-9_]*$" #kun engelske bogstaver og tallene fra 0-9


def validate_username():
    error = "Indtast venligst et gyldigt brugernavn"
    username = html.escape(request.forms.username.strip())
    check_blacklist(username)
    if len(username) < USERNAME_MIN:
        raise Exception(error)
    if len(username) > USERNAME_MAX:
        raise Exception(error)
    # henter en liste over alle end points
    all_endpoints = [route.rule for route in bottle.default_app().routes]

    # Tjekker om brugernavn findes i end point
    if username in all_endpoints:
        raise Exception(error)
    return username


# -------------------------------
#    Fornavn og efternavn
# -------------------------------
FIRST_NAME_MIN = 2
FIRST_NAME_MAX = 20

LAST_NAME_MIN = 2
LAST_NAME_MAX = 20


def validate_first_name():
    error = "Indtast venligst et gyldigt fornavn"
    first_name = html.escape(request.forms.first_name.strip())
    check_blacklist(first_name)
    if len(first_name) < FIRST_NAME_MIN or len(first_name) > FIRST_NAME_MAX:
        raise Exception(error)
    return first_name


def validate_last_name():
    error = "Indtast venligst et gyldigt efternavn"
    last_name = html.escape(request.forms.last_name.strip())
    check_blacklist(last_name)
    if len(last_name) < LAST_NAME_MIN:
        raise Exception(error)
    if len(last_name) > LAST_NAME_MAX:
        raise Exception(error)
    return last_name
