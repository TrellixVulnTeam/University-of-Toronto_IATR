

module shifter (clock,reset_n,d,par_load,enable,OUT);

    wire [13:0] QQ;
    output [13:0] OUT;
    input [13:0] d ;                  // Declare d
    input clock;                     // Declare clock
    input reset_n;                   // Declare reset_n
    input par_load, enable;          // Declare par_load and enable
    reg [13:0] q;                    // Declare q
    always @(posedge clock)         // Triggered every time clock rises
    begin
        if (reset_n == 1'b0)        // When reset_n is 0
            q <= 0 ;                // Set q to 0
        else if ( par_load == 1'b1) // Check if parallel load
            q <= d ;                // Load d
        else if ( enable == 1'b1 )  // Increment q only when enable is 1
            q <= QQ ; // Increment q

    end

    assign OUT[13:0] = q[13:0];
    shifting s4(
            .N(q),
            .Q(QQ)
            );


endmodule

module shifting (N,Q);
	input [13:0]N;
	output [13:0] Q;
    assign Q[13:1] = N[12:0];
    assign Q[0] = 0;


endmodule
