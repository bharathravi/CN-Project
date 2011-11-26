f = open("summarised_avg_times","r")

count = 0
isp = {}
google = {}
opendns = {}
for line in f:
  words = line.split(",")
  hour = words[0].split("/")[3][0:2]
  
  if not isp.has_key(hour):
    isp[hour] = [0,0]
 
  if not google.has_key(hour):
    google[hour] = [0,0]
 
  if not opendns.has_key(hour):
    opendns[hour] = [0,0]

  isp[hour][0] += float(words[1])
  google[hour][0] += float(words[2])
  opendns[hour][0] += float(words[3])
  isp[hour][1] += 1
  google[hour][1] += 1
  opendns[hour][1] += 1


for j in range(0,24): 
  i = str(j)

  if j<10:
   i = '0' + str(j)

  if isp.has_key(i) or google.has_key(i) or opendns.has_key(i):
    print i,

  print ",",
  if isp.has_key(i):
    print isp[i][0]/isp[i][1],
  else:
   print "-",
   
  print ",",
  if google.has_key(i):
    print google[i][0]/google[i][1],
  else:
   print "-",
   
  print ",",
  if opendns.has_key(i):
    print opendns[i][0]/opendns[i][1]
  else:
   print "-"
