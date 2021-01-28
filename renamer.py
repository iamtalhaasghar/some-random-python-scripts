# A simple script to prettify pdf file names

def listAllPdfFiles(dirPath):
    'Return list of all pdf files of provided path'
    import os
    pdfFiles = list()
    print('Looking for pdf files...')
    for f in os.listdir():
        if(os.path.isfile(f) and f.endswith('.pdf')):
            print('%s' % f, end=", ")
            pdfFiles.append(f)
    print()
    return pdfFiles

def prettifyFileNames(filesList):
    'prettifies file names as title strings'
    import os
    for e in filesList:
        newName = e.title().replace('_',' ')
        print('Renamed: %s >>> %s' % (e, newName))
        os.rename(e, newName)

def prettifyDesktopShortcuts(dirPath):
    import os    
    for f in os.listdir():
        if(f.endswith('hortcut.lnk') ):
            index = f.rfind('-')
            newName = '%s.lnk' % f[:index].strip()
            print('Renaming: %s >>> %s' % (f, newName))
            os.rename(f, newName)

if __name__ == "__main__":
    import os
    print('# File Names Prettifier by Talha Asghar')
    choice = input('Do you want to proceed : %s\n(y=yes, n=no) ? : ' % os.getcwd())
    if(choice=='y' or choice=='Y'):
        task = input('What can I do for you? Mr.Programmer!\n1) Prettify Desktop Shortcut Names\n2) Prettify PDF file Names\n? : ')
        if(task=='1'):
            prettifyDesktopShortcuts(os.getcwd())
        elif(task=='2'):
            prettifyFileNames(listAllPdfFiles(os.getcwd()))
        else:
            print('Seriously! I don`t have much time to deal with you insensible inputs.')
    print('Hey! Java Champion, I have done my work!!!')

