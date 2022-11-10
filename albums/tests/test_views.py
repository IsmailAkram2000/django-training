import pytest
from django.test import TestCase
from users.models import User
from artists.models import Artist

class AllAlbumsTest(TestCase):
    def setUp(self):
        self.endpoint = '/albums/'

    # Test all albums success
    def test_AllAlubums_found(self):
        response = self.client.get(f'{self.endpoint}')
        self.assertEqual(response.status_code, 200)

    # Test all albums fail
    def test_AllArtist_not_found(self):
        response = self.client.get(f'{self.endpoint}/')
        self.assertEqual(response.status_code, 404)

    # Test Ceate Album

    def test_CreateAlbum_unauthorized(self):
        album = {
            "name": "New Album1",
            "release_date": "2022-01-01",
            "cost": "49.99" 
        }
        response = self.client.post(f'{self.endpoint}', album)
        self.assertEqual(response.status_code, 401)


# create album success
@pytest.mark.django_db
def test_createAlbum_success(auth_client):
    user = User.objects.create_user(username = 'admin', password = 'a#12345678#a')
    Artist.objects.create(user = user, Stage_name = 'Nancy Ajram')
    client = auth_client(user)

    album = {
        "name": "New Album1",
        "release_date": "2022-01-01",
        "cost": "49.99" 
    }
    response = client.post(f'/albums/', album)
    assert response.status_code == 201

# create album with user that isn't artist
@pytest.mark.django_db
def test_createAlbum_success(auth_client):
    user = User.objects.create_user(username = 'admin', password = 'a#12345678#a')
    client = auth_client(user)

    album = {
        "name": "New Album1",
        "release_date": "2022-01-01",
        "cost": "49.99" 
    }
    response = client.post(f'/albums/', album)
    assert response.status_code == 403