vlib work

vlog -timescale 1ns/1ns part2.v

vsim part2

log {/*}
add wave {/*}

force {CLOCK_50} 0 0, 1 1 -r 2
force {KEY[0]} 0 0, 1 5

force {KEY[3]} 0 0, 1 10, 0 20, 1 30
force {SW} 0111110000 0, 0110011100 15
force {KEY[1]} 0 0, 1 40
run 100ns 