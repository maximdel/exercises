import re

def parse_time(string):
    time = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?' , string)
    if time:
        h, m, s, ms = time.groups('.000')
        return int(h), int(m), int(s), int(ms[1:])