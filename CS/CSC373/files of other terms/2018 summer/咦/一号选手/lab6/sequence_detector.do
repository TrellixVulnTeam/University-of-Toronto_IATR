# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns sequence_detector.v

# Load simulation using mux as the top level simulation module.
vsim sequence_detector

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}



# First test case 1111
force {KEY[0]} 1

force {SW[0]} 0
force {SW[1]} 0

# Run simulation for a few ns.
run 10ns


force {KEY[0]} 0
run 10ns
#1
force {KEY[0]} 1

force {SW[0]} 1
force {SW[1]} 1

# Run simulation for a few ns.
run 10ns


force {KEY[0]} 0
run 10ns

#11
force {KEY[0]} 1
force {SW[0]} 1
force {SW[1]} 1
run 10ns
force {KEY[0]} 0
run 10ns

#111
force {KEY[0]} 1
force {SW[0]} 1
force {SW[1]} 1
run 10ns
force {KEY[0]} 0
run 10ns

#1111
force {KEY[0]} 1
force {SW[0]} 1
force {SW[1]} 1
run 10ns
force {KEY[0]} 0
run 10ns

#Second 1101
#reset
force {KEY[0]} 1
force {SW[0]} 0
force {SW[1]} 0
run 10ns
force {KEY[0]} 0
run 10ns
#1
force {KEY[0]} 1

force {SW[0]} 1
force {SW[1]} 1

# Run simulation for a few ns.
run 10ns


force {KEY[0]} 0
run 10ns

#11
force {KEY[0]} 1
force {SW[0]} 1
force {SW[1]} 1
run 10ns
force {KEY[0]} 0
run 10ns

#110
force {KEY[0]} 1
force {SW[0]} 1
force {SW[1]} 0
run 10ns
force {KEY[0]} 0
run 10ns

#1101
force {KEY[0]} 1
force {SW[0]} 1
force {SW[1]} 1
run 10ns
force {KEY[0]} 0
run 10ns