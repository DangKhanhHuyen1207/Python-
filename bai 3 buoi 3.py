s1=input('Nhap chuoi s1:')
s2=input('Nhap chuoi s2:')
res=[]
len_s1=len(s1)
len_s2=len(s2)
for i in range(max(len_s1,len_s2)):
    if i<len_s1:
        res.append(s1[i])
    if i<len_s2:
        res.append(s2[i])
result=''.join(res)
print(result)
