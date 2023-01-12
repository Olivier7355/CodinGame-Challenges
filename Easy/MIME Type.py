import sys
import math

n = int(input())                                # Number of elements which make up the association table.
q = int(input())                                # Number Q of file names to be analyzed.
dictionary = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dictionary[ext.lower()] = mt                # Create a dict containing the ext as key and the MIME as value  

# Iterate through the list of file names to analyze
for i in range(q):  
    fname = input()  # One file name per line.
    farr = fname.split('.') # split the filename between the name and the extension
    print(farr, file=sys.stderr, flush=True)
    if len(farr)>1: # Check if the filename contains at least 2 parts
        try:
            print(dictionary[farr[-1].lower()]) # Print the dict value coresponding to the key extension
        except KeyError:                        # UNKNOWN if the extension is not in the dict
            print("UNKNOWN")
        except IndexError:
            print("UNKNOWN")
    else:                                       # UNKNOWN if the filename does not contain at least 2 parts
        print("UNKNOWN")
