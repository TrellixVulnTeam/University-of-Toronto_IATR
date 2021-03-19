
module counter (SW, LEDR,KEY,HEX0,HEX1);
    input [9:0] SW;
	input [2:0] KEY;
	output [9:0] LEDR;
	output [6:0] HEX0;
	output [6:0] HEX1;
    wire [7:0] Q;
    wire [6:0] T;
    wire Enable, Clear_b,Clock;
    assign Enable = SW[1];
    assign Clear_b = SW[0];
    assign Clock = KEY[0];
    assign LEDR[0]= Q[7];
    assign LEDR[1]= Q[6];
    assign LEDR[2]= Q[5];
    assign LEDR[3]= Q[4];
    assign LEDR[4]= Q[3];
    assign LEDR[5]= Q[2];
    assign LEDR[6]= Q[1];
    assign LEDR[7]= Q[0];
    assign T[6] = Q[7] & Enable;
    assign T[5] = Q[6] & T[6];
    assign T[4] = Q[5] & T[5];
    assign T[3] = Q[4] & T[4];
    assign T[2] = Q[3] & T[3];
    assign T[1] = Q[2] & T[2];
    assign T[0] = Q[1] & T[1];
    tfilpflop t7(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(Enable),
        .q(Q[7])
        );
    tfilpflop t6(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[6]),
        .q(Q[6])
        );
    tfilpflop t5(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[5]),
        .q(Q[5])
        );
    tfilpflop t4(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[4]),
        .q(Q[4])
        );
    tfilpflop t3(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[3]),
        .q(Q[3])
        );
    tfilpflop t2(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[2]),
        .q(Q[2])
        );
    tfilpflop t1(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[1]),
        .q(Q[1])
        );
    tfilpflop t0(
        .clock(Clock),
        .clear_b(Clear_b),
        .t(T[0]),
        .q(Q[0])
        );

    decoderr u0(
        .u(Q[4]),
        .v(Q[5]),
		.w(Q[6]),
        .x(Q[7]),
        .HEX00(HEX0[0]),
		  .HEX01(HEX0[1]),
		  .HEX02(HEX0[2]),
		  .HEX03(HEX0[3]),
		  .HEX04(HEX0[4]),
		  .HEX05(HEX0[5]),
		  .HEX06(HEX0[6])
        );
    decoderr u1(
        .u(Q[0]),
        .v(Q[1]),
		.w(Q[2]),
        .x(Q[3]),
        .HEX00(HEX1[0]),
		  .HEX01(HEX1[1]),
		  .HEX02(HEX1[2]),
		  .HEX03(HEX1[3]),
		  .HEX04(HEX1[4]),
		  .HEX05(HEX1[5]),
		  .HEX06(HEX1[6])
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
	 assign HEX02 = ~u & ~v & w & ~x | u & v & ~x| u & v & w;
	 assign HEX03 = ~u & v & ~w & ~x | ~v & ~w & x | v & w & x | u & ~v & w & ~x ;
	 assign HEX04 = ~u & v & ~w | ~v & ~w & x | ~u & x ;
	 assign HEX05 = ~u & ~v & x | ~u & ~v & w | ~u & w & x | u & v & ~w & x ;
	 assign HEX06 = ~u & ~v & ~w | ~u & v & w & x | u & v & ~w & ~x ;

endmodule











module tfilpflop (clock,clear_b, t,q);
    output q;
    input t,clock,clear_b;
    reg q;
    initial
       begin
        q=1'b0;
       end
    always@(posedge clock, negedge clear_b)
    begin
        if(~clear_b)
           q <= 1'b0;
        else
            q <= (q & ~t)|(~q & t);
    end
endmodule
