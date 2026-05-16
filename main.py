file1 = open("sample.txt", "r")
content = file1.read
print(content)
file1.close()

file2 = open("sample.txt","w")
file2.write("Hi my name is Atharva and im practicing python file handling")
file2.close()

file3 = open("sample.txt",'a')
file2.write("My favourite subject is the studies of the physical universe.")
file3.close()