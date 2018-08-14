 #<timestamp>-<value>-<message> logs to dictionnary

logs = """/
21022017 10:15:20-Alert-New York
21062017 04:04:20-Alert-Los Angeles
21022018 21:30:2O-Alert-Mountain View"""
a = logs.splitlines()
key = ["timestamp", "message", "location"]
res = {}
for i in range(1,len(a)):
    res1={}
    for k,v in zip(key,a[i].split("-")):
        res1.update({k:v})
    res.update({i:res1})
for k,v in res.items():
    print(str(k)+  ':' + str(v) +'\n')
