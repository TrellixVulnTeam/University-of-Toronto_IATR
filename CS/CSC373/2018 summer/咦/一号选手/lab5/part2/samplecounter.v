wire [3:0] d ;                  // Declare d
wire clock;                     // Declare clock
wire reset_n;                   // Declare reset_n
wire par_load, enable;          // Declare par_load and enable
reg [3:0] q;                    // Declare q
always @(posedge clock)         // Triggered every time clock rises
begin
    if (reset_n == 1'b0)        // When reset_n is 0
        q <= 0 ;                // Set q to 0
    else if ( par_load == 1'b1) // Check if parallel load
        q <= d ;                // Load d
    else if ( enable == 1'b1 )  // Increment q only when enable is 1
        begin
            if ( q == 4'b1111 ) // When q is the maximum value for the counter
                q <= 0 ;        // Reset q into 0
            else                // When q is not the maximum value
                q <= q + 1'b1 ; // Increment q
        end
end