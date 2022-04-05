class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        a = len(set(sentence))
        return a == 26