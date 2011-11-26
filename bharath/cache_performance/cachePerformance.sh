#!/bin/sh

python aggregateRanks.py
head -n100 aggCachedTimes > cachedTop
tail -n99 aggCachedTimes > cachedBottom

head -n100 aggUncachedTimes > uncachedTop
tail -n99 aggUncachedTimes > uncachedBottom

gnuplot "cachedTop.plot"
gnuplot "cachedBottom.plot"
gnuplot "uncachedTop.plot"
gnuplot "uncachedBottom.plot"

python averageCachePerformance.py
