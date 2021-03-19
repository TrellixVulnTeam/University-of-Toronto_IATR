
module smallrater (clk, enable,par_load,reset_n,out,QQ);
input clk;                     // Declare clock
input reset_n;                   // Declare reset_n
input par_load, enable;          // Declare par_load and enable
output out;
output [2:0] QQ;
    smallraterr u0(
        .d(3'b001),
        .clk(clk),
		  .reset_n(reset_n),
        .par_load(par_load),
        .enable(enable),
		  .out(out),
		  .QQ(QQ)
        );

endmodule








module smallraterr (d,clk, enable,par_load,reset_n,out,QQ);
input [2:0] d ;                  // Declare d
input clk;                     // Declare clock
input reset_n;                   // Declare reset_n
input par_load, enable;          // Declare par_load and enable
output out;
output [2:0] QQ;
reg [2:0] q;                    // Declare q
always @(posedge clk)         // Triggered every time clock rises
begin
    if (reset_n == 1'b0)        // When reset_n is 0
        q <= 0 ;                // Set q to 0
    else if ( par_load == 1'b1) // Check if parallel load
        q <= d ;                // Load d
    else if ( enable == 1'b1 )  // Increment q only when enable is 1
        begin
            if ( q == 3'b101 ) // When q is the maximum value for the counter
                q <= 0 ;        // Reset q into 0
            else                // When q is not the maximum value
                q <= q + 1'b1 ; // Increment q
        end
end
reg final;
always @(q)
begin
    case (q[2:0])
    3'b000: final = 1;
    default: final = 0;
endcase
end
assign out = final;
assign QQ[2:0] = q[2:0];
endmodule