# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, score, total):
        self.label = label
        self.score = score
        self.total = total
    def status(self, percent):    # this parameter should be self
        return percent

r = Record()
print(r.status(95))

