# Mocking is a powerful technique to isolate the code under test from the rest of the system 
# and replace external dependencies with predictable results.


import pytest
import requests
import source.service as service
import unittest.mock as mock

# This mock will replace the real get_user_from_db function with a mock function that returns a fake user.
@mock.patch('source.service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
    # Aca seteamos el valor que queremos que retorne el mock
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"
    # mock_get_user_from_db.assert_called_once_with(1)
    
    
@mock.patch('requests.get')
def test_get_users(mock_get):
    # Initialize a mock response object
    mock_response = mock.Mock()
    # We set it all up to return a 200 status code and a JSON object with the user's data.
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    # We then set the mock to return the mock response when requests.get is called.
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}
    
@mock.patch('requests.get')
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
    