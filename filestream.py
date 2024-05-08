class Filestream:
    """
    A class representing a file stream.

    Attributes:
    - filename: The name of the file being streamed.
    - file: The file object used for reading.

    Methods:
    - read_line: Reads a single line from the file.
    - reset: Resets the file pointer to the beginning of the file.
    - close: Closes the file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')

    def read_line(self):
        """
        Reads a single line from the file.

        Returns:
        - A string representing the line read from the file.
        """
        return self.file.readline()
    
    def has_next_line(self):
        """
        Checks if there is a next line in the file.
        """
        pos = self.file.tell()  # Remember the current file position.
        line = self.file.readline()
        self.file.seek(pos)  # Restore the file position.
        return line != ''
    
    def reset(self):
        """
        Resets the file pointer to the beginning of the file.
        """
        self.file.close()
        self.file = open(self.filename, 'r')
    
    def close(self):
        """
        Closes the file.
        """
        self.file.close()