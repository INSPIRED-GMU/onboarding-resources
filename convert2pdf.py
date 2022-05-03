import os

flag = False
# traverse directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(os.getcwd()):
    path = root.split(os.sep)
    if "startLoc" in path:
        flag = True
    if "endLoc" in path:
        break
    if ".git" not in path and flag:
        for file in files:
            path_no_ext = os.path.splitext(os.path.join(root,file))[0] 
            print(file)
            if file.endswith(".md") or file.endswith(".rst") or file.endswith(".html"):
                try:
                    if file.endswith(".md"):
                        os.system('grip --user yourUsername --pass yourPassword '+ path_no_ext + ".md"+" --export "+path_no_ext + ".html")
                    #    os.remove(path_no_ext + ".md")
                    if file.endswith(".rst"):
                        os.system("rst2html5.py "+ path_no_ext+".rst " + path_no_ext + ".html" )
                    #    os.remove(path_no_ext + ".rst")
                    os.system("wkhtmltopdf "+ path_no_ext + ".html " + path_no_ext+".pdf")
                    os.remove(path_no_ext + ".html")
                except WindowsError:
                    continue