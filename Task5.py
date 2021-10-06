st=input("Input string ")
words=st.split(" ")
length={}
for word in words:
    length[len(word)]= word
print(f"Longest word is: {length[max(length.keys())]}")