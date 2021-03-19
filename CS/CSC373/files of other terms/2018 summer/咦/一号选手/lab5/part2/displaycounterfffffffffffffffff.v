






module mux (SW, A,B,C,D,T);
	input [1:0] SW;
	input A,B,C,D;
	output T;
	reg out; // target of assignment
	always @(*)
    begin

		case (SW[1:0])
        2'b00: out = A;
        2'b01: out = B;
        2'b10: out = C;
        2'b11: out = D;
   	endcase
	end
   assign T = out;
endmodule

module displaycounterfff (SW,KEY,CLOCK_50,LEDR,HEX0);
input [9:0] SW;
input [2:0] KEY;
input CLOCK_50;
output [9:0] LEDR;
output [6:0] HEX0;
wire A,B,C,D,E;
wire [3:0] Q;
reg edda;
always @(SW)
    begin
        case (SW[1:0])
        2'b00: edda = CLOCK_50;
        2'b01: edda = B;
        2'b10: edda = C;
        2'b11: edda = D;
    endcase
end
assign E = edda;
assign A = CLOCK_50;

endmodule