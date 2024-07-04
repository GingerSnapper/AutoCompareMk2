Tool to compare outputs between the target output (say, your professor's example output) and your own script's. 

Precondition: 
  - Your script's output should be saved as a text file, as well as the target text file. 
  - These should be named: "testfile.txt" and "targetfile.txt" and placed in the same folder as main.py. 
  - Sample txt files are provided. Simply open, CTRL+A, CTRL+V, and Save to commit your test output; repeat for target output.

Postcondition: 
  - Text files will not be overwritten, tool instead creates identical copies called file_a.txt, file_b.txt, with prefixed line numbers, and compares those.
  - Console log ouptuts any line numbers which have differences, with some pleasant formatting.
  - If no differences, outputs congratulations. 
  - One error-handle: if test file or target file is empty, prints error to the console regarding which file is empty.
