import connexion
import six

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.photo import Photo  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def batchget_photo(user_id, photo_ids):  # noqa: E501
    """batchget_photo

    Gets a list of photos # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param photo_ids: a collection of photo IDs
    :type photo_ids: List[str]

    :rtype: List[Photo]
    """
    return 'do some magic!'


def create_photo(user_id, photo=None):  # noqa: E501
    """create_photo

    Creates a photo # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param photo: The photo to add
    :type photo: dict | bytes

    :rtype: Photo
    """
    if connexion.request.is_json:
        photo = Photo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user(user=None):  # noqa: E501
    """create_user

    Creates a new user # noqa: E501

    :param user: The user to create
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_photo(user_id, photo_id):  # noqa: E501
    """delete_photo

    Deletes a photo # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param photo_id: ID of photo
    :type photo_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_photo(user_id, photo_id):  # noqa: E501
    """get_photo

    Gets a photo # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param photo_id: ID of photo
    :type photo_id: str

    :rtype: Photo
    """
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """get_user

    Gets a user # noqa: E501

    :param user_id: ID of user
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def list_photos(user_id, order_by=None, page_token=None):  # noqa: E501
    """list_photos

    Lists all photos # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param order_by: Ordering for the results
    :type order_by: str
    :param page_token: Token for the next page
    :type page_token: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def update_user(user_id, user=None):  # noqa: E501
    """update_user

    Updates a user # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param user: The user to update
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
