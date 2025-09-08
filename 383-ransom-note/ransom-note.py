from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        count_ran = Counter(ransomNote)
        count_mag = Counter(magazine)

        for ch in count_ran:
            if ch not in count_mag:
                return False

        for ch in count_mag:
            if ch in count_ran:
                if count_mag[ch] < count_ran[ch]:
                    return False
        return True
