class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper() or word==word.capitalize() or word==word.lower():
            return True 
        return False
        