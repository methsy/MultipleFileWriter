def insert(files, text):
    """
    This methods opens an array of files and inserts the given string to all of them.

    Arguments:
        files: An array of file paths
        text: The String to be inserted

    """
    for file in files:
        file1 = open(file, "w")
        file1.write(text)


def append_same_line(files, text):
    """
    This method opens an array of files and appends the given string to all of them.

    Arguments:
        files: An array of file paths
        text: The String to be inserted
    """
    for file in files:
        file1 = open(file, "a+")
        file1.write(text)


def append_new_line(files, text):
    """
    This method opens an array of files and appends the given string to all of them at a new line.

    Arguments:
        files: An array of file paths
        text: The String to be inserted
    """
    for file in files:
        file1 = open(file, "a+")
        file1.write('\n'+text)
