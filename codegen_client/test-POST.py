
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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | ID of user
    photo = openapi_client.Photo() # Photo | The photo to add (optional)

    try:
        api_response = api_instance.create_photo(user_id, photo=photo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_photo: %s\n" % e)
