def itemcategorizer():
    root = os.cwd()

    #look for a rateditems.txt
    if os.path.getsize(root+'/rateditems.txt') == 0:
        print('File \'rateditems.txt\' is empty, creating a new one.')
        with open(root+'rateditems.txt','w+') as my_file:
            #header containing categories
            my_file.write('itemname, Category_1, Category_2, Category_3, Category_4\n')
    else:
        print('File \'rateditems.txt\' is not empty')

    exceptor = 0

    #Load the memoryfile input and output lists. 
    with open(root+'/memoryfile_in.txt','r', encoding="utf-8") as input_file, open(root+'/memoryfile_out.txt', 'w', encoding="utf-8") as output_file:

        #Loop through items. 
        for item in input_file:

            #if a certain output in the def
            if exceptor == 1:
                #quickly finish the script
                output_file.write(item)

            else:
                #loop through itemrater function
                outcome, exceptor = rater(item)

                #see if exceptor comes out the function
                if exceptor == 1:
                    output_file.write(item)
                    pass

                if exceptor == 2:
                    output_file.write(item)
                    pass

                else:
                    #decompose outcome into strings
                    itemstring = outcome[0]
                    cat_1 = outcome[1]
                    cat_2 = outcome[2]
                    cat_3 = outcome[3]
                    cat_4 = outcome[4]

                    #When rated,
                    #Write [integer, model_name, rating] into outputlist.txt
                    if exceptor == 0:
                        out_file = open(root+'/rateditems.txt', 'a', encoding='utf-8')
                        out_file.write(itemstring+','+cat_1+','+cat_2+','+cat_3+','+cat_4+'\n')
                        out_file.close()
                    else:
                        pass

                    #Update memory integer in memorylist.txt 
                    if exceptor == 0:
                        item = item.replace(',0\n',',1\n')
                        output_file.write(item)
                    else:
                        pass

    print('Done')
    
    
    ##change the output file to the input file for the next round
    with open(root+'/memoryfile_in.txt','w', encoding="utf-8") as input_file, open(root+'/memoryfile_out.txt', 'r', encoding="utf-8") as output_file:
        for line in output_file:
            input_file.write(line)
    #save memoryfile_out as memoryfile_in