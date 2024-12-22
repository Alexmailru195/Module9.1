import unittest
from Stack import Stack  # Импорт класса Stack из файла Stack.py

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(stack_size=3)

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertTrue(self.stack.is_full())
        self.stack.pop()
        self.assertFalse(self.stack.is_full())

    def test_clear_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear_stack()
        self.assertTrue(self.stack.is_empty())

    def test_get_data(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_data(0), 3)
        self.assertEqual(self.stack.get_data(1), 2)
        self.assertEqual(self.stack.get_data(2), 1)
        self.assertEqual(self.stack.get_data(3), "Out of range")

    def test_counter_int(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push("string")
        self.assertEqual(self.stack.counter_int(), 2)

if __name__ == "__main__":
    unittest.main()