![logo](https://static.creatordev.io/logo-md-s.svg)

# Creator Python Client

The python client allows you to use 
[The Creator IoT Framework](https://docs.creatordev.io/deviceserver/guides/iot-framework/), 
giving the possibility to quickly implement a client, to consume the Device 
Server REST API.

[![Build Status](https://travis-ci.org/CreatorDev/creator_python_client.svg?branch=master)](https://travis-ci.org/CreatorDev/creator_python_client)

---

## Table of Contents

* [Getting Started](#getting-started)
* [Jump Start](#jump-start)
* [The Request Method](#the-request-method)
    * [Supported HTTP Methods](#supported-http-methods)
    * [Steps](#steps)
    * [Data](#data)
* [Example Get Clients List](#example-get-clients-list)
* [Test](#test)
* [Help](#help)
* [License](#license)
* [Contributing](#contributing)

## Getting Started

On the current version the python module can be used by placing - 
**creator_python_client.py** file on the project directory. Then, import the 
module in the code:
    
```python
import creator_python_client
```

## Jump Start

In order to be able to utilize this library you will have to sign up for a 
creator account. You can do so going through the 
[Creator Developer Console](http://console.creatordev.io)

After signing up, you will need to create an access key and secret pair from 
the API keys section of the console. These will gain you access to the Creator 
REST API while using this library.

You can then create an instance of the library as follows: 

```python
import creator_python_client

CREATOR_ACCESS_KEY = '<your_access_key>'
CREATOR_ACCESS_SECRET = '<your_access_secret>'

creator_python_client.request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET)
```

Please note that you can also set the following **environment variables** for 
the library to use.

* CREATOR_ACCESS_KEY
* CREATOR_ACCESS_SECRET

and then 

```python
import creator_python_client
import os

CREATOR_ACCESS_KEY = os.environ['CREATOR_ACCESS_KEY']
CREATOR_ACCESS_SECRET = os.environ['CREATOR_ACCESS_SECRET']

creator_python_client.request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET)

```

Now you should have a working instance of the library that you can use to access your resources RESTfully.

As you may already know, creator rest api is using what is called the HATEOAS 
REST application structure which means that you need to follow links in order 
to reach to certain resources. This library will do that for you. 
Please keep reading!

### The Request Method

The request method provide a very flexible way of accessing any resource you would like to interact with.

The structure for this method is as follows:

```python
creator_python_client.request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET, method="get", steps=steps, data=data)
```

#### Supported HTTP Methods

This module supports the following HTTP methods/verbs:

1. GET
2. PUT
3. POST
4. DEL

The method can be selected in the method option:

```python
method="<http_method>"
```

#### Steps

In the steps argument, the user provides path to the resource on the device
Device Server. See two usage examples bellow:

```python

steps = ["clients"]

request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET, method="get", steps=steps)
```

To access AwaLWM2M objects and its instances within the Device Server, you 
can provide the steps as shown in the following example:

```python

steps = [("clients","ci40-press"), ("ObjectTypeID", "3201"), ("InstanceID","0")]

request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET, method="get", steps=steps)
```

#### Data

The argument data allows receives the Payload for the PUT and POST method. 
This functionality is useful if the user wants to update a resource on the 
Device Server. For example:

```python

creator_python_client.request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET, method="put", steps=steps, data={"DigitalOutputState": False})

```

Thus, the Digital Output State is updated to False.


## Example Get Clients List

The following example shows how to get a list of AwaLWM2M clients within the
Device Server:

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import creator_python_client

CREATOR_ACCESS_KEY = '<your_access_key>'
CREATOR_ACCESS_SECRET = '<your_access_secret>'

steps = ["clients"]

CLIENTS = creator_python_client.request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET, method="get", steps=steps)

print CLIENTS
```

## Test

You can run the command below to initiate the tests. 
Please note that the aforementioned ENV variables need to be set for the test 
script to work properly.

```bash
$ python test.py
```

## Help

If you have any problems installing or utilising this project, please look into 
our [Creator Forum](https://forum.creatordev.io). 

Otherwise, If you have come across a nasty bug or would like to suggest new 
features to be added then please go ahead and open an issue or a pull request 
against this repo.

## License

Please see the [license](LICENSE) file for a detailed explanation.

## Contributing

Any Bug fixes and/or feature enhancements are welcome. Please see the
[contributing](CONTRIBUTING.md) file for a detailed explanation.

The Python code follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) 
code styling, verified by [Flake8](http://flake8.pycqa.org/en/latest/). 

---
