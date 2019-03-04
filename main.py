import sys, json, CKIPWS, CRF_prepare, argparse
from opencc import OpenCC
cc = OpenCC('s2t')
EOS = ['。', '?', '？', '！', '！', ':']
NEOS = ['，', '、', '：', ';', '；']
punt = EOS+NEOS

with open('data/CDTB_relation.json', 'r') as f:
    relation = json.load(f)

relationWord = []
for num, r in enumerate(relation):
    relationWord.append([])
    for word in relation[r]:
        relationWord[num].append(cc.convert(word))

def checkRelation(word):
    if word == '': return ''
    for i in range(1, len(word)):
        if word[:i] in relationWord[1]:
            return 'Caus'
        if word[:i] in relationWord[3]:
            return 'Expl'
        if word[:i] in relationWord[2]:
            return 'Tran'
        if word[:i] in relationWord[0]:
            return 'Coor'
    return 'Coor'

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="data/example.txt", help="input file")
parser.add_argument("-o", "--output", type=str, default="data/output.csv", help="output file")
args = parser.parse_args()

with open(args.input, 'r', encoding='utf8') as f:
    data = f.read()
# with open('data/example.txt', 'r', encoding='utf8') as f:
#     data = f.read()

data = cc.convert(data)
data = data.split('\n')

segResoult = CKIPWS.segList(data)
CRF_prepare.convertData(segResoult)


with open('crfPredict.txt', 'r', encoding='utf8') as f:
    data = f.read()

data = data.split('\n\n')
data1 = []
for d in data:
    data1.append(d.split('\n'))

crf1 = []
for d in data1:
    sent = ''
    tag = ''
    for j in d:
        sent += j.split('\t')[0]
        for _ in range(len(j.split('\t')[0])):
            tag += j.split('\t')[-1]
    crf1.append([sent, tag])

del data1, data


# convert
ans = []
for data in crf1:
    if data == ['', '']: continue
    sent = data[0]
    s = ''
    for num, word in enumerate(sent):
        if sent == '': continue
        if word in EOS:
            s += word + '|'
            s += checkRelation(sent[num+1:num+4]) + ' '
        elif data[1][num] == 'S':
            s += word + '|'
            s += checkRelation(sent[num + 1:num + 4]) + ' '
        else: s += word
    if s[-2] == '|': s = s[:-2]
    ans.append(s)

with open(args.output, 'w', encoding='utf8') as f:
    for i in ans:
        f.write(i+',\n')
