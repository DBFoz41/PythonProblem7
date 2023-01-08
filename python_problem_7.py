"""
Jolly Jumper problem

Given a sequence of integers, taking the abs difference between each consecutive value to create a new sequence
If that new sequence includes consecutive integers from 1 to n-1, this is called Jolly, else not jolly

"""

import file_reader as fr
import file_writer as fw

class JollyJumper:

    def __init__(self):
        self.int_list_to_process = []
        self.sequence_list = []
        self.n_value = 0
        self.sequence_list_max = 0
        self.jumper_check = 0
     

    def process_int_list(self, int_list_to_process):
        self.int_list_to_process = int_list_to_process
        self.sequence_list = []
        
        self.n_value = len(self.int_list_to_process)

        for index in range(self.n_value-1):
            self.sequence_list.append(abs(self.int_list_to_process[index] - self.int_list_to_process[index+1]))
        
        self.sequence_list_max = max(self.sequence_list)

        self.jumper_check = ((self.n_value-1)/2)*(1 + self.sequence_list_max)


        if self.jumper_check == sum(self.sequence_list):
            return "Jolly"
        else:
            return "Not Jolly"


def execute_main():
    input_int_list = []
    file = fr.FileReader("inputFile.txt")
    fileOut = fw.FileWriter("outputFile.txt")
    input_int_list = file.file_as_int_line_list()
    solve = JollyJumper()
    return_string = ""

    fileOut.file_write_open()
    for number_input in input_int_list:
        return_string = solve.process_int_list(number_input)
        fileOut.file_write_all_str(return_string)
    fileOut.file_write_close()

if __name__ == "__main__":
    execute_main()