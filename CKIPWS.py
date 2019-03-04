#!/usr/bin/python
#-*- encoding: UTF-8 -*-

from ctypes import *
ckipws = None

def initial(main_dll, py_dll, ini):
    global ckipws
    c_main_dll = c_wchar_p(main_dll)
    c_ini = c_wchar_p(ini)
    ckipws = CDLL(py_dll)
    ckipws.Initial(c_main_dll,c_ini)

def segment(inputStr, mode = 0):
    global ckipws
    Result = ''
    try:
        CResult = ckipws.Segment(inputStr)
        CResult = cast(CResult,c_wchar_p)
        Result = CResult.value
    except:
        pass
    finally:
        if mode == 0:
            WSResult = []
            Result = Result.split()
            for res in Result:
                re = res.strip()
                re = res[0:len(res)-1]
                temp = re.split(u'(')
                word = temp[0]
                pos = temp[1]
                WSResult.append((word,pos))
            #[('蔡英文', 'Nb'), ('是', 'SHI'), ...]
            return WSResult
        else:
            #蔡英文(Nb)　是(SHI)　中華民國(Nc)...
            return Result

def segList(corpus):
    # #指定 CKIPWS 統系統檔, 請勿修改
    main_dll = 'CKIPWS.dll'
    py_dll = 'PY_CKIPWS.dll'
    # 指定 CKIPWS 的設定檔
    ini = 'ws.ini'
	# 進行 CKIPWS 初始化的動作
    initial(main_dll, py_dll, ini)
    
    ans = []
    for text in corpus:
        ans.append(segment(text))
    # 結果在 Result 中
    return ans
