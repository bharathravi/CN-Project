# Use the multiple measurements collected over multiple days to get an
# average idea of the query times for each rank of site (popular vs unpopular)
def averages(filename):
  f = open(filename)
  
  count = 0;
  isp = 0
  google = 0
  opendns = 0
  for line in f:
    words = line.split(",")
    rank = int(words[0])

    isp += float(words[1])
    google += float(words[2])
    opendns += float(words[3])
    count += 1
    

  return [isp/count, google/count, opendns/count] 
 

f2 = open("averageCacheStatistics","w")
list1 = averages("cachedTop")
list2 = averages("uncachedTop")
f2.write("Top Sites:\n")
f2.write("ISP- Cached:" + str(list1[0]) + " Uncached:" + str(list2[0]) + "\n")
f2.write("Google- Cached:" + str(list1[1]) + " Uncached:" + str(list2[1]) + "\n")
f2.write("OpenDns- Cached:" + str(list1[2]) + " Uncached:" + str(list2[2]) + "\n")

list1 = averages("cachedBottom")
list2 = averages("uncachedBottom")
f2.write("Bottom Sites:\n")
f2.write("ISP- Cached:" + str(list1[0]) + " Uncached:" + str(list2[0]) + "\n")
f2.write("Google- Cached:" + str(list1[1]) + " Uncached:" + str(list2[1]) + "\n")
f2.write("OpenDns- Cached:" + str(list1[2]) + " Uncached:" + str(list2[2]) + "\n")
