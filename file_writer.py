"""
"""


class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.f = None

    def file_write_open(self):
        self.f = open(self.file_name, "w+")
        
    def file_write_all_str(self, string_to_write):
        string_to_write = string_to_write + "\n"
        self.f.write(string_to_write)

    def file_write_close(self):
        self.f.close()