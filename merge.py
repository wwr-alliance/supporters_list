import json,glob,os
data=[]
for f in sorted(glob.glob('data/*.json')):
    with open(f,encoding='utf-8')as x:data.append(json.load(x))
os.makedirs('docs',exist_ok=True)
with open('docs/index.json','w',encoding='utf-8')as f:json.dump(data,f,ensure_ascii=False)