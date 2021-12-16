e = "a@a"
p = "123"
c = "16"
n = "a"
user = {}
user[e] = [p,n,c]
for k, v in user.items():
    print(k,v)
print(type(v[2]))
