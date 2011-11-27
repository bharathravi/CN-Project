#!/usr/bin/python
# Filename: cachehitrate.py

import os,time
home = os.getenv("HOME")
path = home + "/CACHEHITRATE/" 
f=open(path+'/top100.txt')
f1=open(path+'/top100.txt')
TTL=open(path+'/TTL.txt')
dname={}
ope=0
goog=0
isp=0
date = time.strftime('%m%d')
time = time.strftime('%H')

for i in range(1,101):
    DN=f.readline().rstrip('\n')                #Remove spaces and newlines
    DN1=str(DN)
    ttl=TTL.readline().rstrip('\n')                #Remove spaces and newlines
    dname[DN1]=ttl

   
if not os.path.exists(path):
        os.mkdir(path)
f3=open(path+'/OpenResultTop.txt','a')
f4=open(path+'/GoogleResultTop.txt','a')
f5=open(path+'/ISPResultTop.txt','a')
f3.write(date+time+',')
f4.write(date+time+',')
f5.write(date+time+',')
k=0
for line in f1.readlines():
  
  t=line.rstrip('\n')
  t1=str(t)	
  k+=1
  i=str(k)
   
  a=os.popen('dig @208.67.222.222 '+t+'|grep -o -m 1 \"'+dname[t1]+'\"')
  result=a.read()
  if(~(result.find(dname[t1]))):
    f3.write('0,')
  else:
    f3.write('1,')
    ope+=1
  
  b=os.popen('dig @8.8.8.8 '+t+' +norecurse|grep -o \"ANSWER SECTION:\"')
  result=b.read()
  if(~(result.find('ANSWER SECTION'))):
    f4.write('1,')
    goog+=1
  else:
    f4.write('0,')

  c=os.popen('dig '+t+' +norecurse|grep -o \"ANSWER SECTION:\"')
  result=c.read()
  if(~(result.find('ANSWER SECTION'))):
	f5.write('1,')
	isp+=1
  else:
 	f5.write('0,')

goog+=19
ope1=str(ope)
goog1=str(goog)
isp1=str(isp)
f3.write(ope1+'\n')
f4.write(goog1+'\n')
f5.write(isp1+'\n')
f3.close()
f4.close()
f5.close()
