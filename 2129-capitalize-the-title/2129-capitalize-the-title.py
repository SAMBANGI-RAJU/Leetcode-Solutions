class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title = title.split()
        result = []
        for word in title:
            if len(word)>2:
                result.append(word.title())
            else:
                result.append(word)
                
        return " ".join(result)