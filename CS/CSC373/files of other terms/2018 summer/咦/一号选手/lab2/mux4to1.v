//SW[2:0] data inputs
//SW[9] select signal

//LEDR[0] output display

module mux(LEDR, SW);
    input [9:0] SW;
    output [9:0] LEDR;

    mux4to1 u0(
        .u(SW[0]),
        .v(SW[1]),
		  .w(SW[2]),
        .x(SW[3]),
		  .s1(SW[8]),
        .s2(SW[9]),
        .m(LEDR[0])
        );
endmodule

module mux2to1(x, y, s, m);
    input x; //selected when s is 0
    input y; //selected when s is 1
    input s; //select signal
    output m; //output
  
    assign m = s & y | ~s & x;
    // OR
    // assign m = s ? y : x;

endmodule


module mux4to1(u,v,w,x,s1,s2,m);
    input u; //selected when s1 is 0 and s2 is 0
    input v; //selected when s1 is 0 and s2 is 1
	 input w; //selected when s1 is 1 and s2 is 0
    input x; //selected when s1 is 1 and s2 is 1
    input s1; //select signal # 1
	 input s2; //select signal # 2
	 wire A;
	 wire B;
	 output m; //output
	 
	 mux2to1 m1(
	      .x(u),
			.y(w),
			.s(s1),
			.m(A)
	 );
	 mux2to1 m2(
	      .x(v),
			.y(x),
			.s(s1),
			.m(B)
	 );
	 mux2to1 m3(
	      .x(A),
			.y(B),
			.s(s2),
			.m(m)
	 );
endmodule