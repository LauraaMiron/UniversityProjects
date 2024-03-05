class FiniteAutomaton:
    def __init__(self, file_path):
        self.states = set()
        self.alphabet = set()
        self.transitions = dict()
        self.initial_state = None
        self.final_states = set()
        self.read_fa_from_file(file_path)

    def read_fa_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip().split()

            if line[0] == 'States:':
                self.states = set(line[1:])
            elif line[0] == 'Alphabet:':
                self.alphabet = set(line[1:])
            elif line[0] == 'Transitions:':
                self.transitions = {(line[i], line[i + 1]): line[i + 2] for i in range(1, len(line)-2, 3)}
            elif line[0] == 'Initial:':
                self.initial_state = line[1]
            elif line[0] == 'Final:':
                self.final_states = set(line[1:])

    def display_elements(self):
        print("1. Set of States:", self.states)
        print("2. Alphabet:", self.alphabet)
        print("3. Transitions:")
        for transition, target_state in self.transitions.items():
            print(f"   {transition} -> {target_state}")
        print("4. Initial State:", self.initial_state)
        print("5. Set of Final States:", self.final_states)

    def is_sequence_accepted(self, sequence):
        current_state = self.initial_state

        for symbol in sequence:
            transition_key = (current_state, symbol)
            if transition_key in self.transitions:
                current_state = self.transitions[transition_key]
            else:
                return False

        return current_state in self.final_states


def main():
    file_path = "FA.in"
    fa = FiniteAutomaton(file_path)

    while True:
        print("\nMenu:")
        print("1. Display FA elements")
        print("2. Verify if a sequence is accepted")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            fa.display_elements()
        elif choice == '2':
            sequence = input("Enter the sequence to be verified: ")
            if fa.is_sequence_accepted(sequence):
                print("The sequence is accepted by the FA.")
            else:
                print("The sequence is not accepted by the FA.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
