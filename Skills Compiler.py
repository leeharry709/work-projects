import os
import sys
import win32com.client
from docx import Document

looper = 0
print("\nRunning Skills Compiler.py...\n")
# os change directory
dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"
crit = 0
skip = 0

folder_input = " iii "
folder_input_jet = " iii "

while crit == 0:
    looper = 0
    skip = 0
    while looper == 0:
        skip = 0
        while dir_path == "--DIRECTORY REDACTED FOR PRIVACY--":
            print("\n\n[BASE] Directory:   " + dir_path)
            folder_input = ""
            folder_input = input("Enter folder name (type 'exit' to close window): ")
            re_path = dir_path
            dir_path = dir_path+folder_input
        if folder_input.lower() == "exit":
            crit = 1
            looper = 1
        else:
            if folder_input.lower() == "jet":
                pass
            else:
                try:    
                    os.chdir(dir_path)
                    looper = 1
                    skip = 1
                except FileNotFoundError:
                    print("Folder not found...")
                    dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"
                    skip = 1
                
        if skip == 1:
            pass
        else:
            if folder_input.lower() == "jet":
                dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"
            while dir_path == "--DIRECTORY REDACTED FOR PRIVACY--":
                print("\n\n[JET] Directory:   " + dir_path)
                folder_input_jet = ""
                folder_input_jet = input("[JET] Enter folder name (type 'exit to close window): ")
                re_path = dir_path
                dir_path = dir_path + folder_input_jet
            if folder_input_jet.lower() == "back":
                dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"
            else:
                if folder_input_jet.lower() == "exit":
                    crit = 1
                    looper = 1
                else:
                    try:
                        os.chdir(dir_path)
                        looper = 1
                    except FileNotFoundError:
                        print("Folder not found...")
                        dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"
                        

                
                
                
                
    g = open('text_dumpster.txt', 'w')
    skipname = 'text_dumpster.txt'
    
    if crit == 0:
        counter = 0
        for filename in os.listdir(os.getcwd()):
            counter += 1
            blocker = ''
            print("["+str(counter)+"]"+" "+filename)
            # ----- .DOCX READER -----
            if filename[filename.index("."):].lower() == '.docx':
                if filename[0] == '~':
                    pass
                else:
                    f = open(filename, 'rb')
                    document = Document(f)
                    for p in document.paragraphs:
                        try:
                            if 'Job Duties & Responsibilities' in p.text.strip():
                                blocker = 'Job Duties & Responsibilities'
                            if 'Education and Experience' in p.text.strip():
                                blocker = ''
                            if blocker == 'Job Duties & Responsibilities':
                                g.write(p.text)
                                g.write('\n')
                        except UnicodeEncodeError:
                            pass
                        pass
                    f.close()
            
            # ----- .DOC READER -----
            if filename[filename.index("."):].lower() == '.doc':
                if filename[0] == '~':
                    pass
                else:
                    DOC_FILEPATH = dir_path + '/'+ filename
                    doc = win32com.client.GetObject(DOC_FILEPATH)
                    text = doc.Range().Text
                    with open(filename[:filename.index(".")]+'.txt', "wb") as f:
                        f.write(text.encode("utf-8"))
                f.close()
            
            # ----- .TXT READER -----
            if filename[filename.index('.'):].lower() == '.txt':
                if filename == skipname:
                    pass
                else:
                    with open(filename) as f:
                        try:
                            line = f.readline()
                            for line in f:
                                if 'Job Duties & Responsibilities' in line.strip():
                                    blocker = 'Job Duties & Responsibilities'
                                if 'Education and Experience' in line.strip():
                                    blocker = ''
                                if blocker == 'Job Duties & Responsibilities':
                                    g.write(line)
                        except UnicodeDecodeError:
                            pass
                f.close()
        g.close()
    else:
        pass
    

    skip = 0
    dir_path = re_path
    os.chdir(re_path)

    print("\n\n")
    
print("\n--Process successfully completed.")