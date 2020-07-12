"""
This is the context manager example
"""

class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.file_name,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



with File("E:\sample_file.txt.txt", 'r') as file_header:
    print(file_header.readline())