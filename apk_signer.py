# A python module which creates .zip & .rar archives of subfolders of a given path

def listApks(folder_path):
    'Returns list of subfolders of given path'
    import os
    foldersList = list()
    print('Looking for subfolder of : %s' % (folder_path))
    for i in os.listdir(folder_path):
        if(os.path.isfile(i) and i.endswith(".apk")):
            #print('%s' % (i))
            foldersList.append(folder_path+"/"+i)
    print('\nTotal Subfolders: %s' % (len(foldersList)))
    return foldersList
    
def signApks(pathList):
    'create archives of folders list passed in first argument'
    import os
    for f in pathList:
        apk_name = os.path.basename(f)
        apk_name = apk_name.replace(".apk","")
        dir_name = os.path.dirname(f)
        command = 'java -jar signapk.jar certificate.pem key.pk8 "%s/%s.apk" "%s/%s-signed.apk"' % (
            dir_name, apk_name,dir_name,apk_name)
        print(apk_name)
        os.system(command)      
    print('Success: I am free now!')
    
if __name__ == "__main__":
    import sys
    import os
    print('# Zipper by Talha Asghar')
    
    if(len(sys.argv) == 1):
        choice = 'y'#input('Proceed with "%s" \n(y=yes, n=no) ? : ' % os.getcwd())
        if(choice == 'Y' or choice == 'y'):
            listApks(os.getcwd())
            signApks(listApks(os.getcwd()))
    else:
        print('Error : Invalid Command Entered!\nUsage : zipper.py [,extension]')

