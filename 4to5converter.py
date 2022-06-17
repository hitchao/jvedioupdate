output="D:\\Jvedio\\jvedioupdate\\list.json"
input="D:\\Jvedio\\jvedioupdate\\list"
names=[]
hashes=[]
with open(input,'r',encoding="utf8") as f:
    content=f.read()
    for item in content.split('\n'):
        if item is None or len(item)<=0 or item.index(' ')<=0:continue
        name=item.split(' ')[0]
        hash=item.split(' ')[1]
        names.append(name)
        hashes.append(hash)
d={"FileName":names,"FileHash":hashes}
print(d)
