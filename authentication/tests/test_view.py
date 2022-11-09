import pytest

endpoint = '/authentication'

# Test Register

@pytest.mark.django_db
def test_register_success(client):
    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password1": "$#12345678#$a",
        "password2": "$#12345678#$a",
        "bio": '',
    }

    response = client.post(f'{endpoint}/register', user)
    assert response.status_code == 201


@pytest.mark.django_db
def test_register_bad_request(client):

    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password1": "$#12345678#$a",
        "password2": "$#12345678#$a",
        "bio": '',
    }

    # empty data
    response = client.post(f'{endpoint}/register', {})
    assert response.status_code == 400

    # already registered email
    response = client.post(f'{endpoint}/register', user)
    response = client.post(f'{endpoint}/register', user)
    assert response.status_code == 400

    # check validate password
    user["password1"] = user["password2"] = "1"
    response = client.post(f'{endpoint}/register', user)
    assert response.status_code == 400

    # invalid email
    user["password1"] = user["password2"] = "admin1234"
    user['email'] = "admin"
    response = client.post(f'{endpoint}/register', user)
    assert response.status_code == 400


# Test Login
@pytest.mark.django_db
def test_login_success(client):
    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password1": "$#12345678#$a",
        "password2": "$#12345678#$a",
        "bio": '',
    }

    # register user
    response = client.post(f'{endpoint}/register', user)
    assert response.status_code == 201

    # login
    response = client.post(f'{endpoint}/login', {'username': "admin", 'password': "$#12345678#$a",})

    assert response.status_code == 200
    
    assert 'token' in response.data

@pytest.mark.django_db
def test_login_fail(client):
    # login
    response = client.post(f'{endpoint}/login', {'username': "adminfail", 'password': "adminfail", })
    assert response.status_code == 400


# Test Logout
@pytest.mark.django_db
def test_logout_success(auth_client):
    client = auth_client()
    response = client.post(f'{endpoint}/logout')
    assert response.status_code == 204

@pytest.mark.django_db
def test_logout_fail(client):
    response = client.post(f'{endpoint}/logout')
    assert response.status_code == 401
