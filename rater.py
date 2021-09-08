import os
import random

import cv2
import numpy as np
from skimage import io

import requests
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


#define itemrater program
def rater(itemname):
    
    #split input string into list
    itemname = itemname.split(',')
    
    #memory check in last list element
    if '1' not in itemname[2]:
        
        #call item name in middle list element and apply query
        item = itemname[1]
        print('Scanning', item.strip())
        query = item.strip()
        query= query.split()
        query='+'.join(query)
        
        #retrieve soup from search function on item query
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url="https://www.bing.com/images/search?q="+query+"&form=QBLH&sp=-1&pq="+query+"&sc=0-10&qs=n&cvid=8CA2E3701FF042A08817EBB7E9FCDA63&first=1&tsc=ImageBasicHover"
        resp = requests.get(url, headers = user_agent)
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        #stringify soup
        stringmess = str(soup) 
        
        #initialize link list plus add delimiters
        images = []
        start = ',"murl":"'      
        end = '"'
        
        starts = stringmess.split(start)
        for link in starts:
            linklist = link.split(end)
            images.append(linklist[0])
        
        #initialize memory value
        mem = 0
        
        #how many links
        if len(images) != 0:
            setting = 1
            print(len(images), 'images found.')
        #if no links, break out of the loop
        else:
            print(item.strip(), 'No bing image results.')
            itemstring = item.strip()
            cat_1 = 'NA'
            cat_2 = 'NA'
            cat_3 = 'NA'
            cat_4 = 'NA'
            mem = 1

        #initialize errorcounter (when all links forbidden)
        errorcount = 0
        #initialize exceptor
        exceptor = 0
        
        #as long as memory val is unchanged
        while mem == 0:
            if errorcount > len(images):
                itemstring = item.strip()
                cat_1 = 'NA'
                cat_3 = 'NA'
                cat_2 = 'NA'
                cat_4 = 'NA'
                mem = 1
            try:
                #reset setting value if you're at imagemax
                if setting == len(images):
                    setting = 1
                
                img = io.imread(images[setting])
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                cv2.imshow('URL Img', img)
                user = cv2.waitKey(0)
                
                #
                if user == 48: #NUM0
                    setting += 1                
                #
                elif user == 49: #NUM1
                    itemstring = item.strip()
                    cat_1 = 'TRUE'
                    cat_2 = 'TRUE'
                    cat_3 = 'TRUE'
                    cat_4 = 'FALSE'
                    print('Put', item.strip(), 'into Category 1')
                    mem = 1
                
                #
                elif user == 50: #NUM2
                    itemstring = item.strip()
                    cat_1 = 'FALSE'
                    cat_2 = 'TRUE'
                    cat_3 = 'TRUE'
                    cat_4 = 'FALSE'
                    print('Put', item.strip(), 'into Category 2')
                    mem = 1
                
                #
                elif user == 51: #NUM3
                    itemstring = item.strip()
                    cat_1 = 'FALSE'
                    cat_2 = 'FALSE'
                    cat_3 = 'TRUE'
                    cat_4 = 'FALSE'
                    print('Put', item.strip(), 'into Category 3')
                    mem = 1
                    
                #
                elif user == 52: #NUM4
                    itemstring = item.strip()
                    cat_1 = 'FALSE'
                    cat_2 = 'FALSE'
                    cat_4 = 'FALSE'
                    cat_3 = 'FALSE'
                    print('Put', item.strip(), 'into no category')
                    mem = 1
                
                # 
                elif user == 53: #NUM5
                    itemstring = item.strip()
                    cat_1 = 'FALSE'
                    cat_2 = 'FALSE'
                    cat_3 = 'FALSE'
                    cat_4 = 'TRUE'
                    print('Put', item.strip(), 'into Category 4')
                    mem = 1
                
                # terminates the program
                elif user == 54: #NUM6(?)
                    exceptor = 1
                    itemstring = item.strip()
                    cat_1 = 'NA'
                    cat_2 = 'NA'
                    cat_3 = 'NA'
                    cat_4 = 'NA'                 
                    print('Stopped')
                    mem = 1
                
                # if keystroke is not detected
                else:
                    print('input not recognized')
                    
            except:
                setting += 1
                errorcount += 1
                print('Erroring for', setting, 'of', len(images))
        
        cv2.destroyAllWindows()
        print('Returning results')
        outcome = [itemstring, cat_1, cat_2, cat_3, cat_4]
        return outcome, exceptor
        
    else:
        print(itemname[1],'already processed')
        outcome = [] 
        exceptor = 2
        return outcome, exceptor
