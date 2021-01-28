# A python module which creates .zip & .rar archives of subfolders of a given path

def subFolders(folder_path):
    'Returns list of subfolders of given path'
    import os
    foldersList = list()
    print('Looking for subfolder of : %s' % (folder_path))
    for i in os.listdir(folder_path):
        if(os.path.isdir(i)):
            print('%s' % (i), end=', ')
            foldersList.append(i)
    print('\nTotal Subfolders: %s' % (len(foldersList)))
    return foldersList
    
def createArchives(pathList, extension = 'zip'):
    'create archives of folders list passed in first argument'
    import os
    for f in pathList:
        command = '%s' % (f)
        os.chdir(command)
        command = 'winrar.exe a "%s.%s" * */ ' % (f, extension)
        print('Creating Archive: "%s" >>> "%s.%s"' % (f, f, extension))
        os.system(command)        
        command = "cd.."
        os.chdir("..")
    print('Success: I am free now!')
    
if __name__ == "__main__":
    import sys
    import os
    print('# Zipper by Talha Asghar')
    
    if(len(sys.argv) == 1):
        choice = input('Proceed with "%s" \n(y=yes, n=no) ? : ' % os.getcwd())
        if(choice == 'Y' or choice == 'y'):
            createArchives(subFolders(os.getcwd()))
    elif (len(sys.argv) == 2):
        choice = input('Proceed with "%s" \n(y=yes, n=no) ? : ' % os.getcwd())
        if(choice == 'Y' or choice == 'y'):
            createArchives(subFolders(os.getcwd()), sys.argv[1])
    else:
        print('Error : Invalid Command Entered!\nUsage : zipper.py [,extension]')

