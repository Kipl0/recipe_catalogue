from bottle import hook, request, response
from uuid import uuid4


@hook('before_request')
def setup_csrf():
    csrf_token = request.get_cookie('csrf_token', secret='some-secret-key')
    if not csrf_token:
        csrf_token = str(uuid4())
        response.set_cookie('csrf_token', csrf_token, secret='some-secret-key')
    request.csrf_token = csrf_token
