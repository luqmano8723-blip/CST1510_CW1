# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        if percent >= 90:
            return "WARNING"
        return "OK"


r = Record("R-001", 95, 100)
print(r.status())
