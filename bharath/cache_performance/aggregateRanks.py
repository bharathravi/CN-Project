# Use the multiple measurements collected over multiple days to get an
# average idea of the query times for each rank of site (popular vs unpopular)
def aggregate(filename, out):
  f = open(filename)

  ranks = {}

  for line in f:
    words = line.split(",")
    rank = int(words[1])

    if not ranks.has_key(rank):
      ranks[rank] = [0,0,0,0]
  
    isp = float(words[3])
    google = float(words[4])
    opendns = float(words[5])
  
    if not (isp == -1.0 or google == -1.0 or opendns == -1.0):
      ranks[rank][0] += isp
      ranks[rank][1] += google
      ranks[rank][2] += opendns
      ranks[rank][3] += 1
 

  f2 = open(out,"w")
  # Print out the average query times for each rank of site.
  ranklist = ranks.keys()
  ranklist.sort()
  for rank in ranklist:
    this = ranks[rank]
    if (this[3] > 0):
      f2.write(str(rank) + "," + str(this[0]/this[3]) + "," + str(this[1]/this[3]) + "," + str(this[2]/this[3]) + "\n") 

aggregate("cachedTimes", "aggCachedTimes")
aggregate("uncachedTimes", "aggUncachedTimes")
