

module fulladder(LEDR, SW);
    input [9:0] SW;
    output [9:0] LEDR;

    fulladderr f0(
        .x(SW[2]),
        .y(SW[1]),
		  .cin(SW[0]),
        .cout(LEDR[1]),
        .s(LEDR[0])
        );
endmodule

module fulladderr(x, y, cin, cout,s);
    input x, y, cin; 
    output cout,s; 
  
    assign cout = x & y | x & cin | y & cin;
	 assign s = x ^ y ^ cin;
	 

endmodule

