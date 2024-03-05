import re
from SymbolTable import SymbolTable

class Scanner:
    def __init__(self, source_code):
        self._line_count = 0
        self._source_code = source_code
        self._symbol_table = SymbolTable(30)
        self._program_internal_form = []
        self._tokens = []

        try:
            self.read_tokens()
            self.tokenize()
        except ValueError as err:
            print(err)

    def read_tokens(self):
        with open("token.in") as token_file:
            self._tokens = [line.rstrip() for line in token_file]

    def write_to_output_files(self):
        with open('PIF.txt', 'w') as pif_output_file:
            pif_output_file.write('\n'.join(map(str, self._program_internal_form)))

        with open('ST.txt', 'w') as st_output_file:
            st_output_file.write(str(self._symbol_table))

    def tokenize(self):
        lines = re.split('[\n]', self._source_code)
        non_empty_lines = [line for line in lines if line.strip()]

        for code_line in non_empty_lines:
            line_tokens = self.extract_tokens_from_line(code_line)

            for token in line_tokens:
                if token in self._tokens:
                    self._program_internal_form.append((token, 0))
                else:
                    self.classify_and_add_to_pif(token)

        self.write_to_output_files()
        print("Lexical analysis complete")

    def extract_tokens_from_line(self, line_string):
        self._line_count += 1
        line_elements = [element for element in re.findall(r'("[^"]+"|[a-zA-Z0-9]+|[^a-zA-Z0-9"\s]+)', line_string) if element.strip()]
        print(line_elements)

        final_line_tokens = []
        i = 0
        n = len(line_elements)

        while i < n:
            if i >= n:
                break

            current_element = line_elements[i]

            if current_element == '=':
                final_line_tokens.append('==' if line_elements[i + 1] == '=' else '=')
                i += 1 if line_elements[i + 1] == '=' else 0
            elif current_element == '<' and line_elements[i + 1] == '=':
                final_line_tokens.append('<=')
                i += 1
            elif current_element in {'<', '>', '<='}:
                final_line_tokens.append(current_element)
            else:
                final_line_tokens.append(current_element)

            i += 1

        return final_line_tokens

    def classify_and_add_to_pif(self, token):
        token_type = self.classify_token(token)

        if token_type == 1:
            self._symbol_table.add_identifier(token)
            self._program_internal_form.append(('identifier', self._symbol_table.get_position_identifier(token)))
        elif 2 <= token_type <= 4:
            self._symbol_table.add_constant(token)
            self._program_internal_form.append(('constant', self._symbol_table.get_position_constant(token)))
        else:
            raise ValueError(f"Lexical error: Token {token} cannot be classified: line {self._line_count}")

    @staticmethod
    def classify_token(token):
        match_identifier = re.match('^[a-z]+[a-z0-9]*$', token)
        if match_identifier:
            return 1

        match_string_constant = re.match(r'^"[a-zA-Z0-9\s]+"$', token)
        if match_string_constant:
            return 2

        match_char_constant = re.match('^\'[a-zA-Z0-9\'$]', token)
        if match_char_constant:
            return 3

        match_integer_constant = re.match('^0$|^(\+|-)?[1-9][0-9]*$', token)
        if match_integer_constant:
            return 4

        return 0


def analyze_program():
    with open('p2.txt', 'r') as file:
        lexer = Lexer(file.read())

analyze_program()
