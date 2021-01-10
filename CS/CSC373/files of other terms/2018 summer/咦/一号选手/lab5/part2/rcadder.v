

module rcadder(LEDR, SW);
    input [9:0] SW;
    output [9:0] LEDR;

    rcadderr r0(
        .a0(SW[0]),
		  .a1(SW[1]),
		  .a2(SW[2]),
		  .a3(SW[3]),
		  .b0(SW[4]),
		  .b1(SW[5]),
		  .b2(SW[6]),
		  .b3(SW[7]),
		  .cin(SW[8]),
		  .s0(LEDR[0]),
		  .s1(LEDR[1]),
		  .s2(LEDR[2]),
		  .s3(LEDR[3]),
		  .cout(LEDR[4])
        );
endmodule

module fulladderr(x, y, cin, cout,s);
    input x, y, cin; 
    output cout,s; 
  
    assign cout = x & y | x & cin | y & cin;
	 assign s = x ^ y ^ cin;
	 

endmodule



module rcadderr(a1,a2,a3,a0,b1,b2,b3,b0,cin,s0,s1,s2,s3,cout);
    input a1,a2,a3,a0,b1,b2,b3,b0,cin; 
	 wire c1,c2,c3;
	 output s0,s1,s2,s3,cout; 
	 
	 fulladderr f1(
	      .x(a0),
			.y(b0),
			.cin(cin),
			.s(s0),
			.cout(c1)
	 );
    fulladderr f2(
	      .x(a1),
			.y(b1),
			.cin(c1),
			.s(s1),
			.cout(c2)
	 );
	 fulladderr f3(
	      .x(a2),
			.y(b2),
			.cin(c2),
			.s(s2),
			.cout(c3)
	 );
	 fulladderr f4(
	      .x(a3),
			.y(b3),
			.cin(c3),
			.s(s3),
			.cout(cout)
	 );

endmodule