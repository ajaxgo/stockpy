# coding=utf-8
import urllib2,os,string

def queryUrl(line):
    code = line.split(",",3)
    number = code[1]
    if(code[0]!='888888'):
        codeConv = parseMarket(code[0])
        url = urlBase+codeConv
        data = urllib2.urlopen(url).read();
        resultTuple = parseResult((code,data))
    else:
        codeConv=code[0]
        resultTuple=['',"1"]
    resultTuple.insert(0, codeConv)
    resultTuple.insert(1, number)
    return resultTuple

    # f.seek(0,0)s
# 将代码转换为代前缀的
def parseMarket(code):
    if(len(code)==6 ):
        if (code[0:1] == '6' or code[0:1] == '5'):
            return 'sh' + code;
        elif (code[0:1] == '0' or code[0:1] == '1'):
            return 'sz' + code
    elif(len(code)==5 ):
        return 'hk'+code
    elif(len(code)<5):
        return  'hk'+code.zfill(5)
    else:
        return code

def parseResult(resultTuple):
    fullContent = resultTuple[1].split('="', 3)
    code = resultTuple[0]
    content = fullContent[1].split(',', 10)
    if (len(code[0]) == 6 or code[0].startswith("sh")or code[0].startswith("sz")):
        stockName = content[0]
    elif (len(code[0]) == 5 or code[0].startswith("hk")):
        stockName = content[1]
    else:
        stockName=""
    # retStr = code[0] + "," + stockName + "," + content[3]
    list = []
    list.append(stockName)
    if(content[3]=="0.000"):#判断停牌
        list.append(content[2])
    else:
        list.append(content[3])
    return list


def refactorResult(list):
    sum = 0
    # cr为汇率，港股默认使用.85
    for item in list:
        if(item[0].startswith("hk")):
            cr=0.85
        else:
            cr=1
        sum=sum+(string.atof(item[3])*string.atoi(item[1])*cr)
    for val in list:
        if(val[0].startswith("hk")):
            cr=0.85
        else:
            cr=1
        ratio = string.atof(val[3])*string.atoi(val[1])*cr/sum
        val.append(format(ratio, '4.2%'))
    return list

# main start
urlBase =  "http://hq.sinajs.cn/list="
f = open("stockCalc.csv","r")
fw =  open("temp.csv","w")

resultList =[]
for line in f:
    line = line.strip('\n')
    dataline = queryUrl(line)
    resultList.append(dataline)

list = refactorResult(resultList)


    # resultList.append(dataline)
for result in list:
    strList = ",".join(result)
    fw.write(strList)
    fw.write("\n")

fw.close()
f.close()
os.remove("stockCalc.csv")
os.rename("temp.csv","stockCalc.csv")





