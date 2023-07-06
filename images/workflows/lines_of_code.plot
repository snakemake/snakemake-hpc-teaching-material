set terminal png size 640,480
set size 1.0,1.0

set output 'lines_of_code.png'
unset key
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "{/*1.3 Lines of code}" 
set xtics rotate by 45 offset -4.5,-3
set bmargin 6
plot '/uni-mainz.de/homes/meesters/Documents/projects/hpc-jgu-lifescience/seq-analysis/stats_out/lines_of_code.dat' using 1:2 w lines lw 4 linecolor 2
