num = int(input("Enter the value:"))
seen_dic={}
seen=[]
for i in num:
    if i in seen_dic:
        seen.append(i)
else:
    seen_dic[i]=1    
    print(seen)