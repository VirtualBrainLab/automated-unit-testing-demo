from unittest import TestCase
from unittest.mock import Mock

from demo.demo_class import DemoClass


class TestDemoClass(TestCase):
    """Test demo class functions"""

    def setUp(self):
        """Setup class and mock callback function"""
        self.demo = DemoClass('Demo')
        self.mock = Mock()

    def test_return_data(self):
        """Test return_data function"""
        self.assertEqual(self.demo.return_data(), '{name: Demo, data: hello}')

    def test_vector_sum(self):
        """Test vector_sum function"""
        self.assertEqual(self.demo.vector_sum((2, 2, 2), (2, 2, 2)), (4, 4, 4))

    def test_scale_vector(self):
        """Test scale_vector function"""
        self.assertEqual(self.demo.scale_vector(2, (2, 2, 2)), (4, 4, 4))

    def test_sum_and_callback(self):
        """Test sum_and_callback function"""
        self.demo.sum_and_callback((2, 2, 2), (2, 2, 2), self.mock)
        self.mock.assert_called_with((4, 4, 4))
