f = open("avgtimes","r")

count = 0
isp = 0
google = 0
opendns = 0
for line in f:
  words = line.split(",")
  isp += float(words[4])
  google += float(words[5])
  opendns += float(words[6])
  
  count += 1
  if count == 10:
    count = 0
    print words[0] + "," + str(isp/10) + "," + str(google/10) + "," + str(opendns/10)
    isp = 0;
    google = 0
    opendns = 0
  

  


