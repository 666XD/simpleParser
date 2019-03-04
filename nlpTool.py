import re
import json
import os

def getChinese(context):
    # context = context.decode("utf-8") # convert context from str to unicode
    filtrate = re.compile(u'[^\u4E00-\u9FA5]') # non-Chinese unicode range
    context = filtrate.sub(r'', context) # remove all non-Chinese letters
    # context = context.encode("utf-8") # convert unicode back to str
    return context

def textClean(context):
    # Remove links:
    context = re.sub("http://[a-zA-z:?=#% ./\d]*","",context)
    # Remove emoji:
    context = re.sub("\[.{0,12}\]","",context)

    # Extract and remove tags:

    tags = re.findall("#(.{0,30})#",context)
    context = re.sub("#.{0,30}#","",context)

    # Extract and remove @somebody:
    at = re.findall("@([^@]{0,30})\s",context)
    context = re.sub("@([^@]{0,30})\s","",context)
    at+= re.findall("@([^@]{0,30})）",context)
    context = re.sub("@([^@]{0,30})）","",context)

    # Extract and remove english letters:
    english = re.findall("[a-z]+",context)
    context = re.sub("[a-z]+","",context)

    # Remove punctuation:
    # context = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",context)
    # context = re.sub("[【】╮╯▽╰╭★→「」]+","",context)
    # context = re.sub("！，❤。～《》：（）【】「」？”“；：、".decode("utf8"),"",context)

    # Remove space:
    context = re.sub("\s","",context)

    # Remove digits:
    context = re.sub("\d","",context)

    # Remove ....:
    context = re.sub("\.*","",context)

    return  context


def readText(name):
    with open(name, 'r', encoding='utf8') as f:
        d = f.read()
    return d


def readcsv(name):
    with open(name, 'r', encoding='utf8') as f:
        return json.load(f)
    return d


def saveText(data, name, split=False):
    if split:
        with open(name, 'w', encoding='utf8') as f:
            for i in data: f.write(i + '\n')
    else:
        with open(name, 'w', encoding='utf8') as f:
            f.write(data)

def saveCsv(data, name):
    with open(name, 'w', encoding='utf8') as f:
        json.dump(data, f)

def saveListAsText(data, name):
    with open(name, 'w', encoding='utf8') as f:
        for i in data:
            f.write(i+'\n')

def read_file(path=''):
    if path == '':
        all_texts = []
        for f in os.listdir():
            with open(f, encoding='utf8') as file_input:
                all_texts.append(file_input.read())
    else:
        all_texts = []
        for f in os.listdir(path):
            with open(path + f, encoding='utf8') as file_input:
                all_texts.append(file_input.read())

def read_filesInFile(path):
    file_list = []
    for f in os.listdir(path):
        for fi in os.listdir(path + '/' + f):
            file_list.append(path + '/' + f + '/' + fi)
    print('read', 'files:', len(file_list))
    all_texts = []
    for fi in file_list:
        with open(fi, encoding='utf8') as file_input:
            all_texts += [" ".join(file_input.readlines())]
    return all_texts