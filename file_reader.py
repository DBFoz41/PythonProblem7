"""
File reading class
"""

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.str_list = ""
        self.str_split = ""
        self.list_str_numbers = []
        self.int_line = []
        self.int_line_list = []
        
    def _file_read_all_str_list(self):
        f = open(self.file_name, "r")
        self.str_list = f.readlines()
        f.close()
        
    def file_as_int_line_list(self):
        self._file_read_all_str_list()    
        
        for str_num in self.str_list:
            self.int_line = []
            self.str_split = str_num.split("\n")
            self.list_str_numbers = self.str_split[0].split(" ")
            for str_ele in self.list_str_numbers:
                self.int_line.append(int(str_ele))
            self.int_line_list.append(self.int_line)
        return self.int_line_list


#file_example = FileReader("inputFile.txt")
#lenght = file_example.file_as_int_line_list()
#print(lenght)
