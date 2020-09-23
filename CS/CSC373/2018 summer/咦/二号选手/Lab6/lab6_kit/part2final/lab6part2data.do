vlib work

vlog -timescale 1ns/1ns fpga_top.v

vsim datapath

log {/*}

add wave {/*}

force {resetn} 0
force {clk} 0 0, 1 10 -r 20
run 20 ns

force {resetn} 1
force {clk} 0 0, 1 10 -r 20
force {ld_alu_out} 0
force {ld_r} 1
force {data_in} 8'd1 0, 8'd2 20, 8'd3 40, 8'd4 60
force {ld_a} 1 0, 0 20
force {ld_b} 0 0, 1 20, 0 40
force {ld_c} 0 0, 1 40, 0 60
force {ld_x} 0 0, 1 60, 0 80

run 80 ns

force {resetn} 1
force {ld_r} 1
force {clk} 0 0, 1 10 -r 20
force {alu_select_a} 2'b00 0, 2'b10 20
force {alu_select_b} 2'b01 0, 2'b11 20
force {alu_op} 0 0, 1 20
run 40 ns

force {ld_alu_out} 1
force {ld_a} 1
force {ld_b} 1
run 20 ns






