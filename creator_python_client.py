#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Python client library for creator device server.
"""

import requests


def get_token(access_key, access_secret,
              auth_url="https://deviceserver.creatordev.io/oauth/token"):
    """ Gets device server access token. """
    try:
        # POST Body Payload for Auth
        payload = {
            'grant_type': 'password',
            'username': access_key,
            'password': access_secret
            }
        # POST Request Access Token
        auth_response = requests.post(auth_url, data=payload)
        # Access Token
        token = auth_response.json()['access_token']
        # Auth Bearer, to send on request header
        bearer = "Bearer" + " "+str(token)
        # GET Request Header
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization': bearer
            }
        return headers
    except ValueError:
        print ('Invalid key and secret !')


def select_http_method(method, url, headers, **data):
    """ Selects HTTP method from requests module. """
    if method == "get":
        response = requests.get(url, headers=headers)
    elif method == "put":
        response = requests.put(url, headers=headers, json=data)
    elif method == "post":
        response = requests.post(url, headers=headers)
    elif method == "del":
        response = requests.delete(url, headers=headers)
    else:
        raise Exception("Invalid HTTP method!")
    return response


def query_url(value, query_name, return_key, current_url, headers):
    """ Compose URL helper. """
    cmd_url = ""
    query = select_http_method("get", current_url + query_name, headers)
    for i in query.json()["Items"]:
        if i[return_key] == value:
            for j in i["Links"]:
                if j["rel"] == "self":
                    cmd_url = j["href"]
    if cmd_url == "":
        raise Exception("not found ", query_name, "with value of ", value)
    return cmd_url


def query_naming(name):
    """TODO moving to a config file"""
    if name == "clients":
        query_key = "Name"
        add_url = "clients"
    elif name == "ObjectTypeID":
        query_key = "ObjectTypeID"
        add_url = "objecttypes"
    elif name == "InstanceID":
        query_key = "InstanceID"
        add_url = "instances"
    else:
        raise "invalid naming"
    return query_key, add_url


def parse_steps(steps, headers, base_url="https://deviceserver.creatordev.io"):
    """ Parse string or dictionary to help build the steps. """
    result_url = base_url
    # Verifies if its a string, one step only
    if isinstance(steps, str) and len(steps) > 0:
        result_url = base_url + steps
    elif isinstance(steps, list):
        for step in steps:
            if isinstance(step, str):
                result_url = result_url + "/" + step
            elif isinstance(step, tuple) and len(step) > 1:
                query_key = query_naming(step[0])[0]
                add_url = "/" + query_naming(step[0])[1]
                result_url = query_url(
                    step[1], add_url, query_key, result_url, headers)
            else:
                raise Exception("invalid steps")
    else:
        pass
    return result_url


def request(access_key, access_secret, method="get", steps="versions", **data):
    """
    Request method
    """
    try:
        headers = get_token(access_key, access_secret)
        url = parse_steps(steps, headers)
        response = select_http_method(method, url, headers, **data)
        return response.json()
    except ValueError:
        print ('Fail Decoding JSON Response !')
        return response
