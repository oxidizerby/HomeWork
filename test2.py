s="Шла Саша по шоссе и сосала сушку"
print(s)

i1 = s.find("а")
i2 = s.rfind("а")

s1 = s[:i1+1]
s2 = s[i1+1:i2]
s3 = s[i2:]

st=""
for sl in s2:
    if sl=="а": sl="А"
    st+=sl       
print(st)

s = s1 + st + s3
print(s)

print("New2 branch")

