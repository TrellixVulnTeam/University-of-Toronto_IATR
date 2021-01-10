module decoder(HEX0, SW);
    input [9:0] SW;
    output [6:0] HEX0;

    decoderr u0(
        .u(SW[0]),
        .v(SW[1]),
		  .w(SW[2]),
        .x(SW[3]),
        .HEX00(HEX0[0]),
		  .HEX01(HEX0[1]),
		  .HEX02(HEX0[2]),
		  .HEX03(HEX0[3]),
		  .HEX04(HEX0[4]),
		  .HEX05(HEX0[5]),
		  .HEX06(HEX0[6])
        );
endmodule


module decoderr(u,v,w,x,HEX00,HEX01,HEX02,HEX03,HEX04,HEX05,HEX06);
    input u; 
    input v; 
	 input w; 
    input x; 
	 output HEX00;
	 output HEX01;
	 output HEX02;
	 output HEX03;
	 output HEX04;
	 output HEX05;
	 output HEX06;	 
    assign HEX00 = ~u & ~v & ~w &x | ~u & v & ~w & ~x| u & ~v & w & x | u & v & ~w & x ;
	 assign HEX01 = ~u & v & ~w & x | u & w & x | u & v & ~x | v & w & ~x ;
	 assign HEX02 = u & v & ~x | ~v & w & ~x;
	 assign HEX03 = ~u & v & ~w & ~x | ~v & ~w & x | v & w & x | u & ~v & w & ~x ;
	 assign HEX04 = ~u & v & ~w | ~v & ~w & x | ~u & x ;
	 assign HEX05 = ~u & ~v & x | ~u & ~v & w | ~u & w & x | u & v & ~w & x ;
	 assign HEX06 = ~u & ~v & ~w | ~u & v & w & x | u & v & ~w & ~x ;

endmodule

