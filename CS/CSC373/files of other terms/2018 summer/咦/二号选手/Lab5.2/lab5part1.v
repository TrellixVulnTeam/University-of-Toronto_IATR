`timescale 1ns / 1ns // `timescale time_unit/time_precision

module tFlipFlop(reset, clock, toggle, out);
    input reset, clock, toggle;
	 output reg out;
	 
	 always @(posedge clock, negedge reset)
	 begin
	     if (!reset) out <= 1'b0;
		  else if (toggle) out <= out + 1'b1;
	 end
endmodule

module EightBitCounter(enable, clock, reset, Q);
    input enable, clock, reset;
	 output [7:0]Q;
	 
	 tFlipFlop t0(.reset(reset), .clock(clock), .toggle(enable), .out(Q[0]));
	 tFlipFlop t1(.reset(reset), .clock(clock), .toggle(enable & Q[0]), .out(Q[1]));
	 tFlipFlop t2(.reset(reset), .clock(clock), .toggle(enable & Q[0] & Q[1]), .out(Q[2]));
	 tFlipFlop t3(.reset(reset), .clock(clock), .toggle(enable & Q[0] & Q[1] & Q[2]), .out(Q[3]));
	 tFlipFlop t4(.reset(reset), .clock(clock), .toggle(enable & Q[0] & Q[1] & Q[2] & Q[3]), .out(Q[4]));
	 tFlipFlop t5(.reset(reset), .clock(clock), .toggle(enable & Q[0] & Q[1] & Q[2] & Q[3] & Q[4]), .out(Q[5]));
	 tFlipFlop t6(.reset(reset), .clock(clock), .toggle(enable & Q[0] & Q[1] & Q[2] & Q[3] & Q[4] & Q[5]), .out(Q[6]));
	 tFlipFlop t7(.reset(reset), .clock(clock), .toggle(enable & Q[0] & Q[1] & Q[2] & Q[3] & Q[4] & Q[5] & Q[6]), .out(Q[7]));	 
endmodule 

module lab5part1 (KEY, SW, HEX0, HEX1);
    input [3:0] KEY;
	 input [9:0] SW;
	 output [6:0] HEX0;
	 output [6:0] HEX1;
	 wire [7:0] w1;
	 
	 EightBitCounter e1(.enable(SW[1]), .clock(KEY[0]), .reset(SW[0]), .Q(w1));
	 hexDecoder h0(.SW(w1[3:0]), .HEX0(HEX0));
	 hexDecoder h1(.SW(w1[7:4]), .HEX0(HEX1));
endmodule 	 

module segment0(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = ~c3 & ~c2 & ~c1 & c0 | ~c3 & c2 & ~c1 & ~c0 | c3 & ~c2 & c1 & c0 | c3 & c2 & ~c1 & c0;
endmodule

module segment1(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = ~c3 & c2 & ~c1 & c0 | c3 & c2 & ~c0 | c2 & c1 & ~c0 | c3 & c1 & c0;
endmodule

module segment2(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = c3 & c2 & c1 | ~c3 & ~c2 & c1 & ~c0 | c3 & c2 & ~c0;
endmodule

module segment3(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = ~c2 & ~c1 & c0 | c2 & c1 & c0 | ~c3 & c2 & ~c1 & ~c0 | c3 & ~c2 & c1 & ~c0;
endmodule

module segment4(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = ~c2 & ~c1 & c0 | ~c3 & c1 & c0 | ~c3 & c2 & ~c1;
endmodule

module segment5(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = ~c3 & ~c2 & c0 | ~c3 & c2 & c1 & c0 | c3 & c2 & ~c1 & c0 | ~c3 & ~c2 & c1;
endmodule

module segment6(c3,c2,c1,c0,s);
    input c3; //4bit input
	 input c2; //4bit input
	 input c1; //4bit input
	 input c0; //4bit input
	 output s; 
	 
	 assign s = ~c3 & ~c2 & ~c1 | ~c3 & c2 & c1 & c0 | c3 & c2 & ~c1 & ~c0;
endmodule
    
module hexDecoder(SW, HEX0);	 
	 input [3:0]SW;
	 output [6:0]HEX0;
	 
	 segment0 s0(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),	
	             .s(HEX0[0]));
	 segment1 s1(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),
	             .s(HEX0[1]));
	 segment2 s2(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),
	             .s(HEX0[2]));
	 segment3 s3(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),
	             .s(HEX0[3]));
	 segment4 s4(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),
	             .s(HEX0[4]));
	 segment5 s5(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),
	             .s(HEX0[5]));
	 segment6 s6(.c3(SW[3]),
	             .c2(SW[2]),
					 .c1(SW[1]),
				    .c0(SW[0]),
	             .s(HEX0[6]));
endmodule