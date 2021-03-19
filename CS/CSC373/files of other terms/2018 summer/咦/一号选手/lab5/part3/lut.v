module lut (SW, Q);
	input [2:0] SW;
	output [13:0] Q;
	reg out0;
	always @(*)
    begin

		case (SW[2:0])
		default: out0 = 0;
   	endcase
	end
	reg out1;
	always @(*)
    begin

		case (SW[2:0])
		3'b110: out1 = 1;
		default: out1 = 0;
   	endcase
	end
	reg out2;
	always @(*)
    begin

		case (SW[2:0])
		3'b110: out2 = 1;
		default: out2 = 0;
   	endcase
	end
	reg out3;
	always @(*)
    begin

		case (SW[2:0])
		3'b101: out3 = 1;
		3'b110: out3 = 1;
		3'b111: out3 = 1;
		default: out3 = 0;
   	endcase
	end
	reg out4;
	always @(*)
    begin

		case (SW[2:0])
		3'b101: out4 = 1;
		default: out4 = 0;
   	endcase
	end
	reg out5;
	always @(*)
    begin

		case (SW[2:0])
		3'b011: out5 = 1;
		3'b100: out5 = 1;
		3'b101: out5 = 1;
		3'b110: out5 = 1;
		3'b111: out5 = 1;
		default: out5 = 0;
   	endcase
	end
	reg out6;
	always @(*)
    begin

		case (SW[2:0])
		3'b011: out6 = 1;
		3'b100: out6 = 1;
		3'b110: out6 = 1;
		default: out6 = 0;
   	endcase
	end
	reg out7;
	always @(*)
    begin

		case (SW[2:0])
		3'b010: out7 = 1;
		3'b011: out7 = 1;
		3'b100: out7 = 1;
		3'b101: out7 = 1;
		3'b110: out7 = 1;
		3'b111: out7 = 1;
		default: out7 = 0;
   	endcase
	end
    reg out8;
	always @(*)
    begin

		case (SW[2:0])
		3'b010: out8 = 1;
		3'b111: out8 = 1;
		default: out8 = 0;
   	endcase
	end
	reg out9;
	always @(*)
    begin

		case (SW[2:0])
		3'b000: out9 = 1;
		3'b010: out9 = 1;
		3'b011: out9 = 1;
		3'b100: out9 = 1;
		3'b101: out9 = 1;
		3'b110: out9 = 1;
		3'b111: out9 = 1;
		default: out9 = 0;
   	endcase
	end
    reg out10;
	always @(*)
    begin

		case (SW[2:0])
		3'b100: out10 = 1;
		default: out10 = 0;
   	endcase
	end
	reg out11;
	always @(*)
    begin

		case (SW[2:0])
		default: out11 = 1;
   	endcase
	end
    reg out12;
	always @(*)
    begin

		case (SW[2:0])
        3'b000: out12 = 0;
		3'b010: out12 = 0;
		3'b011: out12 = 0;
		3'b100: out12 = 0;
		default: out12 = 1;
   	endcase
	end
	reg out13;
	always @(*)
    begin

		case (SW[2:0])
		default: out13 = 1;
   	endcase
	end
    assign Q[0]=out0    ;
    assign Q[1]=out1    ;
    assign Q[2]=out2    ;
    assign Q[3]=out3    ;
    assign Q[4]=out4    ;
    assign Q[5]=out5    ;
    assign Q[6]=out6    ;
    assign Q[7]=out7    ;
    assign Q[8]=out8    ;
    assign Q[9]=out9    ;
    assign Q[10]=out10   ;
    assign Q[11]=out11    ;
    assign Q[12]=out12    ;
    assign Q[13]=out13    ;

endmodule



