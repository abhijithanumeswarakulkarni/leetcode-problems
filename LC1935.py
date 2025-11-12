class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for word in text.split(" "):
            canBeFormed = True
            for letter in word:
                if letter in brokenLetters:
                    canBeFormed = False
                    break
            if canBeFormed:
                res += 1
        return res