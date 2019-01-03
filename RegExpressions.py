#python

import re

root = "weyd : to see, to know : video, wit"
text = re.match(r'(.*?) : (.*?) : (.*)',root)
print("root : ", text.group(1))
print("definition : ", text.group(2))
print("reflexes : ", text.group(3))
