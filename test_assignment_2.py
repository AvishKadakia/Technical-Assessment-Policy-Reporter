import unittest
from assignment_2 import FiniteAutomaton, ModThreeAutomaton


class TestModThreeAutomaton(unittest.TestCase):
    """
    Unit tests for the ModThreeAutomaton class.
    """

    def setUp(self):
        """
        Initialize the ModThreeAutomaton instance before each test.
        """
        self.mod_three_automaton = ModThreeAutomaton()

    def test_compute_remainder(self):
        """
        Test the compute_remainder method with various binary strings.
        """
        test_cases = [
            ('1101', 1),  # 13 % 3 = 1
            ('1110', 2),  # 14 % 3 = 2
            ('1111', 0),  # 15 % 3 = 0
            ('110', 0),   # 6 % 3 = 0
            ('1010', 1),  # 10 % 3 = 1
            ('0', 0),     # 0 % 3 = 0
            ('1', 1),     # 1 % 3 = 1
            ('', 0),      # Empty string, default to 0
            ('1011', 2),  # 11 % 3 = 2
            ('1001', 0),  # 9 % 3 = 0 (Corrected from 1 to 0)
            ('1000', 2),  # 8 % 3 = 2 (Corrected from 0 to 2)
        ]
        for binary_str, expected_remainder in test_cases:
            with self.subTest(binary_str=binary_str):
                remainder = self.mod_three_automaton.compute_remainder(binary_str)
                self.assertEqual(
                    remainder,
                    expected_remainder,
                    msg=f"Failed for input '{binary_str}'"
                )

    def test_invalid_input(self):
        """
        Test that invalid inputs raise a ValueError.
        """
        invalid_inputs = ['2', 'abc', '1012', '10a1', '@#$']
        for binary_str in invalid_inputs:
            with self.subTest(binary_str=binary_str):
                with self.assertRaises(ValueError):
                    self.mod_three_automaton.compute_remainder(binary_str)



class TestFiniteAutomaton(unittest.TestCase):
    """
    Unit tests for the generic FiniteAutomaton class using different FSMs.
    """

    def setUp(self):
        """
        Set up different automata for testing.
        """
        # ModFiveAutomaton setup
        self.mod_five_automaton = self.create_mod_five_automaton()
        self.mod_five_state_to_remainder = {
            'S0': 0,
            'S1': 1,
            'S2': 2,
            'S3': 3,
            'S4': 4,
        }

    def create_mod_five_automaton(self):
        """
        Creates a ModFiveAutomaton using the generic FiniteAutomaton class.
        """
        states = {'S0', 'S1', 'S2', 'S3', 'S4'}
        input_alphabet = {'0', '1'}
        initial_state = 'S0'
        final_states = states  # All states are considered final

        def transition_function(state, input_symbol):
            """
            Transition function for Mod 5 FSM.
            """
            transition_table = {
                'S0': {'0': 'S0', '1': 'S1'},
                'S1': {'0': 'S2', '1': 'S3'},
                'S2': {'0': 'S4', '1': 'S0'},
                'S3': {'0': 'S1', '1': 'S2'},
                'S4': {'0': 'S3', '1': 'S4'},
            }
            return transition_table[state][input_symbol]

        return FiniteAutomaton(
            states=states,
            input_alphabet=input_alphabet,
            transition_function=transition_function,
            initial_state=initial_state,
            final_states=final_states,
        )

    def compute_mod_five_remainder(self, binary_string):
        """
        Helper method to compute the remainder when divided by 5.
        """
        final_state = self.mod_five_automaton.process_input(binary_string)
        return self.mod_five_state_to_remainder[final_state]

    def test_mod_five_automaton(self):
        """
        Test the ModFiveAutomaton with various binary strings.
        """
        test_cases = [
            ('0', 0),
            ('1', 1),
            ('10', 2),
            ('11', 3),
            ('100', 4),
            ('101', 0),
            ('110', 1),
            ('111', 2),
            ('1000', 3),
            ('1001', 4),
            ('1010', 0),
            ('1011', 1),
            ('1100', 2),
            ('', 0),  # Empty string should result in initial state (S0)
        ]
        for binary_str, expected_remainder in test_cases:
            with self.subTest(binary_str=binary_str):
                remainder = self.compute_mod_five_remainder(binary_str)
                self.assertEqual(
                    remainder,
                    expected_remainder,
                    msg=f"Failed for input '{binary_str}'"
                )

    def test_invalid_input_mod_five(self):
        """
        Test that invalid inputs raise a ValueError in ModFiveAutomaton.
        """
        invalid_inputs = ['2', 'abc', '10b1', '1@1']
        for binary_str in invalid_inputs:
            with self.subTest(binary_str=binary_str):
                with self.assertRaises(ValueError):
                    self.compute_mod_five_remainder(binary_str)

    def test_custom_automaton_accepts_strings_ending_with_one(self):
        """
        Test a custom automaton that accepts binary strings ending with '1'.
        """
        states = {'EndsWith0', 'EndsWith1'}
        input_alphabet = {'0', '1'}
        initial_state = 'EndsWith0'  # Assume empty string ends with '0'
        final_states = {'EndsWith1'}  # Accepting state is 'EndsWith1' (strings ending with '1')

        def transition_function(state, input_symbol):
            """
            Transition function that updates the state based on the last input symbol.
            """
            if input_symbol == '0':
                return 'EndsWith0'
            else:  # input_symbol == '1'
                return 'EndsWith1'

        automaton = FiniteAutomaton(
            states=states,
            input_alphabet=input_alphabet,
            transition_function=transition_function,
            initial_state=initial_state,
            final_states=final_states,
        )

        accepting_inputs = ['1', '01', '001', '111', '101']
        rejecting_inputs = ['0', '00', '10', '1100', '']

        for binary_str in accepting_inputs:
            with self.subTest(binary_str=binary_str):
                self.assertTrue(
                    automaton.accepts(binary_str),
                    msg=f"Automaton should accept '{binary_str}'"
                )

        for binary_str in rejecting_inputs:
            with self.subTest(binary_str=binary_str):
                self.assertFalse(
                    automaton.accepts(binary_str),
                    msg=f"Automaton should reject '{binary_str}'"
                )

if __name__ == '__main__':
    unittest.main()
