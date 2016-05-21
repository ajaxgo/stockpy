import urllib2

url =  "http://hq.sinajs.cn/list="
data = urllib2.urlopen("http://hq.sinajs.cn/list=sh601006").read();
print data
kk = data.split('"',3)
tt = kk[1].split(',',10)

print tt

