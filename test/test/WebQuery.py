import urllib2,os

urlBase =  "http://hq.sinajs.cn/list="
def queryUrl(line):
    code = line.split(",",3)
    codeConv = parseMarket(code[0])
    url = urlBase+codeConv
    data = urllib2.urlopen(url).read();
    kk = data.split('"',3)
    tt = kk[1].split(',',10)
    if(len(code[0])==6):
        stockName = tt[0]
    elif(len(code[0])==5):
        stockName = tt[1]
    retStr = code[0]+","+stockName+","+ tt[3]
    return retStr
    # f.seek(0,0)s

def parseMarket(code):
    if(len(code)==6):
        if (code[0:1] == '6' or code[0:1] == '5'):
            return 'sh' + code;
        elif (code[0:1] == '0' or code[0:1] == '1'):
            return 'sz' + code
    elif(len(code)==5):
        return 'hk'+code



f = open("E:/test.csv","r")
fw =  open("E:/temp.csv","w")

for line in f:
    dataline = queryUrl(line)
    fw.write(dataline+"\n")
fw.close()
f.close()
os.remove("E:/test.csv")
os.rename("E:/temp.csv","E:/test.csv")
# os.remove("E:/temp.csv")





