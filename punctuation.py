import os, nlpTool

punctuation = ['。', '，', '、', '：', ';', '?', '!', '...', ')', '–', '"', '」', '！', '？', '；', '．．．', '）', '“']
condition = []
# The ends in discourse_parser program
ENDs = ('?', '”', '…', '—', '、', '。', '」', '！', '，', '：', '；', '？')
# The end in CDTB paper
END = ('。', '?', '？', '！', '！', ':')
# The conjunction list in the CDTB paper
con = nlpTool.readText('data/conjunction.txt').split('\n')
conjun = [i.split(', ') for i in con]
conjunction = list(set(item.strip() for sublist in conjun for item in sublist))
# 內部分界點
in_END = ('…', '—', '、', '」', '，', '：', '；', '；')