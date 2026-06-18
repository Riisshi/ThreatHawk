import sys
import os

sys.path.append(os.path.abspath("."))

from backend.parser import parse_log_line

with open("logs/sample.log") as file:
    for line in file:
        result = parse_log_line(line)
        print(result)
