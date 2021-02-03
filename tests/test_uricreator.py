import unittest
from libs.uri_creator import UriCreator

class TestUriCreator(unittest.TestCase):

    def test_can_create_uri_for_file_in_bucket(self):
        file_name, bucket_name = "test.mp3", "rodrigo-test-bucket"
        actual = UriCreator.get_uri(file_name=file_name, bucket_name=bucket_name)
        expected = "gs://rodrigo-test-bucket/test.mp3"
        self.assertEqual(actual, expected)