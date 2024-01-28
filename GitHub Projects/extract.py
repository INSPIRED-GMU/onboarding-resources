import os

# traverse directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(os.getcwd()):
    path = root.split(os.sep)
#    print((len(path) - 1) * '---', os.path.basename(root))
    if (".git" not in root.lower() and "wiki" not in root.lower()):
        for file in files:
            if not (file.lower() == "extract.py" or file.lower() == "linkExtractor.py" or file.endswith(".txt") or file.endswith(".md") or file.endswith(".rst") or "bug_report" in file.lower() or "feature_request" in file.lower()) or file.lower() == "links.txt":
                os.remove(os.path.join(root, file))
            if len(os.listdir(root)) == 0:
                os.rmdir(root)
        if len(os.listdir(root)) == 0:
            os.rmdir(root)
    