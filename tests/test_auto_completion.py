from tree.prefix_tree import Prefix_Tree
# from english_words import english_words_set
import unittest


class AutoCompletion(unittest.TestCase):

    def test_auto_completion(self):
        tree = Prefix_Tree()

        # all words
        # for word in english_words_set:
        #     tree.add_word(word)

        # for the test
        english_words_set = ['something', 'varnish', 'vary', 'various', 'variac', 'variate',
                             'variant', 'variable', 'varistor', 'variegate', 'variety', 'varsity']
        for word in english_words_set:
            tree.add_word(word)
        # print(tree)

        prefix = 'var'
        auto_completions = tree.find_words_for_prefix(prefix)
        print(auto_completions)
        self.assertCountEqual(auto_completions, ['varnish', 'vary', 'various', 'variac', 'variate',
                                                 'variant', 'variable', 'varistor', 'variegate', 'variety', 'varsity'])
