import os
file_1 = open("PLP_Ass_Week4.py", "r")
file_2 = open("file_write.txt", "a")

content = file_1.read()
file_2.writelines("\nline1\nline2\nline3")
print(content)
file_1.close()
file_2.close()
os.remove("file_write.py")