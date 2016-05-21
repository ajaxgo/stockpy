import urllib2,os

urlBase =  "http://hq.sinajs.cn/list="
def queryUrl(line):
    eachdata = line.split(",",2)
    url = urlBase+"sh"+eachdata[0]
    data = urllib2.urlopen(url).read();
    kk = data.split('"',3)
    tt = kk[1].split(',',10)
    retStr = eachdata[0]+","+ tt[3]
    return retStr
    # f.seek(0,0)


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





