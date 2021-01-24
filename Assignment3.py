#Write a Python program to merge two files into a third file.
filenames = ['file1.txt', 'file2.txt']
with open('output_file.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())


#Take two lists as input list1 = [1,2,3,4,5] and list2 = ["a", "b", "c", "d", "e"] 
#From that make a dictionary ouput {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}

list1 = [1,2,3,4,5] 
list2 = ["a", "b", "c", "d", "e"]
dist1={}
for i in range(len(list1)):
    dist1[list1[i]]=list2[i]
    
print(dist1) 