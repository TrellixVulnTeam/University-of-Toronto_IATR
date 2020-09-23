# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns rcadder.v

# Load simulation using mux as the top level simulation module.
vsim rcadder

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# First test case
# Set input values using the force command, signal names need to be in {} brackets.
force {SW[0]} 1 0ns, 1 10ns -repeat 40ns
force {SW[1]} 1 0ns, 1 10ns -repeat 40ns
force {SW[2]} 1 0ns, 1 10ns -repeat 40ns
force {SW[3]} 1 0ns, 1 10ns -repeat 40ns
force {SW[4]} 1 0ns, 1 10ns -repeat 40ns
force {SW[5]} 1 0ns, 1 10ns -repeat 40ns
force {SW[6]} 1 0ns, 1 10ns -repeat 40ns
force {SW[7]} 1 0ns, 1 10ns -repeat 40ns
force {SW[8]} 0 0ns, 1 10ns -repeat 40ns

run 70ns