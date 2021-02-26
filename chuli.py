#pip install jieba
import jieba
import re
import json
from collections import Counter
cutwords = ""
for line in open('./comments.json',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\“\”\，\。\：]", "", line)
    seglist=jieba.cut(line)
    cutwords += (" ".join(seglist))
words = cutwords.split()
c = Counter()
print(c)
for i in words:
    if len(i)>1 and i != '\r\n':
        c[i] += 1
comments = []
for k,v in c.most_common(200):
    comment = {}
    comment["name"] = k
    comment["value"] = v
    comments.append(comment)
    print(comment)
with open('Topword.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(comments, indent=2, ensure_ascii=False))