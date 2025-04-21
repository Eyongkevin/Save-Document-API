import http.client
import json

from faker import Faker

fake = Faker()


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


def test_registration_already_registered_user(client, user_fixture):
    user: dict[str, str] = user_fixture[0]

    response = client.post(
        "api/users/v1/auth/register/",
        data=json.dumps(
            dict(
                username=user["username"],
                email=user["email"],
                password=user["password"],
            )
        ),
        content_type="application/json",
    )
    data = response.json

    assert http.client.UNAUTHORIZED == response.status_code


def test_registered_user_login(client, user_fixture):

    username = user_fixture[0]["username"]
    password = user_fixture[0]["password"]

    response = client.post(
        "api/users/v1/auth/login/",
        data=json.dumps(
            dict(
                username=username,
                password=password,
            )
        ),
        content_type="application/json",
    )
    data = response.json
    assert http.client.OK == response.status_code
    assert "Successfully logged in" == data["message"]
    assert "success" == data["status"]
    assert data["auth_token"] is not None
    assert response.content_type == "application/json"


def test_non_registered_user_login(client):
    response = client.post(
        "api/users/v1/auth/login/",
        data=json.dumps(
            dict(
                username="kenzjohn",
                password="kenzjohn11234",
            )
        ),
        content_type="application/json",
    )
    data = response.json
    assert http.client.UNAUTHORIZED == response.status_code
    assert "username or password incorrect. Try again" == data["message"]
    assert "fail" == data["status"]
    assert response.content_type == "application/json"


def test_registered_user_wrong_password_login(client, user_fixture):
    username = user_fixture[0]["username"]
    password = fake.password()

    response = client.post(
        "api/users/v1/auth/login/",
        data=json.dumps(
            dict(
                username=username,
                password=password,
            )
        ),
        content_type="application/json",
    )
    data = response.json
    assert http.client.UNAUTHORIZED == response.status_code
    assert "username or password incorrect. Try again" == data["message"]
    assert "fail" == data["status"]
    assert response.content_type == "application/json"
