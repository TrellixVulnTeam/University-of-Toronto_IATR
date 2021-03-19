

module shifter (SW,KEY,LEDR);
	input [9:0] SW;
	input [3:0] KEY;
    output [7:0] LEDR;
    wire ASR,ShiftRight,Load_n, clk,reset_n,first_in;
    wire [7:0] LoadVal;
    assign LoadVal[7:0] =SW[7:0] ;
    assign ASR = KEY[3];
    assign ShiftRight = KEY[2];
    assign Load_n = KEY[1];
    assign clk = KEY[0];
    assign reset_n = SW[9];
	wire [7:0] Q;
    assign LEDR[7:0] = Q[7:0] ;

    mux m0(
        .s(ASR),
        .x(0),
		.y(Q[7]),
        .out(first_in)
        );

    shifterbit s7(
        .load_val(LoadVal[7]),
        .in(first_in),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[7])
        );

    shifterbit s6(
        .load_val(LoadVal[6]),
        .in(Q[7]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[6])
        );

    shifterbit s5(
        .load_val(LoadVal[5]),
        .in(Q[6]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[5])
        );

    shifterbit s4(
        .load_val(LoadVal[4]),
        .in(Q[5]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[4])
        );

    shifterbit s3(
        .load_val(LoadVal[3]),
        .in(Q[4]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[3])
        );

    shifterbit s2(
        .load_val(LoadVal[2]),
        .in(Q[3]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[2])
        );

    shifterbit s1(
        .load_val(LoadVal[1]),
        .in(Q[2]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[1])
        );

    shifterbit s0(
        .load_val(LoadVal[0]),
        .in(Q[1]),
		.shift(ShiftRight),
        .load_n(Load_n),
        .clk(clk),
        .reset_n(reset_n),
		.out(Q[0])
        );








endmodule

module shifterbit (load_val,in,shift,load_n, clk,reset_n,out);
    input load_val,in,shift,load_n, clk,reset_n;
	output out;
    wire m0out,m1out;
    mux m0(
        .s(shift),
        .x(out),
		.y(in),
        .out(m0out)
        );
    mux m1(
        .s(load_n),
        .x(load_val),
		.y(m0out),
        .out(m1out)
        );


    filpflop f0(
        .clock(clk),
        .reset_n(reset_n),
		.q(out),
        .d(m1out)
        );

endmodule



module mux (s,x,y, out);
	input s,x,y;
	output out;
	reg t; // target of assignment
	always @(s)
    begin

		case (s)
		1'b0: t = x;
		1'b1: t = y;

   	endcase
	end
    assign out = t;

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