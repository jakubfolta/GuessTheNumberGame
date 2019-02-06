#! python3

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3})|\(\d{3}\)?
(\s|-|\.)?
(\d{3})
()


)''',re.VERBOSE)
