vlib work

vlog -timescale 1ps/1ps part3.v

vsim datapath

log {/*}
add wave {/*}

force {clk} 0 0, 1 1 -r 2
force {resetn} 0 0, 1 5
force {enable} 0 0, 1 10
force {colour_in} 011 0

run 1000ns 
