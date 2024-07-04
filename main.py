# Comparison tool to check project output against target text output
# by Steve M

from __future__ import with_statement


def autoCompare(file1, file2):
    """
    Takes two text files, with same number of lines, saved in same folder as this script
    Call your output "testfile.txt", and the reference text "targetfile.txt".
    Returns basic comparison summary, then any line number with divergences
    """
    with open(file1, 'r') as f1:  # your file
        with open(file2, 'r') as f2:  # file to check against

            check1 = f1.read()
            # check1 (& check2 below) are type 'string'.
            # If a strings is empty, report it and stop operations.
            if check1 == "": 
                print("File 1 is empty")
                return

            check2 = f2.read()
            if check2 == "":
                print("File 2 is empty")
                return

            if check1 != check2:
                print("Difference detected.")
                f1.seek(0)
                f2.seek(0)
                testfile_lines = f1.readlines()
                targetfile_lines = f2.readlines()
                for i in range(len(testfile_lines)):
                    if testfile_lines[i] != targetfile_lines[i]:
                        print("Line " + str(i+1) + " doesn't match.")
                        print("------------------------")
                        print("File1: " + testfile_lines[i])
                        print("File2: " + targetfile_lines[i])
            else:
                print("Nice work, they're the same!")

def add_line_numbers(file):
    """
    Takes one argument: the filename of a text file, saved in the same folder as script.
    Returns a multi-line string of that file, with each line prepended to include line numbers
    """
    with open(file, 'r') as script:
        text = script.readlines()
        script.seek(0)
        size = len(text)
        new_script = ""
        for line in range(size):
            new_script += f'{line+1:>2}. {script.readline()}'
        return new_script

if __name__ == "__main__":
    with open("file_a.txt", 'w') as file_a:
        # testfile.txt - this is your file
        file_a.write(add_line_numbers("testfile.txt")) 
    with open("file_b.txt", 'w') as file_b:
        # targetfile.txt - this is theirs, the target file
        file_b.write(add_line_numbers("targetfile.txt")) 
    autoCompare("file_a.txt", "file_b.txt")
