from albums.serializers import AlbumSerializer
from django.test import TestCase

class AllAlbumsTest(TestCase):
    # test serialize album 
    def test_serialize_album_success(self):
        album = {
            "name": "New Album1",
            "release_date": "2022-01-01",
            "cost": "49.99" 
        }

        serializer = AlbumSerializer(data=album)
        assert serializer.is_valid() == True
        assert serializer.data == {
            "name": "New Album1",
            "release_date": "2022-01-01T00:00:00Z",
            "cost": "49.99"
        }


    # test serialize album fail
    def test_serialize_album_fail(self):
        # empty data
        serializer = AlbumSerializer(data={})
        assert serializer.is_valid() == False
        
        # cost not number
        album = {
            "name": "New Album1",
            "release_date": "2022-01-01",
            "cost": "Wrong data"
        }

        serializer = AlbumSerializer(data=album)
        assert serializer.is_valid() == False