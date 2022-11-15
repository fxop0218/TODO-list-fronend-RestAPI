from datetime import datetime, timedelta
from os import getenv
from flask import jsonify
import os
from jwt import decode, encode, exceptions


def data_expiration(days: int):
    now = datetime.now()
    newdate = now + timedelta(days)
    return newdate

def write_token(data: dict):
    token = encode(payload={**data, "exp": data_expiration(2)}, key=getenv("KEY"), algorithm ="HS256")
    return token.encode("UTF-8")

def validate_token(token, output:False): 
    try: 
        if output: 
            return decode(token, key=getenv("KEY"), algorithms=["HS256"])
        decode(token, key=getenv("KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token expired"})
        response.status_code = 401
        return response