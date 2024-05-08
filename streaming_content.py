from filestream import Filestream

fs = Filestream('animals.txt')
print(fs.read_line())   # Read the first line of the file
print(fs.read_line())   # Read the second
fs.reset()              # Reset the file pointer to the beginning
print(fs.read_line())   # Read the first line again
fs.close()              # Close the file