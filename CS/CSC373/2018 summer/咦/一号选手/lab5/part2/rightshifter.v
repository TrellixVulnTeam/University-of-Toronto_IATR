module rightshifter (A,B, OUT);
	input [3:0] A;
	input [3:0] B;
	output [7:0] OUT;

    rightshifterr rs(
        .A(A),
        .B(B),
        .OUT(OUT)
        );


endmodule

module rightshifterr (A,B, OUT);
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