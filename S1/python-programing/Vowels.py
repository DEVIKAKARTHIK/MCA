word="Elephant"
vow="aeiouAEIOU"
occ={}
for ch in word:
    if ch in vow:
        occ[ch]=occ.get(ch,0)+1
print("Number of vowels")
for k,v in occ.items():
    print(k,":",v)