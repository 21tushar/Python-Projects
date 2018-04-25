import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_url = pattern.sub(r'\2\3', urls)
print(subbed_url)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2))