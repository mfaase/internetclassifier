#import modules
import os

def uniquetxt(oldtxt, newtxt)
    '''
    This script returns a new txt file only containing unique lines from two specified files.
    Provide txt stringnames as arguments, which should be in the same directory as the script.
    '''
    root = os.getcwd()

    nhandles_list = []
    ohandles_list = []
    handles_list = []

    #Load that list. 
    with open(root+oldtxt,'r', encoding="utf-8") as oldfile, open(root+newtxt, 'r', encoding="utf-8") as newfile:
        #Loop through items. 
        for nhandle in newfile:
            nhandles_list.append(nhandle.strip())
        for ohandle in oldfile: 
            ohandles_list.append(ohandle.strip())

    for x in nhandles_list:
        if x not in ohandles_list:
            print('Item', x,'NOT IN old list')
        else:
            pass
            
    file1 = open(root+"updated_newfile.txt","a") #append mode 
    for line in handles_list:
        file1.write(line +'\n') 
    file1.close() 