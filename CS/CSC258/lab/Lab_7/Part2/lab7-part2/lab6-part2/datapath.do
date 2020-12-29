vlib work

vlog -timescale 1ns/1ns part2.v

vsim datapath

log {/*}
add wave {/*}

force {clk} 0 0, 1 1 -r 2

force {resetn} 0 0, 1 3

force {ldX} 0 0, 1 5, 0 10
force {ldY} 0 0, 1 15, 0 20
force {counter} 00000 0, 01111 35
force {x_in} 01110110
force {y_in} 1110001
run 50ns
