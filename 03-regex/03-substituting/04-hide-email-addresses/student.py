# Write your code here
import re

def hide_email_addresses(string):
    def replace(match):
        stars1, stars2 = match.groups()
        return f'{'*' * len(stars1)}*{'*' * len(stars2)}'

    return re.sub(r'([a-zA-Z0-9.]+)@([a-zA-Z0-9.]+)', replace, string)