//SW[2:0] data inputs
//SW[9] select signal

//LEDR[0] output display

// Simple 4-1 mux
module mux (SW, LEDR);
	input [9:0] SW; // 2-bit control signal
	output [9:0] LEDR;
	reg out; // target of assignment
	always @(*s)
   begin

		case (SW[9:7])
		3'b000: out = SW[0];
		3'b001: out = SW[1];
		3'b010: out = SW[2];
		3'b011: out = SW[3];
    3'b100: out = SW[4];
		3'b101: out = SW[5];
		3'b110: out = SW[6];
		3'b111: out = SW[0];
   	endcase
	end
   assign LEDR[0] = out;
endmodule
