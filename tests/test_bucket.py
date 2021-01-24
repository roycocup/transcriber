import unittest 
from libs import bucket

class TestBucket(unittest.TestCase):

    def setUp(self):
        self.sut = bucket.Bucket()
        self.test_bucket_name = "test-transcriber-rodderscode-co-uk"
        self.test_bucket_created = False
    
    def tearDown(self):
        if self.test_bucket_created:
            self._delete_test_bucket()
        
    def _create_test_bucket(self):
        self.sut.create_bucket(self.test_bucket_name)
        self.test_bucket_created = True

    def _delete_test_bucket(self):
        self.sut.delete_bucket(self.test_bucket_name)
        self.test_bucket_created = False

    def test_can_get_list(self):
        self._create_test_bucket()
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
        self._create_test_bucket()
        results = self.sut.get_all_buckets()
        
        names = []
        for bucket in results:
            names.append(bucket.name)
            
        if self.test_bucket_name not in names:
            self.fail('Test bucket name not in list')

        
            