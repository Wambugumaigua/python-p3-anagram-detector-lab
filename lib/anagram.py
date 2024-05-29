# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        matches = []
        for potential_anagram in words:
            if self.is_anagram(potential_anagram):
                matches.append(potential_anagram)
        return matches

    def is_anagram(self, potential_anagram):
        potential_anagram_lower = potential_anagram.lower()
        return sorted(self.word) == sorted(potential_anagram_lower)
