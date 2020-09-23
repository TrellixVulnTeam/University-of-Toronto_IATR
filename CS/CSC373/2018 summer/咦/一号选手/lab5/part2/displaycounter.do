# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns displaycounter.v

# Load simulation using mux as the top level simulation module.
vsim displaycounter

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# First test case
# Set input values using the force command, signal names need to be in {} brackets.


force {SW[0]} 0
force {SW[1]} 0
force {CLOCK_50} 0
force {KEY[0]} 1
run 1ns
force {CLOCK_50} 1
run 1ns
force {KEY[0]} 0
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
force {CLOCK_50} 0
run 1ns
force {CLOCK_50} 1
run 1ns
