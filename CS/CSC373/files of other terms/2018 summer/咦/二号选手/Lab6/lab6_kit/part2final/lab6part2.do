vlib work

vlog -timescale 1ns/1ns lab6part2.v

vsim lab6part2


log {/*}

add wave {/*}

force {CLOCK_50} 0 0, 1 1 -r 2
force {KEY[0]} 0 0, 1 4
force {KEY[1]} 0 0, 1 4 -r 8
#A=1, B=3, C=10, X=2, result is 20
force {SW[7]} 0
force {SW[6]} 0
force {SW[5]} 0
force {SW[4]} 0
force {SW[3]} 0 8, 1 24, 0 32
force {SW[2]} 0
force {SW[1]} 0 8, 1 16
force {SW[0]} 1 8, 0 24

run 50 ns

force {CLOCK_50} 0 0, 1 1 -r 2
force {KEY[0]} 0 0, 1 4
force {KEY[1]} 0 0, 1 4 -r 8
#A=2, B=4, C=5, X=3, result is 
force {SW[7]} 0
force {SW[6]} 0
force {SW[5]} 0
force {SW[4]} 0
force {SW[3]} 0
force {SW[2]} 0 4, 1 12, 0 28
force {SW[1]} 1 4, 0 14, 1 28
force {SW[0]} 0 4, 1 20

run 50 ns
