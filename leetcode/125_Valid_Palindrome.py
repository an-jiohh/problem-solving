s = "A man, a plan, a canal: Panama"
s = s.lower()
cstr = []
for i in s :
    if ((97 <= ord(i)) & (ord(i) <= 122)) | ((48 <= ord(i)) & (ord(i)<= 57)) : cstr.append(i)
rcst = []
for i in cstr[::-1] :
    rcst.append(i)
if cstr == rcst : print(True)
else : print(False)