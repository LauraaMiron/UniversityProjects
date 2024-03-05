class Parser:
    def __init__(self, grammar, sequence_file):
        # Initialize the parser with a grammar and a sequence file
        self.grammar = grammar
        self.sequence = self.read_sequence(sequence_file)
        self.working = []  # A stack to keep track of parsing progress
        self.input = [self.grammar.get_start_symbol()]  # The input being parsed
        self.state = "q"  # The parser's state ("q" for normal parsing, "b" for backtracking, "f" for success, "e" for error)
        self.index = 0  # Current index in the input sequence

    @staticmethod
    def read_sequence(seq_file):
        # Read a sequence from a file and return it as a list
        seq = []
        with open(seq_file) as f:
            line = f.readline()
            while line:
                seq.append(line.strip())
                line = f.readline()
        return seq

    def get_situation(self):
        # Print the current situation (state, index, working stack, input)
        print(f"({self.state}, {self.index}, {self.working}, {self.input})")

    def expand(self):
        # Handle expansion of non-terminals
        print("|--- expand")
        non_terminal = self.input.pop(0)  # Get the first non-terminal in the input
        self.working.append((non_terminal, 0))  # Push a tuple indicating the non-terminal and its production index
        new_production = self.grammar.get_productions_for_non_terminal(non_terminal)[0]
        self.input = new_production + self.input  # Replace the non-terminal with its production in the input

    def advance(self):
        # Handle advancing in the input
        print("|--- advance")
        self.working.append(self.input.pop(0))  # Move the current terminal or non-terminal to the working stack
        self.index += 1  # Move to the next index in the input sequence

    def momentary_insuccess(self):
        # Handle momentary insuccess, indicating a mismatch or unexpected input
        print("|--- momentary insuccess")
        self.state = "b"  # Transition to backtracking state

    def back(self):
        # Handle backtracking
        print("|--- back")
        item = self.working.pop()  # Pop the last item from the working stack
        self.input.insert(0, item)  # Insert the item back to the input
        self.index -= 1  # Move back one index in the input sequence

    def success(self):
        # Handle successful parsing
        print("|--- success")
        self.state = "f"  # Transition to success state
        msg = f"(f, {self.index}, {self.working}, {self.input})\n=> sequence is syntactically correct\n"
        print(msg)

    def another_try(self):
        # Handle another try during backtracking
        print("|--- another try")
        if self.working:
            last_nt = self.working.pop()
            nt, production_nr = last_nt

            productions = self.grammar.get_productions_for_non_terminal(nt)

            if production_nr + 1 < len(productions):
                self.state = "q"

                new_tuple = (nt, production_nr + 1)
                self.working.append(new_tuple)

                len_last_production = len(productions[production_nr])
                self.input = self.input[len_last_production:]
                new_production = productions[production_nr + 1]
                self.input = new_production + self.input
            else:
                len_last_production = len(productions[production_nr])
                self.input = self.input[len_last_production:]
                if not len(self.input) == 0:
                    self.input = [nt] + self.input
        else:
            self.state = "e"  # Transition to error state if there is no more working stack

    def error(self):
        # Handle the error state
        print("|--- error")
        self.state = "e"
        msg = f"(e, {self.index}, {self.working}, {self.input})\nNo more input to look at!"
        print(msg)

    def run(self):
        # Main parsing loop
        while (self.state != "f") and (self.state != "e"):
            self.get_situation()
            if self.state == "q":
                if len(self.input) == 0 and self.index == len(self.sequence):
                    self.success()
                else:
                    if self.input[0] in self.grammar.get_non_terminals()[0].split(" "):
                        self.expand()
                    else:
                        if self.index < len(self.sequence) and self.input[0] == self.sequence[self.index]:
                            self.advance()
                        else:
                            self.momentary_insuccess()
            else:
                if self.state == "b":
                    if self.working and self.working[-1] in self.grammar.get_terminals()[0].split(" "):
                        self.back()
                    else:
                        self.another_try()

        if self.state == "e":
            self.get_situation()
            self.error()