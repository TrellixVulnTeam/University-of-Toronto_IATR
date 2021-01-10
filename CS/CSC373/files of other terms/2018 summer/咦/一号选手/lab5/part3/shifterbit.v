module shifterbit (load_val,in,shift,load_n, clk,reset_n,out);
    input load_val,in,shift,load_n, clk,reset_n;
	output out;
    wire m0out,m1out;
    mux m0(
        .s(shift),
        .x(out),
		.y(in),
        .out(m0out)
        );
    mux m1(
        .s(load_n),
        .x(load_val),
		.y(m0out),
        .out(m1out)
        );


    filpflop f0(
        .clock(clk),
        .reset_n(reset_n),
		.q(out),
        .d(m1out)
        );

endmodule



module mux (s,x,y, out);
	input s,x,y;
	output out;
	reg t; // target of assignment
	always @(s)
    begin

		case (s)
		1'b0: t = x;
		1'b1: t = y;

   	endcase
	end
    assign out = t;

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