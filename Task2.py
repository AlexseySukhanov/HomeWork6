name=input("Input a name ")
for ch in name:
    if ch.isdigit():
        if input("Incorrect name, remove digit? y/n ").lower()=="y":
            name=name.replace(ch,"")
            continue

        break
name=name.title()
print(name)
