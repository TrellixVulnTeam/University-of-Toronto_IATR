module alu (SW, LEDR,KEY,HEX0,HEX1,HEX2,HEX3,HEX4,HEX5,RGout);
	input [9:0] SW;
	input [2:0] KEY;
	wire [7:0] ALUout;
	output [7:0] RGout;
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
	wire G1,G2,G3,G4,G5,G6,G7,G0;
	wire H1,H2,H3,H4,H5,H6,H7,H0;
	wire [3:0] A;
	wire [3:0] B;
	wire [3:0] AplusB;
	wire [7:0] leftout;
	wire [7:0] rightout;
    wire [3:0] AmultB;
    assign B[3:0] = ALUout[3:0];
    assign A[3:0] = SW[3:0];
	reg out0;
	always @(SW)
     begin

		case (SW[7:5])
		3'b000: out0 = A0;
		3'b001: out0 = B0;
		3'b010: out0 = C0;
		3'b011: out0 = D0;
		3'b100: out0 = E0;
		3'b101: out0 = F0;
		3'b110: out0 = G0;
		3'b111: out0 = H0;
		default: out0 = 0;
    	endcase
	end
	reg out1;
	always @(SW)
     begin

		case (SW[7:5])
		3'b000: out1 = A1;
		3'b001: out1 = B1;
		3'b010: out1 = C1;
		3'b011: out1 = D1;
		3'b100: out1 = E1;
		3'b101: out1 = F1;
		3'b110: out1 = G1;
		3'b111: out1 = H1;
		default: out1 = 0;
    	endcase
	end
	reg out2;
	always @(SW)
     begin

		case (SW[7:5])
		3'b000: out2 = A2;
		3'b001: out2 = B2;
		3'b010: out2 = C2;
		3'b011: out2 = D2;
		3'b100: out2 = E2;
		3'b101: out2 = F2;
		3'b110: out2 = G2;
		3'b111: out2 = H2;
		default: out2 = 0;
    	endcase
	end
	reg out3;
	always @(SW)
     begin

		case (SW[7:5])
		3'b000: out3 = A3;
		3'b001: out3 = B3;
		3'b010: out3 = C3;
		3'b011: out3 = D3;
		3'b100: out3 = E3;
		3'b101: out3 = F3;
		3'b110: out3 = G3;
		3'b111: out3 = H3;
		default: out3 = 0;
    	endcase
	end
	reg out4;
	always @(SW)
     begin

		case (SW[7:5])
		3'b011: out4 = D4;
		3'b100: out4 = E4;
		3'b101: out4 = F4;
		3'b110: out4 = G4;
		default: out4 = 0;
    	endcase
	end
	reg out5;
	always @(SW)
     begin

		case (SW[7:5])
		3'b011: out5 = D5;
		3'b100: out5 = E5;
		3'b101: out5 = F5;
		3'b110: out5 = G5;
		default: out5 = 0;
    	endcase
	end
	reg out6;
	always @(SW)
     begin

		case (SW[7:5])
		3'b011: out6 = D6;
		3'b100: out6 = E6;
		3'b101: out6 = F6;
		3'b110: out6 = G6;
		default: out6 = 0;
    	endcase
	end
	reg out7;
	always @(SW)
     begin

		case (SW[7:5])
		3'b011: out7 = D7;
		3'b100: out7 = E7;
		3'b101: out7 = F7;
		3'b110: out7 = G7;
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
					  .b0(A[0]),
					  .b1(A[1]),
					  .b2(A[2]),
					  .b3(A[3]),
					  .cin(0),
					  .s0(A0),
					  .s1(A1),
					  .s2(A2),
					  .s3(A3),
					  .cout(A4)
					);
      rcadderr r1(
                  .a0(A[0]),
                  .a1(A[1]),
                  .a2(A[2]),
                  .a3(A[3]),
                  .b0(B[0]),
                  .b1(B[1]),
                  .b2(B[2]),
                  .b3(B[3]),
                  .cin(0),
                  .s0(B0),
                  .s1(B1),
                  .s2(B2),
                  .s3(B3),
                  .cout(B4)
                );


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
    assign LEDR[0] = RGout[0];
    assign LEDR[1] = RGout[1];
    assign LEDR[2] = RGout[2];
    assign LEDR[3] = RGout[3];
    assign LEDR[4] = RGout[4];
    assign LEDR[5] = RGout[5];
    assign LEDR[6] = RGout[6];
    assign LEDR[7] = RGout[7];

    assign F0 = leftout[0];
    assign F1 = leftout[1];
    assign F2 = leftout[2];
    assign F3 = leftout[3];
    assign F4 = leftout[4];
    assign F5 = leftout[5];
    assign F6 = leftout[6];
    assign F7 = leftout[7];

    assign G0 = rightout[0];
    assign G1 = rightout[1];
    assign G2 = rightout[2];
    assign G3 = rightout[3];
    assign G4 = rightout[4];
    assign G5 = rightout[5];
    assign G6 = rightout[6];
    assign G7 = rightout[7];

    assign AmultB[3:0] = A[3:0] *B[3:0];
    assign H0 = AmultB[0];
    assign H1 = AmultB[1];
    assign H2 = AmultB[2];
    assign H3 = AmultB[3];


    rightshifter rsss0(
        .A(A),
        .B(B),
        .OUT(rightout)
        );

    leftshifter lsss0(
        .A(A),
        .B(B),
        .OUT(leftout)
        );




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
    hexalloff u1(
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
    hexalloff u2(
        .u(0),
        .v(0),
		  .w(0),
        .x(0),
        .HEX00(HEX2[0]),
		  .HEX01(HEX2[1]),
		  .HEX02(HEX2[2]),
		  .HEX03(HEX2[3]),
		  .HEX04(HEX2[4]),
		  .HEX05(HEX2[5]),
		  .HEX06(HEX2[6])
        );
    hexalloff u3(
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
        .u(RGout[3]),
        .v(RGout[2]),
		  .w(RGout[1]),
        .x(RGout[0]),
        .HEX00(HEX4[0]),
		  .HEX01(HEX4[1]),
		  .HEX02(HEX4[2]),
		  .HEX03(HEX4[3]),
		  .HEX04(HEX4[4]),
		  .HEX05(HEX4[5]),
		  .HEX06(HEX4[6])
        );
    decoderr u5(
        .u(RGout[7]),
        .v(RGout[6]),
		  .w(RGout[5]),
        .x(RGout[4]),
        .HEX00(HEX5[0]),
		  .HEX01(HEX5[1]),
		  .HEX02(HEX5[2]),
		  .HEX03(HEX5[3]),
		  .HEX04(HEX5[4]),
		  .HEX05(HEX5[5]),
		  .HEX06(HEX5[6])
        );

    register rgs0(
        .clock(KEY[0]),
        .reset_n(SW[9]),
		.D(ALUout),
        .Q(RGout)
        );
endmodule

module register (clock,reset_n,Q, D);
    input clock,reset_n;
    input [7:0] D;
	output [7:0] Q;


    filpflop f0(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[0]),
        .d(D[0])
        );
    filpflop f1(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[1]),
        .d(D[1])
        );
    filpflop f2(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[2]),
        .d(D[2])
        );
    filpflop f3(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[3]),
        .d(D[3])
        );
    filpflop f4(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[4]),
        .d(D[4])
        );
    filpflop f5(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[5]),
        .d(D[5])
        );
    filpflop f6(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[6]),
        .d(D[6])
        );
    filpflop f7(
        .clock(clock),
        .reset_n(reset_n),
		.q(Q[7]),
        .d(D[7])
        );
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

module leftshifter (A,B, OUT);
	input [3:0] A;
	input [3:0] B;
	output [7:0] OUT;

	reg out0;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out0 = B[0];
		default: out0 = 0;
   	endcase
	end
    assign OUT[0] = out0;

	reg out1;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out1 = B[1];
		4'b0001: out1 = B[0];
		default: out1 = 0;
   	endcase
	end
    assign OUT[1] = out1;

    reg out2;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out2 = B[2];
		4'b0001: out2 = B[1];
		4'b0010: out2 = B[0];
		default: out2 = 0;
   	endcase
	end
    assign OUT[2] = out2;

	reg out3;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out3 = B[3];
		4'b0001: out3 = B[2];
		4'b0010: out3 = B[1];
		4'b0011: out3 = B[0];
		default: out3 = 0;
   	endcase
	end
    assign OUT[3] = out3;
    assign OUT[7] = 0;
    assign OUT[6] = 0;
    assign OUT[5] = 0;
    assign OUT[4] = 0;


endmodule

module rightshifter (A,B, OUT);
	input [3:0] A;
	input [3:0] B;
	output [7:0] OUT;

	reg out0;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out0 = B[0];
		4'b0001: out0 = B[1];
		4'b0010: out0 = B[2];
		4'b0011: out0 = B[3];
		default: out0 = 0;
   	endcase
	end
    assign OUT[0] = out0;

	reg out1;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out1 = B[1];
		4'b0001: out1 = B[2];
		4'b0010: out1 = B[3];
		default: out1 = 0;
   	endcase
	end
    assign OUT[1] = out1;

    reg out2;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out2 = B[2];
		4'b0001: out2 = B[3];
		default: out2 = 0;
   	endcase
	end
    assign OUT[2] = out2;

	reg out3;
	always @(A)
    begin
        case (A[3:0])
		4'b0000: out3 = B[3];
		default: out3 = 0;
   	endcase
	end
    assign OUT[3] = out3;
    assign OUT[7] = 0;
    assign OUT[6] = 0;
    assign OUT[5] = 0;
    assign OUT[4] = 0;


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

module hexalloff(u,v,w,x,HEX00,HEX01,HEX02,HEX03,HEX04,HEX05,HEX06);
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
    assign HEX00 = 1 ;
	 assign HEX01 = 1 ;
	 assign HEX02 = 1;
	 assign HEX03 = 1;
	 assign HEX04 = 1 ;
	 assign HEX05 = 1 ;
	 assign HEX06 = 1 ;

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