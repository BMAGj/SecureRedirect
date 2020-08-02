# This will only work if rules of the CSV creation are adhered to. CSV must be called labelLinks.csv. The Python copies JS Templates which will have Analytics inserted (one custom metric for each type of label).
# The JS templates are selfaware of there names and use that to find the JSON of the same name created by this Python Script. One Python per type of label so 3 in total (NFC, QR, ShortURL)

import csv 
import json 
import os 
import shutil

# Python finds its current directory and then accesses the relevant JS file to copy and rename

directory = os.getcwd() + "/"
jsLocation = os.getcwd() + "/JS/NFCtemplate.js"
tag = "NFCTAG"


#Opens csv

csv_file = open(directory +  'labelLinks.csv', 'r')
csv_reader = csv.DictReader(csv_file)
lcount = 0 

Obscure = ["dyydu","u76jr78jft","yjkyuietyj,yjtdyjtdyj,56u5e67u56,"
"5e67e5656h,"]
Obscure2 = ["1111dyydu","11111u76jr78jft","11111yjkyuietyj,yjtdyjtdyj,56u5e67u56,"
"11115e67e5656h,"]

# This """""" lcount could be replaced with a line by line read of the id field from the csv, notes at the end. 

# for loop that reads csv and outputs each row as a JSON file, creates a HTML with the script tag to a JS of the same Name, both our copied/created and moved to a Folder with the same name. The JS when called will find the JSON in the root directory of the system and redirect the user. 
 
for row in csv_reader:
    tag = "NFCTAG"
    tagID = tag + str(lcount)
    os.makedirs(tagID)
    
    
    tagID =   tagID + "/" + str(Obscure2[lcount]) + "/" + str(Obscure2[lcount])
    os.makedirs(tagID)

    tagID = tag + str(lcount)
    tag = tag + str(lcount)
    

    out = json.dumps(row)
    jsonoutput = open(directory + tag + "/" + str(Obscure2[lcount]) + "/" + str(Obscure2[lcount])  +'.json' , 'w')
    jsonoutput.write(out)

    
    tagID2 = str(Obscure2[lcount]) + ".js"
    
    jsPath = directory + tag + "/" + str(Obscure2[lcount]) + "/" + str(Obscure2[lcount]) + "/" + str(Obscure2[lcount])  + "/"  + tagID2
    htmlPath = directory + tag + "/" + str(Obscure2[lcount]) + "/" + str(Obscure2[lcount])  + "/" + "/" + Obscure[lcount] + ".html"
    shutil.copy(jsLocation, directory + tag + "/" + str(Obscure2[lcount]) + "/" + str(Obscure2[lcount])  + "/"  + tagID2)
    html = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>index</title>
</head>

<body>

""" + "<script src= """ + tagID2 + """></script>
</body>
</html>
"""
    file = open(htmlPath, "w")
    file.write(html)
    file.close()
    
    lcount+=1 
    

jsonoutput.close()
csv_file.close() 

# Might be good to add a part which finds the id in the JSON and names the file by that instead, that would help prevent user error, though the linking system will need strict rules to not lose track of which physical label holds which link, so not necessary.


