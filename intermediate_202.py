import sys
import math
import datetime

if len(sys.argv) < 1:
    assert False, "No year given"
Year = int(sys.argv[1])
a = Year % 19
b = math.floor(Year / 100)
c = Year % 100
d = math.floor(b / 4)
e = b % 4
f = math.floor((b + 8) / 25)
g = math.floor((b - f + 1) / 3)
h = ((19 * a) + b - d - g + 15) % 30
i = math.floor(c / 4)
k = c % 4
L = (32 + (2 * e) + (2 * i) - h - k) % 7
m = math.floor((a + (11 * h) + (22 * L)) / 451)
month = math.floor((h + L - (7 * m) + 114) / 31)
day = ((h + L - (7 * m) + 114) % 31) + 1
print datetime.date(Year, int(month), int(day))
