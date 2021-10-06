words=list
file =open("english.txt","r")
words=file.readlines()
file.close()
length={}
st=input("Input a string ")
for word in words:
    if word.replace("\n","") in st:
        length[len(word)]= word.replace("\n","")
print(f"Shortest word {length[min(length.keys())]}")
print(f"Longest word {length[max(length.keys())]}")

