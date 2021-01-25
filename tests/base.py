import os
import unittest
from libs import gfiles
from google.cloud import storage

class Base(unittest.TestCase):
    
    
    test_bucket_name = 'test-bucket-rodderscode-co-uk'
    test_filename = 'test-file.txt'
    test_bucket_created = False
        

    