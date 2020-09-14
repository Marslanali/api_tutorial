# openapi-generator-tutorial

openapi-generator-tutorial

## Dependencies

- npm
- nodejs
- Python3
- openapi-generator-cli 
- build-essentials i.e. GCC, GNU Make

## Install npm and nodejs from source

If you have deprecated versions of `npm` and `nodejs` pull `node-v12.18.3` source code from `https://nodejs.org/en/download/` and install it from source using:

```
cd ~/node-v12.18.3
./configure
make -j 4    ## where j is the number of cores 
sudo make install
```
Now check `npm` and `nodejs` version i.e. `$ npm -v` 6.14.6 `$ node -v` v12.18.3

## Install Openapi-generator-cli

Install `openapi-generator-cli` using npm i.e. `$ npm install @openapitools/openapi-generator-cli -g`. And finally, we can generate a python client from a valid `petstore.yaml` using:

```
openapi-generator generate -i petstore.yaml -g python -o /tmp/test/
```

```
ubuntu@ubuntu-16:/tmp/test$ ls

docs         openapi_client  requirements.txt  setup.py  test-requirements.txt
git_push.sh  README.md       setup.cfg         test      tox.ini

```

## Generate Python flask server using OpenApi Generator

Prepare the server end code:

```
openapi-generator generate -i openapi.yaml -g python-flask -o codegen_server/
cd codegen_server
pip3 install -r requirements.txt

```

Now start the openapi server using `python3 -m openapi_server`. Open your brower and server will show up at `http://localhost:8080/ui/` 

## Generate Python client using OpenApi Generator

Prepare the client end code:

```
openapi-generator generate -i openapi.yaml -g python -o codegen_client/
cd codegen_client
python setup.py install --user

```

Now as an example of sending a POST request to server running at `http://localhost:8080/ui/`.

```
vim test-POST-user.py
```
Copy the following Python code: 
 
```
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
user = openapi_client.User(display_name ="display_name", email="openapi@abc.com") # User | The user to create (optional)

try:
    api_response = api_instance.create_user(user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_user: %s\n" % e)

```

Now run test-POST-user.py using `$ python3 test-POST-user.py` in codgen_client directory.

























