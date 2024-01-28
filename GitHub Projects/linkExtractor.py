import re 
import os

index = 0
writer = any
out = any
flag = 0
unsafe = [")", "<", ">","'","\"", "{", "}", "|", "\\", "^", "~", "[", "]", "`"]
# traverse directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(os.getcwd()):
    
    path = root.split(os.sep)
    if ("sample-onboarding-resources" in root.lower()):
        if (path[len(path)-1] == "sample-onboarding-resources"):
            index = len(path) + 1
        
        if len(path) == index:
            # open the file in the write mode
            print("Processing", root.lower())
            out = open(root + "/Links.txt", 'w', encoding='utf-8',errors="ignore")
            flag = 1

        if(len(path) >= index):
            for file in files:
                if not ( "links" in file.lower() or "change" in file.lower()):
                    with open(root+"/"+file, encoding='utf-8',errors="ignore") as f: 
                        for line in f: 
                            links = re.findall('(?P<url>https?://[^\s]+)', line)
                            if flag == 1:
                                for link in links:
                                    for ch in unsafe:
                                        link = link.split(ch)[0]
                                    out.write(link)
                                    out.write("\n")
        # close the file
        if flag == 1 and len(path) == index-1:
            out.close()
            flag = 0
