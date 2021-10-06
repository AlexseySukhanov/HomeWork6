st=input("Input a string ")
count=0
for ch in st:
    if "b" in ch.lower():
        count+=1
print(f"Amount of 'b' {count}")
