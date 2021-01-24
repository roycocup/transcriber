import os
import unittest
from libs import gfiles
from google.cloud import storage

class TestGFile(unittest.TestCase):

    def setUp(self):
        self.test_bucket_name = 'test-bucket-rodderscode-co-uk'
        self.test_filename = 'test-file.txt'
        self.sut = gfiles.GFiles(self.test_bucket_name)
        self.client = storage.Client()
        self._create_bucket()
        return super().setUp()

    def tearDown(self):
        self._delete_bucket()
        self._delete_test_file()
        return super().tearDown()

    def _create_test_file(self, filename=None):
        if not filename: 
            filename = self.test_filename
        
        with open(filename, 'w') as f:
            text_str = "Lorem in exercitation nisi veniam quis elit cupidatat consequat commodo."
            f.write(text_str)
    
    def _delete_test_file(self, filename=None):
        if not filename: 
            filename = self.test_filename
        if os.path.isfile(filename):
            os.remove(filename)
        

    def _create_bucket(self):
        try:
            self.client.create_bucket(self.test_bucket_name)
        except:
            pass    

    def _delete_bucket(self):
        self.client.bucket(self.test_bucket_name).delete(force=True)

    def test_can_instantiate(self):
        self.assertIsInstance(self.sut, gfiles.GFiles)
        
    def test_upload_returns_a_blob(self):
        self._create_test_file()
        blob = self.sut.upload(self.test_filename)
        
        import google.cloud.storage.bucket as b
        self.assertIsInstance(blob, b.Blob)

    def test_can_upload_file_to_bucket(self):
        self._create_test_file()
        self.sut.upload(self.test_filename)
        bucket = self.client.bucket(self.test_bucket_name)
        blob = bucket.get_blob(self.test_filename)

        self.assertIsNotNone(blob)
        self.assertEqual(blob.name, self.test_filename)

    
    def test_can_delete_unexisting_file_returns_None(self):    
        bucket = self.client.bucket(self.test_bucket_name)
        self.sut.delete(self.test_filename)
        blob = bucket.get_blob(self.test_filename)
        self.assertIsNone(blob)

    def test_can_delete_file(self):
        self._create_test_file()
        self.sut.upload(self.test_filename)
        self._create_test_file('another.test.file')
        self.sut.upload('another.test.file')
        
        # Was the first file uploaded correctly? 
        bucket = self.client.bucket(self.test_bucket_name)
        blob = bucket.get_blob(self.test_filename)
        self.assertEqual(blob.name, self.test_filename)
        
        # call delete
        self.sut.delete(self.test_filename)

        # Should not be there
        blob = bucket.get_blob(self.test_filename)
        self.assertIsNotNone(blob)

        # deletes ONLY that one
        blob2 = bucket.get_blob('another.test.file')
        self.assertEquals(blob2.name,'another.test.file')

        self._delete_test_file('another.test.file')

        

        
