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

        new_demo = DemoClass('')
        self.assertEqual(new_demo.return_data(), '{name: , data: hello}')

        weird_demo = DemoClass(7)
        self.assertEqual(weird_demo.return_data(), '{name: 7, data: hello}')

    def test_vector_sum(self):
        """Test vector_sum function"""
        self.assertEqual(self.demo.vector_sum((2, 2, 2), (2, 2, 2)), (4, 4, 4))
        self.assertEqual(self.demo.vector_sum((2, 2, 2), (0, 0, 0)), (2, 2, 2))
        self.assertEqual(self.demo.vector_sum((1, 2, 3), (4, 5, 6)), (5, 7, 9))

        self.assertRaises(TypeError, self.demo.vector_sum, ("hi", "this", "is"), ("a", "test", "case"))

    def test_scale_vector(self):
        """Test scale_vector function"""
        self.assertEqual(self.demo.scale_vector(2, (2, 2, 2)), (4, 4, 4))
        self.assertEqual(self.demo.scale_vector(0, (2, 2, 2)), (0, 0, 0))
        self.assertEqual(self.demo.scale_vector(1, (2, 2, 2)), (2, 2, 2))
        self.assertEqual(self.demo.scale_vector(2, (1, 2, 3)), (2, 4, 6))

        self.assertRaises(TypeError, self.demo.scale_vector, ("hi", "this", "is"), ("a", "test", "case"))

    def test_sum_and_callback(self):
        """Test sum_and_callback function"""
        self.demo.sum_and_callback((2, 2, 2), (2, 2, 2), self.mock)
        self.mock.assert_called_with((4, 4, 4))
