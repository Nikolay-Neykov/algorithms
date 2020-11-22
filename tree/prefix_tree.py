class Prefix_Tree():
    def __init__(self, character=None, level=0, *leaves):
        self.character = character
        self.leaves = set(leaves)
        self.level = level
        self.word = ''

    def find_words_for_prefix(self, prefix):
        current_leaf = self
        for character in prefix:
            current_leaf = current_leaf.find_leaf(character)
            if not current_leaf:
                return []

        return current_leaf.get_words_from_leaf()

    def get_words_from_leaf(self, found_words=[]):
        if self.word:
            found_words.append(self.word)
        for leaf in self.leaves:
            leaf.get_words_from_leaf(found_words)
        return found_words

    def add_word(self, word):
        current_leaf = self
        for character in word:
            found_leaf = current_leaf.find_leaf(character)
            if not found_leaf:
                found_leaf = Prefix_Tree(character, current_leaf.level + 1)
                current_leaf.leaves.add(found_leaf)
            current_leaf = found_leaf
        current_leaf.word = word

    def find_leaf(self, character):
        if self.leaves:
            for leaf in self.leaves:
                if leaf.character == character:
                    return leaf
        return None

    def print_leaves(self):
        for leaf in self.leaves:
            indent = leaf.level * '\t'
            print(f'{indent}{leaf.character}{leaf.word}')
            leaf.print_leaves()

    def __str__(self):
        print('\n')
        return f'{self.print_leaves()}'

    # def print_leaves(self, output_matrix):
    #     for leaf in self.leaves:
    #         if leaf.level == 1:
    #             for index in range(len(output_matrix)):
    #                 output_matrix[index] += '\t'
    #         if len(output_matrix) < leaf.level:
    #             output_matrix.append('')
    #         # indent = leaf.level * '\t'
    #         have_word = leaf.word if leaf.word else ''
    #         output_matrix[leaf.level - 1] += f'{leaf.character} {have_word}'
    #         leaf.print_leaves(output_matrix)

    # def __str__(self):
    #     print('\n')
    #     output_matrix = []
    #     f'{self.print_leaves(output_matrix)}'
    #     output = ''
    #     for level in output_matrix:
    #         output += f'{level}\n'
    #     return output

    def __repr__(self):
        return self.__str__()
