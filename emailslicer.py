'''
divide email into 2 parts(before and after @) -> save them into a file -> obtain an email from them
'''

source_file = open("email.txt.txt", 'r')
target_file = open("target.csv", 'a')

for line in source_file :
    if line.count('@')== 1 and len(line[0:line.index('@')]) >1 :
        username= line[0:line.index('@')]
        domain = line[line.index('@')+1:len(line.replace("\n",""))]
        target_file.write(username + "," + domain+"\n")
        print("Your Email is Sliced.")
    else:
        print("Invalid Email")

source_file.close()
target_file.close()
