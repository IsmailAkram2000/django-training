from django.test import TestCase
from artists.models import Artist

class AllArtistTest(TestCase):
    def setUp(self):
        Artist.objects.create(Stage_name='Nancy Ajram', Social_link="https://www.facebook.com/Nancy_Ajram")
        self.endpoint = '/artists/'

    # Test get all artist
    def test_AllArtist_found(self):
        response = self.client.get(f'{self.endpoint}')
        self.assertEqual(response.status_code, 200)

    def test_AllArtist_not_found(self):
        response = self.client.get(f'{self.endpoint}/')
        self.assertEqual(response.status_code, 404)

    # Test Create Artist Succsess
    def test_createArtist(self):
        artist = {
            "Stage_name": "Amr Diab",
            "Social_link": "https://www.facebook.com/AmrDiab",
        }
        response = self.client.post(f'{self.endpoint}create/', artist)
        self.assertEqual(response.status_code, 201)

    # Test Create Artist Fail
    def test_createArtist_with_same_name(self):
        artist = {
            "Stage_name": "Amr Diab",
            "Social_link": "https://www.facebook.com/AmrDiab",
        }
        response = self.client.post(f'{self.endpoint}create/', artist)
        self.assertEqual(response.status_code, 201)

        response = self.client.post(f'{self.endpoint}create/', artist)
        self.assertEqual(response.status_code, 400)