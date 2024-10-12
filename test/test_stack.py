import unittest

from whitespace.error import StackEmptyError, StackIndexError
from whitespace.stack import Stack


class StackTestCase(unittest.TestCase):
    def test_it_works_like_a_stack(self):
        stack = Stack()

        with self.assertRaises(StackEmptyError):
            stack.pop()

        with self.assertRaises(StackEmptyError):
            stack.top()

        with self.assertRaises(StackIndexError):
            stack[-1]

        with self.assertRaises(StackIndexError):
            stack[0]

        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack[0], 1)
        self.assertEqual(stack[1], 2)
        self.assertEqual(stack[2], 3)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.top(), 2)

        stack.pop()

        self.assertEqual(len(stack), 1)

        stack.pop()

        self.assertTrue(stack.empty())


class NamedStackTestCase(unittest.TestCase):
    def test_name_is_included_in_error_message(self):
        stack = Stack("a stack")

        with self.assertRaisesRegex(StackEmptyError, "a stack"):
            stack.pop()

        with self.assertRaisesRegex(StackEmptyError, "a stack"):
            stack.top()

        with self.assertRaisesRegex(StackIndexError, "a stack"):
            stack[42]
