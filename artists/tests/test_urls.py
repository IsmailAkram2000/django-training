from django.test import SimpleTestCase
from django.urls import reverse, resolve
from artists.views import allArtists, createArtist


class TestUrls(SimpleTestCase):
    
    def test_allArtist_is_resolved(self):
        url = reverse('Get All Artists')
        self.assertEquals(resolve(url).func.view_class, allArtists)

    def test_createArtist_is_resolved(self):
        url = reverse('Create Artist')
        self.assertEquals(resolve(url).func.view_class, createArtist)