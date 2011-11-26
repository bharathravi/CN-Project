#set multiplot

set datafile separator ","

set key right top
set xlabel "Time"
set ylabel "Query RTT"
#set yrange [0:30000]
set autoscale
set xdata time
set timefmt "%Y/%m/%d/%H:%M:%S"
set pointsize 0.3

set terminal png tiny
set output "timeofweek.png"
set grid xtics ytics 1 1

plot "summarised_avg_times" using 1:2 title "ISP" with linespoints lt -1  lw 0.9, "summarised_avg_times" using 1:3 title "Google" with linespoints lt 3 lw 0.9,"summarised_avg_times" using 1:4 title "ISP" with linespoints lt 1 lw 0.9

#unset multiplot
