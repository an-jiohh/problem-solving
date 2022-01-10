s = "0P"
s = s.lower()
cstr = []
for i in s :
    if ((97 <= ord(i)) & (ord(i) <= 122)) | ((48 <= ord(i)) & (ord(i)<= 57)) : cstr.append(i)
rcst = []
for i in cstr[::-1] :
    rcst.append(i)
print(rcst)
print(cstr)
if cstr == rcst : print(True)
else : print(False)