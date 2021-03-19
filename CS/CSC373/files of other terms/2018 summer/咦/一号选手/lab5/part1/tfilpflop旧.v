module tfilpflop (clock,reset, t,out);
    input clock,reset, t;
	output out;
    wire d,q;
    assign d = t & ^out | ^t & out;
    reg out;
	always @(reset)
     begin

		case (reset)
		1'b1: out = q;
		1'b0: out = 0;
    	endcase
	end


    filpflop f1(
    .reset_n(1),
    .clock(clock),
      .q(q),
      .d(d)
    );
endmodule


module filpflop (clock,q,reset_n, d);
    input clock, d,reset_n;
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