# Discourse Parser

一個簡單的斷句系統

本程式以 windows 系統來建構，建構在python3(32bit)，**注意使用 64bit 的 python 會出錯**
檔案內附帶 `CRF++` & `CKIPWS` window 執行檔
如果是使用 Linux 系統請自行安裝 CRF++ 和 CKIPWS，自行更換檔案內的兩個套件即可
而因為CKIP無法跑在Mac上，故無法在Mac系統上執行
因為 CKIPWS 有期限，若過期請自行至官網([http://ckipsvr.iis.sinica.edu.tw/](https://)) 建立帳號並下載更新檔替換

## 套件
`pip3 install opencc-python-reimplemented`


## 使用方式

python3 main.py <inputFile> <outputFile>
##### Exp: `python3 main.py -i data/example.txt -o data/testout.csv`
## 輸入檔案格式
請以 utf8 為編碼，文章檢簡繁不拘，以 `\n` 作為個句子的結束
> 範例請見 data/example.txt