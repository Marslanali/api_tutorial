# openapi-client
An OpenAPI specification sample for [Build, Deploy, and Manage Networked APIs: An Overview](https://goo.gl/VardtG) document.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | ID of user
photo_ids = ['photo_ids_example'] # list[str] | a collection of photo IDs

    try:
        api_response = api_instance.batchget_photo(user_id, photo_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->batchget_photo: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**batchget_photo**](docs/DefaultApi.md#batchget_photo) | **GET** /users/{user_id}/photos:batchGet | 
*DefaultApi* | [**create_photo**](docs/DefaultApi.md#create_photo) | **POST** /users/{user_id}/photos/ | 
*DefaultApi* | [**create_user**](docs/DefaultApi.md#create_user) | **POST** /users | 
*DefaultApi* | [**delete_photo**](docs/DefaultApi.md#delete_photo) | **DELETE** /users/{user_id}/photos/{photo_id} | 
*DefaultApi* | [**get_photo**](docs/DefaultApi.md#get_photo) | **GET** /users/{user_id}/photos/{photo_id} | 
*DefaultApi* | [**get_user**](docs/DefaultApi.md#get_user) | **GET** /users/{user_id} | 
*DefaultApi* | [**list_photos**](docs/DefaultApi.md#list_photos) | **GET** /users/{user_id}/photos/ | 
*DefaultApi* | [**update_user**](docs/DefaultApi.md#update_user) | **PATCH** /users/{user_id} | 


## Documentation For Models

 - [ErrorMessage](docs/ErrorMessage.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Photo](docs/Photo.md)
 - [User](docs/User.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author



