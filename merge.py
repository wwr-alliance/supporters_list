import json,glob
data=[]
for f in glob.glob('data/*.json'):
    with open(f)as x:data.append(json.load(x))
with open('combined.json','w')as f:json.dump(data,f)