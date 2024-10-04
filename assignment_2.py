class FiniteAutomaton:
    """
    A generic Finite Automaton (FA) class for modeling finite state machines (FSM).
    """

    def __init__(
        self,
        states,
        input_alphabet,
        transition_function,
        initial_state,
        final_states,
    ):
        """
        Initializes the finite automaton.

        Parameters:
        - states: A set of states (Q).
        - input_alphabet: A set of input symbols (Σ).
        - transition_function: A function δ(q, σ) defining state transitions.
        - initial_state: The initial state (q0).
        - final_states: A set of accepting/final states (F).
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_states = final_states

        self._validate_automaton()

    def _validate_automaton(self):
        """
        Validates the FSM configuration.
        """
        if self.initial_state not in self.states:
            raise ValueError(f"Initial state '{self.initial_state}' is not in the set of states.")
        if not self.final_states.issubset(self.states):
            raise ValueError("Final states must be a subset of the set of states.")

    def process_input(self, input_sequence):
        """
        Processes an input sequence and returns the final state.

        Parameters:
        - input_sequence (str): A sequence of input symbols.

        Returns:
        - Any: The final state after processing the input sequence.
        """
        current_state = self.initial_state
        for index, symbol in enumerate(input_sequence):
            if symbol not in self.input_alphabet:
                raise ValueError(f"Invalid input symbol '{symbol}' at position {index}.")
            next_state = self.transition_function(current_state, symbol)
            if next_state not in self.states:
                raise ValueError(
                    f"Transition from state '{current_state}' with input '{symbol}' "
                    f"led to invalid state '{next_state}'."
                )
            current_state = next_state
        return current_state

    def accepts(self, input_sequence):
        """
        Determines if the input sequence is accepted by the automaton.

        Parameters:
        - input_sequence (str): A sequence of input symbols.

        Returns:
        - bool: True if the final state is an accepting state; False otherwise.
        """
        final_state = self.process_input(input_sequence)
        return final_state in self.final_states


class ModThreeAutomaton(FiniteAutomaton):
    """
    A finite automaton subclass specifically for computing modulo three of binary numbers.
    """

    def __init__(self):
        # Define the states
        states = {'S0', 'S1', 'S2'}

        # Define the input alphabet
        input_alphabet = {'0', '1'}

        # Define the initial state
        initial_state = 'S0'

        # Define the final states (all states are considered final in this context)
        final_states = states

        super().__init__(
            states=states,
            input_alphabet=input_alphabet,
            transition_function=self._transition_function,
            initial_state=initial_state,
            final_states=final_states,
        )

        # Mapping from states to remainders
        self.state_to_remainder = {'S0': 0, 'S1': 1, 'S2': 2}

    def _transition_function(self, state, input_symbol):
        """
        Transition function for the mod-three finite automaton.

        Parameters:
        - state (str): The current state.
        - input_symbol (str): The input symbol ('0' or '1').

        Returns:
        - str: The next state.
        """
        transition_table = {
            'S0': {'0': 'S0', '1': 'S1'},
            'S1': {'0': 'S2', '1': 'S0'},
            'S2': {'0': 'S1', '1': 'S2'},
        }
        return transition_table[state][input_symbol]

    def compute_remainder(self, binary_string):
        """
        Computes the remainder when the binary number represented by the input string is divided by three.

        Parameters:
        - binary_string (str): A string of '0's and '1's representing a binary number.

        Returns:
        - int: The remainder (0, 1, or 2).
        """
        final_state = self.process_input(binary_string)
        return self.state_to_remainder[final_state]


# Example usage
def main():
    """
    Main function demonstrating the use of ModThreeAutomaton.
    """
    mod_three_automaton = ModThreeAutomaton()
    test_inputs = ['1101', '1110', '1111', '110', '1010']
    for binary_str in test_inputs:
        try:
            remainder = mod_three_automaton.compute_remainder(binary_str)
            print(f"Input: '{binary_str}' => Remainder: {remainder}")
        except ValueError as e:
            print(f"Error processing input '{binary_str}': {e}")



if __name__ == "__main__":
    main()
