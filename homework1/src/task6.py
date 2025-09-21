import re
def countWords(fileName = "task6_read_me.txt"):
    """
    Opens the file provided and counts the number
    of words using a simple regex

    Args:
        filenName: the name of the file

    Returns:
        int: The word count of the file
    """
    count = 0
    with open(fileName,"r") as file:
        text = file.read()
        words = re.findall(r'\w+',text)
        count= len(words)
    return count

if __name__=="__main__":
    file = input("enter a file to word count: ")
    print(f"{file}: {countWords(file)} words")