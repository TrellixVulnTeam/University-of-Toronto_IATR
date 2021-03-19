# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns shifter.v

# Load simulation using mux as the top level simulation module.
vsim shifter

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# First test case
# Set input values using the force command, signal names need to be in {} brackets.
force {clock} 0
force {reset_n} 1
force {d[0]} 1
force {d[1]} 1
force {d[2]} 1
force {d[3]} 1
force {d[4]} 1
force {d[5]} 1
force {d[6]} 1
force {d[7]} 1
force {d[8]} 1
force {d[9]} 1
force {d[10]} 1
force {d[11]} 1
force {d[12]} 1
force {d[13]} 1

force {par_load} 1
force {enable} 1

run 1ns
force {clock} 1
run 1ns
force {clock} 0
force {par_load} 0
force {enable} 1
run 1ns

force {clock} 1
run 1ns
force {clock} 0
run 1ns

force {clock} 1
run 1ns
force {clock} 0
run 1ns

force {clock} 1
run 1ns
force {clock} 0
run 1ns

force {clock} 1
run 1ns
force {clock} 0
run 1ns

force {clock} 1
run 1ns
force {clock} 0
run 1ns

force {clock} 1
run 1ns
force {clock} 0
run 1ns

