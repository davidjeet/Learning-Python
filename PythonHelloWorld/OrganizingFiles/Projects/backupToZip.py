#! python3
# backupToZip.py Copies an entire folder and its contents into
# a ZIP file whoe filename increments.

import zipfile, os, sys

def backupToZip(folder):

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')


    # Walk the entire folder tree and compress
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backupZip.write(os.path.join(foldername, filename))
    
    backupZip.close()
    print('Done.')

if len(sys.argv) == 2:
    path = sys.argv[1] #supply c:\temp
    backupToZip(path) 
else:
    print('Please supply correct path to zip.')