import unittest
import minimalString as m

class minimalStringTest(unittest.TestCase):

    def test1(self):
        text = "cab"
        obj = m.MinimalString(text)
        result = obj.result()
        self.assertEqual("abc", result)

    def test2(self):
        text = "acdb"
        obj = m.MinimalString(text)
        result = obj.result()
        self.assertEqual("abdc", result)

    def test3(self):
        text = "bababaaababaabbbbbabbbbbbaaabbabaaaaabbbbbaaaabbbbabaabaabababbbabbabbabaaababbabbababaaaaabaaaabbba"
        obj = m.MinimalString(text)
        result = obj.result()
        correct = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        self.assertEqual(correct, result)

    def test4(self):
        text = "a"
        obj = m.MinimalString(text)
        result = obj.result()
        self.assertEqual("a", result)

    def test5(self):
        text = "baaaaaababbbbbaaababaaabbabbabbbaabaaaaabbbaaababaabbbabbbabaaabbaabbabbbbbbbaabbabbabababbabbabaababbaabababbabbaabbabaaabbaaaaaaabbaabaabbababbabbbbaaaaabaabaaaabbabaaaabbbbbabaaabbababbbbaabbaabbaaaabbbbaabbababbaaabbbbabbabaaaaabbabaaaabaabaabbbabababaaababaabaabbabbbbaabbabbabaaaababbbaabbbbaaabbabbbbabbbaaaabbbaabbaabaaabaaaaaabbbbbabbbbbbabaabbbaababaaabbaabbabbbbbbbbbaaabaababaaabbbabaaaabbbabaaaabbbbaaaaaabbaaaaabbaaaababaaaaaaababbaaabbbbaababbaabbaababaaabaabbababbbabaaaabbbbaabbabaabbbaaaaabbab"
        obj = m.MinimalString(text)
        result = obj.result()
        correct = "a" * 261 + "b" * 250
        #import pdb; pdb.set_trace()
        self.assertEqual(correct, result)

if __name__ == '__main__':
    unittest.main()
