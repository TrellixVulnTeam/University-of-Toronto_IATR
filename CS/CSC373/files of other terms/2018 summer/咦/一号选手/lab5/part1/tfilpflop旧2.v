module tfilpflop (clock, t,reset,out);
    input clock, reset,t;
	output out;




    reg out;
    always @(posedge clock)

    begin
           if (reset == 1'b0) // When reset_n is 0
                                // Note this is tested on every rising clock edge
               out <= 0 ;         // Set q to 0 .
                                // Note that the assignmen t use s <= instead of =
           else                 // When reset_n is not 0
               out <= ^out ;         // Store the value of d in q
    end


endmodule

