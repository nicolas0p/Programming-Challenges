
class MinimalString:

    def __init__(self, s):
        self.s = list(s)
        self.t = []
        self.u = []

    def extract_first(self):
        self.t.append(self.s.pop(0))

    def extract_last(self):
        self.u.append(self.t.pop())

    def result(self):
        minimum = min(self.s)
        self.extract_first()
        while len(self.s) > 0 or len(self.t) > 0:
            if len(self.t) == 0:
                self.extract_first()
            if len(self.s) == 0:
                self.extract_last()
                continue
            a = self.s[0]
            b = self.t[-1]
            if b > a:
                self.extract_first()
                if self.t[-1] == minimum and len(self.s) > 0:
                    minimum = min(self.s)
            else:
                if b <= minimum:
                    self.extract_last()
                else:
                    self.extract_first()
                    if self.t[-1] == minimum and len(self.s) > 0:
                        minimum = min(self.s)
        return ''.join(self.u)

if __name__ == "__main__":
    s = input()
    obj = MinimalString(s)
    print(obj.result())
