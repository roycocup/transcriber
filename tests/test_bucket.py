import unittest 
from tests.base import Base
from libs import bucket

class TestBucket(Base):

    def setUp(self):
        super().setUp()
        self.sut = bucket.Bucket()

    def tearDown(self):
        return super().tearDown()
        
        
    def test_can_get_list(self):
        self._create_bucket()
        actual = self.sut.get_all_buckets()
        self.assertIsInstance(actual, list)
    
    def test_can_create_and_delete_bucket(self):
        bucket_name = 'test-transcriber-2-rodderscode-co-uk'
        res1 = self.sut.create_bucket(bucket_name)
        res2 = self.sut.delete_bucket(bucket_name)
    
        import google.cloud.storage.bucket as b

        self.assertIsInstance(res1, b.Bucket)
        self.assertEqual(res2, None)
        
    def test_list_has_bucket_objects(self):
        self._create_bucket()
        results = self.sut.get_all_buckets()
        
        names = []
        for bucket in results:
            names.append(bucket.name)
            
        if self.test_bucket_name not in names:
            self.fail('Test bucket name not in list')

        
            