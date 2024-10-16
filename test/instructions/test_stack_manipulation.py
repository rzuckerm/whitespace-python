import unittest

from whitespace.instructions.stack_manipulation import Copy, Discard, Dup, Push, Slide, Swap
from whitespace.vm import VM


class PushTestCase(unittest.TestCase):
    def test_it_pushes_a_number_onto_the_value_stack(self):
        vm = VM()

        Push(1).execute(vm)

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)


class DupTestCase(unittest.TestCase):
    def test_it_duplicates_the_top_item_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)

        Dup().execute(vm)

        self.assertEqual(len(vm.vstack), 2)
        self.assertEqual(vm.vstack.pop(), 1)
        self.assertEqual(vm.vstack.pop(), 1)


class SwapTestCase(unittest.TestCase):
    def test_it_swaps_the_two_top_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(2)
        vm.vstack.push(3)

        Swap().execute(vm)

        self.assertEqual(len(vm.vstack), 3)
        self.assertEqual(vm.vstack.pop(), 2)
        self.assertEqual(vm.vstack.pop(), 3)
        self.assertEqual(vm.vstack.pop(), 1)


class DiscardTestCase(unittest.TestCase):
    def test_it_discards_the_top_item_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)

        Discard().execute(vm)

        self.assertEqual(len(vm.vstack), 0)


class CopyTestCase(unittest.TestCase):
    def test_it_copies_the_requested_item_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(2)
        vm.vstack.push(3)

        Copy(1).execute(vm)

        self.assertEqual(len(vm.vstack), 4)
        self.assertEqual(vm.vstack.pop(), 2)


class SlideTestCase(unittest.TestCase):
    def test_it_discards_the_requested_items_off_value_stack_and_pushes_top_onto_value_stack(
        self,
    ):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(2)
        vm.vstack.push(3)
        vm.vstack.push(4)

        Slide(2).execute(vm)

        self.assertEqual(len(vm.vstack), 2)
        self.assertEqual(vm.vstack.pop(), 4)
        self.assertEqual(vm.vstack.pop(), 1)
