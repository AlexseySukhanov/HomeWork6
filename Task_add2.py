strings=[]
file=open("p310.html","r")
strings=file.readlines()
file.close()
file=open("p310n.html","w")

for st in strings:
    for ch in st:
        if ch=="<":
            l=st.find("<")
            r=st.find(">")
            st=st.replace(st[l:r+1],"")
    file.write(st)
    print(st)
file.close()


