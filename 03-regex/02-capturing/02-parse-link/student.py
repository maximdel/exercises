# Write your code here
import re

def parse_link(string):
    link = re.fullmatch(r'<a href="(.*)?">(.*)</a>', string)
    if link:
        return (link.group(2),link.group(1))