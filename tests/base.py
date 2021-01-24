import os
import unittest
from libs import gfiles
from google.cloud import storage

class Base(unittest.TestCase):
    
    
    test_bucket_name = 'test-bucket-rodderscode-co-uk'
    test_filename = 'test-file.txt'
    test_bucket_created = False
    client = storage.Client()
        

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
            self.test_bucket_created = True
        except:
            pass    

    def _delete_bucket(self):
        if self.test_bucket_created:
            self.client.bucket(self.test_bucket_name).delete(force=True)