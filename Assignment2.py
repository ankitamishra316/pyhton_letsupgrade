#Write a Python program to remove empty List from List.
list1=[1,2,3,[],8,9,[],0,5]
list2=[n for n in list1 if n!=[]]
print("New list is :",list2)   

#Write a Python program to remove all duplicates words from a given sentence
sent=input("Enter a sentence : ")
list1=sent.split()
output=[]
for i in list1:
    if i not in output:
        output.append(i)
    else:
        continue
print(' '.join(output)) 

#Write a Python program to find all occurrences of a character in the given string 
str1=input("Enter a string : ")
res="";
for i in str1:
    if i not in res:
        count=str1.count(i)
        res=res+i
    else:
        continue
    print("Count of ",i,"is",count)