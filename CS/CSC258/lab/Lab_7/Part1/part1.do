vlib work

vlog -timescale 1ps/1ps ram32x4.v

vsim -L altera_mf_ver ram32x4

log {/*}
add wave {/*}

force {address} 2#10101 0, 2#01010 55, 2#10010 115 
force {clock} 0 0, 1 10 -r 20
force {data} 2#1011 0, 2#0011 35, 2#0010 55, 2#1001 115
force {wren} 0 0, 1 40, 0 80 

run 200ps