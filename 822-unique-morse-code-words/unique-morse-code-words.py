class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dict1  = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

        res = set()
        for word in words:
            new_res=""
            for char in word:
                new_res+=dict1[char]
            res.add(new_res)
        return len(res)



