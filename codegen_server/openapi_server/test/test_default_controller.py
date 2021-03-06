# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.photo import Photo  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_batchget_photo(self):
        """Test case for batchget_photo

        
        """
        query_string = [('photo_ids', 'photo_ids_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}/photos:batchGet'.format(user_id='user_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_photo(self):
        """Test case for create_photo

        
        """
        photo = {
  "data" : "data",
  "name" : "name",
  "created_at" : 0,
  "display_name" : "display_name"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}/photos'.format(user_id='user_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(photo),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        
        """
        user = {
  "name" : "name",
  "display_name" : "display_name",
  "email" : "email"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users',
            method='POST',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_photo(self):
        """Test case for delete_photo

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}/photos/{photo_id}'.format(user_id='user_id_example', photo_id='photo_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_photo(self):
        """Test case for get_photo

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}/photos/{photo_id}'.format(user_id='user_id_example', photo_id='photo_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_photos(self):
        """Test case for list_photos

        
        """
        query_string = [('order_by', 'order_by_example'),
                        ('page_token', 'page_token_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}/photos'.format(user_id='user_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        
        """
        user = {
  "name" : "name",
  "display_name" : "display_name",
  "email" : "email"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id='user_id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
