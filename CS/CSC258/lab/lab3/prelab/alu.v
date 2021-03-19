module alu(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5);
	input[7:0] SW;
	input[2:0] KEY;
	output[7:0] LEDR;
	output[6:0] HEX0;
	output[6:0] HEX1;
	output[6:0] HEX2;
	output[6:0] HEX3;
	output[6:0] HEX4;
	output[6:0] HEX5;

	wire[7:0] Case0;
	wire[7:0] Case1;
	wire[7:0] Case2;
	wire[7:0] Case3;
	wire[7:0] Case4;
	wire[7:0] Case5;

	reg[7:0] Out;

	ripple u0 (
		.A(SW[7:4]),
		.B(4'b0001),
		.Sum(Case0[7:0])
	);

	ripple u1 (
		.A(SW[7:4]),
		.B(SW[3:0]),
		.Sum(Case1[7:0])
	);

	verisum u2 (
		.A(SW[7:4]),
		.B(SW[3:0]),
		.Sum(Case2[7:0])
	);

	xororor u3 (
		.A(SW[7:4]),
		.B(SW[3:0]),
		.Result(Case3[7:0])
	);

	reductionor u4 (
		.A(SW[7:4]),
		.B(SW[3:0]),
		.Result(Case4[7:0])
	);

	concat u5 (
		.A(SW[7:4]),
		.B(SW[3:0]),
		.Result(Case5[7:0])
	);


	always @(*)
	begin
		case(KEY[2:0])
			3'b000: Out = Case0; // case 0
			3'b001: Out = Case1; // case 1
			3'b100: Out = Case2; // case 2
			3'b101: Out = Case3; // case 3
			3'b010: Out = Case4; // case 4
			3'b011: Out = Case5; //case 5
			default: Out = 8'b00000000; //default case
		endcase
	end

	assign LEDR = Out;

	sevenseg u6 (
		.Data(SW[3:0]),
		.Display(HEX0[6:0])
	);

	sevenseg u7 (
		.Data(SW[7:4]),
		.Display(HEX2[6:0])
	);

	sevenseg u8 (
		.Data(Out[3:0]),
		.Display(HEX4[6:0])
	);

	sevenseg u9 (
		.Data(Out[7:4]),
		.Display(HEX5[6:0])
	);

	assign HEX1[6:0] = 4'b0000;
	assign HEX3[6:0] = 4'b0000;

endmodule


module concat(A, B, Result);
	input[3:0] A;
	input[3:0] B;
	output[7:0] Result;

	assign Result[7:0] = {A, B};

endmodule


module reductionor(A, B, Result);
	input[3:0] A;
	input[3:0] B;
	output[7:0] Result;

	assign Result[0] = | {A, B};
	assign Result[7:1] = 7'b0000000;

endmodule

module xororor(A, B, Result);
	input[3:0] A;
	input[3:0] B;
	output[7:0] Result;

	assign Result[3:0] = A^B;
	assign Result[7:4] = A|B;
endmodule



module verisum(A, B, Sum);
	input[3:0] A;
	input[3:0] B;
	output[7:0] Sum;

	assign Sum[3:0] = A + B;
	assign Sum[7:4] = 4'b0000;
endmodule


module ripple(A, B, Sum);
	input[3:0] A;
	input[3:0] B;
	output[7:0] Sum;
	wire dummy;

	wire w01;
	wire w12;
	wire w23;

	full_adder u0 (
		.sum(Sum[0]),
		.cout(w01),
		.a(A[0]),
		.b(B[0]),
		.cin(1'b0)
	);

	full_adder u1 (
		.sum(Sum[1]),
		.cout(w12),
		.a(A[1]),
		.b(B[1]),
		.cin(w01)
	);

	full_adder u2 (
		.sum(Sum[2]),
		.cout(w23),
		.a(A[2]),
		.b(B[2]),
		.cin(w12)
	);

	full_adder u3 (
		.sum(Sum[3]),
		.cout(dummy),
		.a(A[3]),
		.b(B[3]),
		.cin(w23)
	);

	assign Sum[7:4] = 4'b0000;

endmodule


module full_adder(sum, cout, a, b, cin);
	output sum, cout;
	input a, b, cin;

	assign sum = a^b^cin;
	assign cout = (a&b)|(cin&(a^b));
endmodule


module sevenseg (Display, Data);
	input[3:0] Data;
	output[6:0] Display;

	assign Display[0] = ~Data[3] & ~Data[2] & ~Data[1] &  Data[0] |
			 ~Data[3] &  Data[2] & ~Data[1] & ~Data[0] |
			  Data[3] &  Data[2] & ~Data[1] &  Data[0] |
			  Data[3] & ~Data[2] &  Data[1] &  Data[0];

	assign Display[1] = ~Data[3] &  Data[2] & ~Data[1] &  Data[0] |
			  Data[3] &  Data[2] & ~Data[1] & ~Data[0] |
			  Data[3] &           Data[1] &  Data[0] |
			           Data[2] &  Data[1] & ~Data[0];

	assign Display[2] =  Data[3] &  Data[2] & ~Data[1] & ~Data[0] |
			 ~Data[3] & ~Data[2] &  Data[1] & ~Data[0] |
			  Data[3] &  Data[2] &  Data[1];


	assign Display[3] = ~Data[3] &  Data[2] & ~Data[1] & ~Data[0] |
			          ~Data[2] & ~Data[1] &  Data[0] |
			           Data[2] &  Data[1] &  Data[0] |
			  Data[3] & ~Data[2] &  Data[1] & ~Data[0];

	assign Display[4] = ~Data[3] &                    Data[0] |
			 ~Data[3] &  Data[2] & ~Data[1]          |
			          ~Data[2] & ~Data[1] &  Data[0];


	assign Display[5] = ~Data[3] & ~Data[2]          &  Data[0] |
			 ~Data[3] & ~Data[2] &  Data[1]          |
			 ~Data[3] &           Data[1] &  Data[0] |
			  Data[3] &  Data[2] & ~Data[1] &  Data[0];

	assign Display[6] = ~Data[3] & ~Data[2]  & ~Data[1]         |
			 ~Data[3] &  Data[2] &  Data[1] &  Data[0] |
			  Data[3] &  Data[2] & ~Data[1] & ~Data[0];

endmodule
