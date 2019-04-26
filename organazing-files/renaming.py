 
import sys, os, re, shutil


dateFormat = re.compile(r'((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)', re.VERBOSE)

fileNames = os.listdir('./rename')
for i in fileNames:
    match1 = dateFormat.search(i)
    stripedDate = i.split("-")
    print(stripedDate)
    
    if int(stripedDate[0]) < 12:
        newDate = stripedDate[1] + '-' + stripedDate[0] + '-' + stripedDate[2]
        shutil.move('./rename/' + i, './rename/' + newDate)
        print(newDate)
    

        
