from libs.ffmpeg import Ffmpeg
import unittest
from unittest import mock

class TestFmpeg(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.sut = Ffmpeg()
    
    def test_can_instantiate_with(self):
        self.assertIsInstance(self.sut, Ffmpeg)

