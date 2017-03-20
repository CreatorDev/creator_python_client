#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Python client library for creator device server.
"""

import requests

def get_token(access_key, access_secret, auth_url="https://deviceserver.creatordev.io/oauth/token"):
    """ Gets device server access token. """
    # POST Body Payload for Auth
    payload = {'grant_type': 'password', 'username': access_key, \
    'password': access_secret}
    # POST Request Access Token
    auth_response = requests.post(auth_url, data=payload)
    # Access Token
    token = auth_response.json()['access_token']
    # Auth Bearer, to send on request header
    bearer = "Bearer"+ " "+str(token)
    # GET Request Header
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', \
    'Authorization': bearer}
    return headers

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

def make_url(steps, keyname, query_name, return_key, current_url, headers):
    """ Compose URL helper. """
    cmd_url = ""
    item = steps.get(keyname, "not found")
    if item != "not found":
        query = select_http_method("get", current_url + query_name, headers)
        for i in query.json()["Items"]:
            if i[return_key] == item:
                for j in i["Links"]:
                    if j["rel"] == "self":
                        cmd_url = j["href"]
    return cmd_url

def parse_steps(steps, headers, base_url="https://deviceserver.creatordev.io/"):
    """ Parse string or dictionary to help build the steps. """
    # Verifies if its a string, one step only
    if isinstance(steps, str) and len(steps) > 0:
        instance_url = base_url + steps
        print instance_url
        return instance_url
    else:
        # parse a dictionary with steps
        client_url = make_url(steps, "clients", "clients", "Name", base_url, headers)
        object_url = make_url(steps, "ObjectTypeID", "/objecttypes", "ObjectTypeID", client_url, headers)
        instance_url = make_url(steps, "InstanceID", "/instances", "InstanceID", object_url, headers)
        # print instance_url
    return instance_url

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
        print 'Fail Decoding JSON Response !'
        return response
