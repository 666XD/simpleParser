# Discourse Parser

一個簡單的斷句系統

* 本程式建構在 Windows python3(32bit)，**注意使用 64bit 的 python 會出錯**
* 檔案內附帶 `CRF++` & `CKIPWS` window 執行檔
* 若是使用 Linux 系統，請自行安裝 CRF++ 和 CKIPWS，且程式或需要小幅度更改
* CKIP 無法跑在 Mac 上，故無法在 Mac 系統上執行
* CKIPWS 有期限限制，若過期請自行至官網([http://ckipsvr.iis.sinica.edu.tw/](https://)) 建立帳號並下載更新檔替換

## 套件
`pip3 install opencc-python-reimplemented`

## 使用方式

python3 main.py <inputFile> <outputFile>
##### Exp: `python3 main.py -i data/example.txt -o data/testout.csv`
## 輸入檔案格式
請以 utf8 為編碼，文章檢簡繁不拘，以 `\n` 作為個句子的結束
> 範例請見 data/example.txt
