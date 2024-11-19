class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen_list = sentence.split()
        for i in range(len(sen_list)):
            if searchWord in sen_list[i]:
                if searchWord==sen_list[i][:len(searchWord)]:
                    return i+1
        return -1
