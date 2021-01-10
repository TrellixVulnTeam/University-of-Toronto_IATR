module register (clock,reset_n,Q, D);
    input clock,reset_n;
    input [7:0] D;
	output [7:0] Q;


    filpflop f0(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[0]),
        .d(D[0])
        );
    filpflop f1(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[1]),
        .d(D[1])
        );
    filpflop f2(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[2]),
        .d(D[2])
        );
    filpflop f3(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[3]),
        .d(D[3])
        );
    filpflop f4(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[4]),
        .d(D[4])
        );
    filpflop f5(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[5]),
        .d(D[5])
        );
    filpflop f6(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[6]),
        .d(D[6])
        );
    filpflop f7(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[7]),
        .d(D[7])
        );
endmodule





module filpflop (clock,reset_n,q, d);
    input clock,reset_n, d;
	output q;

    reg q;
    always @(posedge clock) // Triggered every time clock rises
                            // Note that clock is not a keyword
    begin
           if (reset_n == 1'b0) // When reset_n is 0
                                // Note this is tested on every rising clock edge
               q <= 0 ;         // Set q to 0 .
                                // Note that the assignmen t use s <= instead of =
           else                 // When reset_n is not 0
               q <= d ;         // Store the value of d in q
    end
endmodule