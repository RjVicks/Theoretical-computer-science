""" Turing machine
% States: These are constants for n states, 0, ..., n-1
% Current state: starts at qo.
% Alphabet: A constant set of symbols
% Tape Alphabet: A super set of the alphatbet also includes tape symbols
% start state
% a string of elements
% head: the current position of the head

* transistion function:
* get configuration: prints the configuration of the TM
"""

class TuringMachine():
    """docstring for TuringMachine."""

    def __init__(self, transistion_function_description_file):
        self.N_STATES = 0
        self.current_state = 0
        self.head_ = 0
        self.tail = 0
        self.tape = ['_' for x in range(100)]
        self.transistion_function = self.load_transition_function_from_file(transistion_function_description_file)


    def load_transition_function_from_file(self):
        pass

    def load_input_string(self, input_string):
        for i, x in enumerate(input_strings):
            self.tape[i] = x
            self.tail = i+1

    def transistion(self):
        next_state, write_symbol, head_movement = self.transistion_function(self.current_state, self.tape[self.head])
        self.tape[self.head] = write_symbol
        self.current_state = next_state
        if head_movement == 'L':
            self.head -= 1
        elif head_movement == 'R':
            self.head += 1

    def print_configuration(self):
        configuration = ""
        for i in range(self.head):
            configuration += self.tape[i]
            configuration += "q" + str(self.current_state)

        i = self.head
        while self.tape[i] != '_':
            configuration += self.tape[i]
            i += 1
        configuration += self.tape[i]

        print(configuration)


    def run(self):
        while self.current_state != "accept" or self.current_state != "reject":
            print(configuration)
            self.transistion()
