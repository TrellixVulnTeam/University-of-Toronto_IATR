module alu (SW, LEDR,KEY,HEX0,HEX1,HEX2,HEX3,HEX4,HEX5,ALUout);
	input [9:0] SW;
	input [2:0] KEY;
	output [7:0] ALUout;
	output [9:0] LEDR;
	output [6:0] HEX0;
	output [6:0] HEX2;
	output [6:0] HEX1;
	output [6:0] HEX3;
	output [6:0] HEX4;
	output [6:0] HEX5;
	wire A1,A2,A3,A4,A5,A6,A7,A0;
	wire B1,B2,B3,B4,B5,B6,B7,B0;
	wire C1,C2,C3,C4,C5,C6,C7,C0;
	wire D1,D2,D3,D4,D5,D6,D7,D0;
	wire E1,E2,E3,E4,E5,E6,E7,E0;
	wire F1,F2,F3,F4,F5,F6,F7,F0;
	wire [3:0] A;
	wire [3:0] B;
	wire [3:0] AplusB;

	reg out0;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b000: out0 = A0;
		3'b001: out0 = B0;
		3'b010: out0 = C0;
		3'b011: out0 = D0;
		3'b100: out0 = E0;
		3'b101: out0 = F0;
		default: out0 = 0;
    	endcase
	end

	reg out1;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b000: out1 = A1;
		3'b001: out1 = B1;
		3'b010: out1 = C1;
		3'b011: out1 = D1;
		3'b100: out1 = E1;
		3'b101: out1 = F1;
		default: out1 = 0;
    	endcase
	end

	reg out2;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b000: out2 = A2;
		3'b001: out2 = B2;
		3'b010: out2 = C2;
		3'b011: out2 = D2;
		3'b100: out2 = E2;
		3'b101: out2 = F2;
		default: out2 = 0;
    	endcase
	end

	reg out3;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b000: out3 = A3;
		3'b001: out3 = B3;
		3'b010: out3 = C3;
		3'b011: out3 = D3;
		3'b100: out3 = E3;
		3'b101: out3 = F3;
		default: out3 = 0;
    	endcase
	end

	reg out4;
	always @(KEY)
     begin

		case (KEY[2:0])

		3'b011: out4 = D4;
		3'b100: out4 = E4;
		3'b101: out4 = F4;
		default: out4 = 0;
    	endcase
	end

	reg out5;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b011: out5 = D5;
		3'b100: out5 = E5;
		3'b101: out5 = F5;
		default: out5 = 0;
    	endcase
	end

	reg out6;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b011: out6 = D6;
		3'b100: out6 = E6;
		3'b101: out6 = F6;
		default: out6 = 0;
    	endcase
	end

	reg out7;
	always @(KEY)
     begin

		case (KEY[2:0])
		3'b011: out7 = D7;
		3'b100: out7 = E7;
		3'b101: out7 = F7;
		default: out7 = 0;
    	endcase
	end

	assign ALUout[0] = out0;
	assign ALUout[1] = out1;
	assign ALUout[2] = out2;
	assign ALUout[3] = out3;
	assign ALUout[4] = out4;
	assign ALUout[5] = out5;
	assign ALUout[6] = out6;
	assign ALUout[7] = out7;

      rcadderr r0(
					  .a0(1),
					  .a1(0),
					  .a2(0),
					  .a3(0),
					  .b0(SW[4]),
					  .b1(SW[5]),
					  .b2(SW[6]),
					  .b3(SW[7]),
					  .cin(0),
					  .s0(A0),
					  .s1(A1),
					  .s2(A2),
					  .s3(A3),
					  .cout(A4)
					);
					
      rcadderr r1(
                  .a0(SW[0]),
                  .a1(SW[1]),
                  .a2(SW[2]),
                  .a3(SW[3]),
                  .b0(SW[4]),
                  .b1(SW[5]),
                  .b2(SW[6]),
                  .b3(SW[7]),
                  .cin(0),
                  .s0(B0),
                  .s1(B1),
                  .s2(B2),
                  .s3(B3),
                  .cout(B4)
                );

    assign A[3:0] = SW[7:4];
    assign B[3:0] = SW[3:0];
    assign AplusB[3:0] = A[3:0] +B[3:0];
    assign C0 = AplusB[0];
    assign C1 = AplusB[1];
    assign C2 = AplusB[2];
    assign C3 = AplusB[3];
    assign D7 = SW[7]|SW[3];
    assign D6 = SW[6]|SW[2];
    assign D5 = SW[5]|SW[1];
    assign D4 = SW[4]|SW[0];
    assign D3 = SW[7]^SW[3];
    assign D2 = SW[6]^SW[2];
    assign D1 = SW[5]^SW[1];
    assign D0 = SW[4]^SW[0];
    assign E0 = SW[7]|SW[6]|SW[5]|SW[4]|SW[3]|SW[2]|SW[1]|SW[0];
    assign E1 = 0;
    assign E2 = 0;
    assign E3 = 0;
    assign E4 = 0;
    assign E5 = 0;
    assign E6 = 0;
    assign E7 = 0;
    assign F7 = SW[7];
    assign F6 = SW[6];
    assign F5 = SW[5];
    assign F4 = SW[4];
    assign F3 = SW[3];
    assign F2 = SW[2];
    assign F1 = SW[1];
    assign F0 = SW[0];
    assign LEDR[0] = ALUout[0];
    assign LEDR[1] = ALUout[1];
    assign LEDR[2] = ALUout[2];
    assign LEDR[3] = ALUout[3];
    assign LEDR[4] = ALUout[4];
    assign LEDR[5] = ALUout[5];
    assign LEDR[6] = ALUout[6];
    assign LEDR[7] = ALUout[7];

    decoderr u0(
        .u(SW[3]),
        .v(SW[2]),
		  .w(SW[1]),
        .x(SW[0]),
        .HEX00(HEX0[0]),
		  .HEX01(HEX0[1]),
		  .HEX02(HEX0[2]),
		  .HEX03(HEX0[3]),
		  .HEX04(HEX0[4]),
		  .HEX05(HEX0[5]),
		  .HEX06(HEX0[6])
        );

    decoderr u1(
        .u(0),
        .v(0),
		  .w(0),
        .x(0),
        .HEX00(HEX1[0]),
		  .HEX01(HEX1[1]),
		  .HEX02(HEX1[2]),
		  .HEX03(HEX1[3]),
		  .HEX04(HEX1[4]),
		  .HEX05(HEX1[5]),
		  .HEX06(HEX1[6])
        );

    decoderr u2(
        .u(SW[7]),
        .v(SW[6]),
		  .w(SW[5]),
        .x(SW[4]),
        .HEX00(HEX2[0]),
		  .HEX01(HEX2[1]),
		  .HEX02(HEX2[2]),
		  .HEX03(HEX2[3]),
		  .HEX04(HEX2[4]),
		  .HEX05(HEX2[5]),
		  .HEX06(HEX2[6])
        );

    decoderr u3(
        .u(0),
        .v(0),
		  .w(0),
        .x(0),
        .HEX00(HEX3[0]),
		  .HEX01(HEX3[1]),
		  .HEX02(HEX3[2]),
		  .HEX03(HEX3[3]),
		  .HEX04(HEX3[4]),
		  .HEX05(HEX3[5]),
		  .HEX06(HEX3[6])
        );

    decoderr u4(
        .u(ALUout[3]),
        .v(ALUout[2]),
		  .w(ALUout[1]),
        .x(ALUout[0]),
        .HEX00(HEX4[0]),
		  .HEX01(HEX4[1]),
		  .HEX02(HEX4[2]),
		  .HEX03(HEX4[3]),
		  .HEX04(HEX4[4]),
		  .HEX05(HEX4[5]),
		  .HEX06(HEX4[6])
        );

    decoderr u5(
        .u(ALUout[7]),
        .v(ALUout[6]),
		  .w(ALUout[5]),
        .x(ALUout[4]),
        .HEX00(HEX5[0]),
		  .HEX01(HEX5[1]),
		  .HEX02(HEX5[2]),
		  .HEX03(HEX5[3]),
		  .HEX04(HEX5[4]),
		  .HEX05(HEX5[5]),
		  .HEX06(HEX5[6])
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
