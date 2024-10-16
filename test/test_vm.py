import unittest

from whitespace.error import LabelMissingError, OutOfBoundsError
from whitespace.instructions import (
    Push,
    Dup,
    Mul,
    End,
    Label,
    Add,
    Putn,
    Putc,
    Sub,
    Zjmp,
    Ujmp,
    Discard,
)
from whitespace.peripherals import TestScreen
from whitespace.vm import VM


class VMTestCase(unittest.TestCase):
    def test_it_executes_each_instruction_one_by_one_until_an_end_instruction_is_reached(
        self,
    ):
        vm = VM()
        vm.instructions = [Push(3), Dup(), Mul(), End(), Dup()]

        vm.run()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 9)

    def test_it_raises_an_error_when_no_end_instruction_is_reached(self):
        vm = VM()
        vm.instructions = [Push(3), Dup(), Mul()]

        with self.assertRaisesRegex(OutOfBoundsError, "program counter: 3"):
            vm.run()

    def test_find_label(self):
        vm = VM()
        vm.instructions = [Push(1), Label("a"), Push(2), Label("b"), Add()]

        self.assertEqual(vm.find_label("a"), 1)
        self.assertEqual(vm.find_label("b"), 3)

        with self.assertRaisesRegex(LabelMissingError, "c"):
            vm.find_label("c")


class CountTestCase(unittest.TestCase):
    def test_it_counts_from_1_to_10(self):
        screen = TestScreen()

        vm = VM()
        vm.screen = screen
        vm.instructions = [
            Push(1),  # Put a 1 on the stack
            Label(" "),  # Set a Label at this point
            Dup(),  # Duplicate the top stack item
            Putn(),  # Output the current value
            Push(10),  # Put 10 (newline) on the stack...
            Putc(),  # ...and output the newline
            Push(1),  # Put a 1 on the stack
            Add(),  # Increment our current value
            Dup(),  # Duplicate the value to test it
            Push(11),  # Push 11 onto the stack
            Sub(),  # Subtraction
            Zjmp("\t"),  # If we have a 0, jump to the end
            Ujmp(" "),  # Jump to the start
            Label("\t"),  # Set the end label
            Discard(),  # Discard our accumulator, to be tidy
            End(),  # Finish
        ]

        vm.run()

        self.assertEqual(screen.contents, "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")

        screen.turn_off()
