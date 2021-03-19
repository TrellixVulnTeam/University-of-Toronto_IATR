# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns filpflop.v

# Load simulation using mux as the top level simulation module.
vsim filpflop

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# First test case
# Set input values using the force command, signal names need to be in {} brackets.
force {clock} 0
force {reset_n} 1
force {d} 1

run 10ns

force {clock} 1
force {reset_n} 1
force {d} 1

run 10ns

force {clock} 0
force {reset_n} 0
force {d} 0

run 10ns

force {clock} 1
force {reset_n} 1
force {d} 0

run 10ns


