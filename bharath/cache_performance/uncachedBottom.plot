#set multiplot

set datafile separator ","

set key right top
set xlabel "Rank of site"
set ylabel "Cached Query RTT"
#set yrange [0:30000]
set autoscale
set pointsize 0.3

set terminal png tiny
set output "uncachedBottom.png"
set grid xtics ytics 1 1

plot "uncachedBottom" using 1:2 title "ISP" with linespoints lt -1  lw 0.9, "uncachedBottom" using 1:3 title "Google" with linespoints lt 3 lw 0.9,"uncachedBottom" using 1:4 title "OpenDns" with linespoints lt 1 lw 0.9

#unset multiplot
