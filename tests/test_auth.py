import http.client
import json


def test_registration(client):
    response = client.post(
        "api/users/v1/auth/register/",
        data=json.dumps(
            {
                "username": "tonyparker",
                "email": "tony@gmail.com",
                "password": "tony1234",
            }
        ),
        content_type="application/json",
    )
    data = response.json

    assert http.client.CREATED == response.status_code
    assert "Successfully registered" == data["message"]
    assert "success" == data["status"]
    assert data["auth_token"] is not None
    assert response.content_type == "application/json"
