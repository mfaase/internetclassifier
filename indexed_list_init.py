#import modules
import os

def indexed_list_init(somefile)
    '''
    run this script ONLY ONCE, will wipe your memory file if not careful
    
    Takes any list of items to be searched. 
    Preprends an index to a line. 
    Appends a memory state to a line. 
    Shuffles all lines. 
    Then saves these shuffled lines as memoryfile_in.txt
    '''
    #initialize memory-based list (RUN ONLY ONCE!)
    newlist = []
    counter = 1

    ratinglist = somefile
    root = os.getcwd()

    #load all lines from input.txt list,
    with open(root+'/'+ratinglist,'r', encoding="utf-8") as txtfile:
        #loop and add:
        for line in txtfile:
            #prepend sequential integer, 
            #add memory integer 0 to that list. 
            newlist.append([counter, line.strip(), '0'])
            counter += 1

    #Shuffle order of the .
    random.shuffle(newlist)
    
    #Save that list as memorylist_in.txt. (SEPARATE PART)
    root = os.getcwd()
    file = open(root+'/memoryfile_in.txt', 'w', encoding='utf-8')
    for i in range(len(newlist)):
        file.write(str(newlist[i][0])+','+newlist[i][1]+','+newlist[i][2]+'\n')
    file.close()

    print('File saved!')
