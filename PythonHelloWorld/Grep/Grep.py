#! python3
# Grep.py A way to find stuff in files


import zipfile, os, sys, re

invalidTypes = { 'zip', 'exe', 'bin', 'dll', 'jpg' , 'png', 'gif' }
list = []



def grep(folder, searchPhrase):

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Walk the entire folder tree and compress
    for foldername, subfolders, filenames in os.walk(folder):
        print('Searching files in %s...' % (foldername))
        
        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            file, file_extension = os.path.splitext(filename)
            if file_extension[1:] not in invalidTypes:                   
                if match(filename, searchPhrase) == True:
                    list.append(filename)
    
    print('RESULTS:\n' + '\n'.join(list))
end

def match(filename, searchPhrase):
    txt = r'^(.*?)' + searchPhrase + r'(.*?)$'
    regEx = re.compile(txt, re.VERBOSE)
    
    #now go into the file and go line by line and look for matches
    #for every line, increment the counter for line number
    #match by groups using findall (see phoneANdEmail.py)
    #to the list (should be a dictionary) we are adding each match
    #KV pairs (filepath, list(line number))

end

if len(sys.argv) == 3:
    folderPath = sys.argv[1]    #ex. c:\temp
    searchPhrase = sys.argv[2]  #ex. dog 
    grep(folderPath, searchPhrase)
else:
    print('Please supply correct parameters.')