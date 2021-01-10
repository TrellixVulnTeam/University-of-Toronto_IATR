# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns register.v

# Load simulation using mux as the top level simulation module.
vsim register

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# First test case
# Set input values using the force command, signal names need to be in {} brackets.
force {clock} 0
force {reset_n} 1
force {D[6]} 1
force {D[5]} 1
force {D[4]} 1
force {D[3]} 1
force {D[2]} 1
force {D[1]} 1
force {D[0]} 1
force {D[7]} 1



run 10ns

force {clock} 1
force {reset_n} 1
force {D[6]} 1
force {D[5]} 1
force {D[4]} 1
force {D[3]} 1
force {D[2]} 1
force {D[1]} 1
force {D[0]} 1
force {D[7]} 1

run 10ns

force {clock} 0
force {reset_n} 0
force {D[6]} 0
force {D[5]} 0
force {D[4]} 0
force {D[3]} 0
force {D[2]} 0
force {D[1]} 0
force {D[0]} 0
force {D[7]} 0

run 10ns

force {clock} 1
force {reset_n} 1
force {D[6]} 0
force {D[5]} 0
force {D[4]} 0
force {D[3]} 0
force {D[2]} 0
force {D[1]} 0
force {D[0]} 0
force {D[7]} 0

run 10ns


