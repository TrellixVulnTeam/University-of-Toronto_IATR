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