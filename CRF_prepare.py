import json, punctuation, os

# init
inner_end = punctuation.in_END
CJT = punctuation.conjun
END = punctuation.END

# testing Data for single sentence prepare
## 1. used the CKIPconvert.py file to convert sentence to posTage sentence
## 2. read file

def convertData(mg_result):
    ansSent = ''
    for text in mg_result:
        for num, sent in enumerate(text):
            if sent[0] != '|':
                if sent[0] in END:
                    ansSent += sent[0] + ' ' + 'END'
                elif sent[0] in inner_end:
                    ansSent += sent[0] + ' ' + 'in_END'
                else:
                    ansSent += sent[0] + ' ' + sent[1]
                if sent[0] in CJT: ansSent += ' yes'
                else: ansSent += ' no'
                if sent[0] in inner_end: ansSent += ' yes'
                else: ansSent += ' no'
                ansSent += '\n'
        ansSent += '\n'
    ansSent += '\n'
    
    ## 4. output the CRF test file
    with open('crf_test_data.txt', 'w', encoding='utf8') as f:
        f.write(ansSent)
    ## 5. Used: crf_test -m model_t3_3_MG data1.txt -o data1Ret.txt
    os.system('crf_test -m model_t3_3_MG crf_test_data.txt -o crfPredict.txt')
