class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        from collections import defaultdict

        # Dictionary to group words by sorted characters
        anagram_map = defaultdict(list)

        for word in arr:
            # Sort the characters in the word to create a key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        # Return the grouped anagrams as a list of lists
        return list(anagram_map.values())
