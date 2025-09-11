import re
def countWords(fileName = "task6_read_me.txt"):
    count = 0
    with open(fileName,"r") as file:
        text = file.read()
        words = re.findall(r'\w+',text)
        count= len(words)
    return count