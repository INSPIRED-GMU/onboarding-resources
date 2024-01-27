
import os

flag = False
startLoc = input("Enter the location you want to start converting: ")
endLoc = input("Enter ending location (will not be converted): ")
# traverse directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(os.getcwd()):
    path = root.split(os.sep)
    if startLoc in path or startLoc == "none":
        flag = True
    if endLoc in path and endLoc != "none":
        break
    if ".git" not in path and flag:
        for file in files:
            path_no_ext = os.path.splitext(os.path.join(root,file))[0] 
            print(file)
            if file.endswith(".md") or file.endswith(".rst") or file.endswith(".html") or file.endswith(".yml"):
                try:
                    if file.endswith(".md"):
                        os.system('md-to-pdf ' + path_no_ext + ".md")
                        os.remove(path_no_ext + ".md")
                    elif file.endswith(".rst"):
                        os.system("rst2html5.py "+ path_no_ext+".rst " + path_no_ext + ".html" )
                        os.remove(path_no_ext + ".rst")
                        os.system("wkhtmltopdf "+ path_no_ext + ".html " + path_no_ext+".pdf")
                        os.remove(path_no_ext + ".html")
                    elif file.endswith(".html"):
                        os.system("wkhtmltopdf "+ path_no_ext + ".html " + path_no_ext+".pdf")
                        os.remove(path_no_ext + ".html")
                    elif file.endswith(".yml"):
                        os.rename(path_no_ext + ".yml", path_no_ext + ".txt")
                except WindowsError:
                    continue