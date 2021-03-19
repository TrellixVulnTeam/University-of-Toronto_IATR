# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns poly_function.v

# Load simulation using mux as the top level simulation module.
vsim fpga_top

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}



# Reset
force {CLOCK_50} 1
force {KEY[0]} 0




# Run simulation for a few ns.
run 10ns

force {CLOCK_50} 0

run 10ns

#Load A
force {CLOCK_50} 1 
force {KEY[0]} 1
force {KEY[1]} 0

force {SW[0]} 1
force {SW[1]} 1
force {SW[2]} 0
force {SW[3]} 0

force {SW[4]} 0
force {SW[5]} 0
force {SW[6]} 0
force {SW[7]} 0
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
force {KEY[1]} 1
run 10ns
force {CLOCK_50} 0
run 10ns
#Load B
force {CLOCK_50} 1 
force {KEY[0]} 1
force {KEY[1]} 0

force {SW[0]} 1
force {SW[1]} 1
force {SW[2]} 1
force {SW[3]} 0

force {SW[4]} 0
force {SW[5]} 0
force {SW[6]} 0
force {SW[7]} 0
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
force {KEY[1]} 1
run 10ns
force {CLOCK_50} 0
run 10ns
#Load C
force {CLOCK_50} 1 
force {KEY[0]} 1
force {KEY[1]} 0

force {SW[0]} 1
force {SW[1]} 0
force {SW[2]} 1
force {SW[3]} 0

force {SW[4]} 0
force {SW[5]} 0
force {SW[6]} 0
force {SW[7]} 0
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
force {KEY[1]} 1
run 10ns
force {CLOCK_50} 0
run 10ns


#Load X
force {CLOCK_50} 1 
force {KEY[0]} 1
force {KEY[1]} 0

force {SW[0]} 0
force {SW[1]} 1
force {SW[2]} 0
force {SW[3]} 0

force {SW[4]} 0
force {SW[5]} 0
force {SW[6]} 0
force {SW[7]} 0
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
force {KEY[1]} 1
run 10ns
force {CLOCK_50} 0
run 10ns

#Load Result

force {CLOCK_50} 1 
force {KEY[0]} 1
force {KEY[1]} 0


run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
force {KEY[1]} 1
run 10ns
force {CLOCK_50} 0
run 10ns
#run few more clock cycles
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns
force {CLOCK_50} 1
run 10ns
force {CLOCK_50} 0
run 10ns