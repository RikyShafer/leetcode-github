class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        s = s.upper()
        t = t.upper()
        counter1 = Counter(s)

        # מילון עם כל האותיות באנגלית באותיות גדולות, גם אלו שלא מופיעות
        full_counter1 = {letter: counter1.get(letter, 0) for letter in string.ascii_uppercase}
        counter2 = Counter(t)

        # מילון עם כל האותיות באנגלית באותיות גדולות, גם אלו שלא מופיעות
        full_counter2 = {letter: counter2.get(letter, 0) for letter in string.ascii_uppercase}

        return full_counter1 == full_counter2

