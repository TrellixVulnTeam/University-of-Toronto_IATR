module part3
	(
		CLOCK_50,						//	On Board 50 MHz
		// Your inputs and outputs here
      KEY,
      SW,
		// The ports below are for the VGA output.  Do not change.
		VGA_CLK,   						//	VGA Clock
		VGA_HS,							//	VGA H_SYNC
		VGA_VS,							//	VGA V_SYNC
		VGA_BLANK_N,						//	VGA BLANK
		VGA_SYNC_N,						//	VGA SYNC
		VGA_R,   						//	VGA Red[9:0]
		VGA_G,	 						//	VGA Green[9:0]
		VGA_B   						//	VGA Blue[9:0]
	);

	input	  CLOCK_50;
	input   [9:0]   SW;
	input   [3:0]   KEY;

	// Declare your inputs and outputs here
	// Do not change the following outputs
	output			VGA_CLK;   				//	VGA Clock
	output			VGA_HS;					//	VGA H_SYNC
	output			VGA_VS;					//	VGA V_SYNC
	output			VGA_BLANK_N;				//	VGA BLANK
	output			VGA_SYNC_N;				//	VGA SYNC
	output	[9:0]	VGA_R;   				//	VGA Red[9:0]
	output	[9:0]	VGA_G;	 				//	VGA Green[9:0]
	output	[9:0]	VGA_B;   				//	VGA Blue[9:0]
//	
	wire resetn;
	assign resetn = KEY[0];
	
	// Create the colour, x, y and writeEn wires that are inputs to the controller.
	wire [2:0] colour;
	wire [7:0] x;
	wire [7:0] y;
	wire writeEn;
	wire enable, loadC;
	wire [4:0] counter;

	// Create an Instance of a VGA controller - there can be only one!
	// Define the number of colours as well as the initial background
	// image file (.MIF) for the controller.
	vga_adapter VGA(
			.resetn(resetn),
			.clock(CLOCK_50),
			.colour(colour),
			.x(x),
			.y(y),
			.plot(writeEn),
			/* Signals for the DAC to drive the monitor. */
			.VGA_R(VGA_R),
			.VGA_G(VGA_G),
			.VGA_B(VGA_B),
			.VGA_HS(VGA_HS),
			.VGA_VS(VGA_VS),
			.VGA_BLANK(VGA_BLANK_N),
			.VGA_SYNC(VGA_SYNC_N),
			.VGA_CLK(VGA_CLK));
		defparam VGA.RESOLUTION = "160x120";
		defparam VGA.MONOCHROME = "FALSE";
		defparam VGA.BITS_PER_COLOUR_CHANNEL = 1;
		defparam VGA.BACKGROUND_IMAGE = "black.mif";
		
	// Put your code here. Your code should produce signals x,y,colour and writeEn/plot
	// for the VGA controller, in addition to any other functionality your design may require.
	
	
	
    
    // Instansiate datapath
	datapath d0(
			.clk(CLOCK_50),
			.enable(enable),
			.loadC(loadC),
			.resetn(resetn),
			.x_out(x),
			.y_out(y),
			.colour_in(SW[9:7]),
			.colour_out(colour));

    // Instansiate FSM control
   control c0(
			.clk(CLOCK_50),
			.go(KEY[1]),
			.resetn(resetn),
			.writeEn(writeEn),
			.enable(enable),
			.loadC(loadC));
    
endmodule

module datapath(clk, enable, loadC, resetn, x_out, y_out, colour_in, colour_out);
	input clk, enable, loadC;
	input resetn;
	output [7:0] x_out;
	output [7:0] y_out;
	input [2:0] colour_in;
	output reg [2:0] colour_out;
	
	reg [4:0] counter;
	reg [7:0] x;
	reg [7:0] y;
	wire go;
	
	wire [7:0] x_ld, y_ld;
	wire [1:0] direction;
	
	// delay, frame counter
	wire enable1;
	wire [19:0] delay;
	wire [19:0] frame;
	RateDivider delayCounter (.d(20'd833333), .enable(enable), .clk(clk), .resetn(resetn), .q(delay));
	assign enable1 = (delay == 20'd0) ? 1 : 0;
	RateDivider frameCounter (.d(20'd15), .enable(enable1), .clk(clk), .resetn(resetn), .q(frame));
	assign go = (frame == 20'd0) ? 1 : 0;
	
	// x, y counter
	Counter counterX (.reset(8'd0), .direction(direction[1]), .enable(go), .clk(clk), .resetn(resetn), .coord_out(x_ld));
	Counter counterY (.reset(8'd60), .direction(direction[0]), .enable(go), .clk(clk), .resetn(resetn), .coord_out(y_ld));
	
	directionRegister dir (.clk(clk), .resetn(resetn), .enable(go), .x(x_ld), .y(y_ld), .direction(direction));
	
	always@(posedge clk)
	begin
		if(!resetn)
		begin
			x <= 8'd0;
			y <= 8'd60;
			colour_out <= 3'b000;
		end
		else
		begin
			x <= x_ld;
			y <= y_ld;
		end
		
		if(loadC)
			colour_out <= (go == 1) ? 3'b000 : colour_in;
	end
	
	always@(posedge clk)
	begin
		if(!resetn)
			counter <= 5'b10000;
		else if(enable)
		begin
			if(counter == 5'b00000)
				counter <= 5'b10000;
			else
				counter <= counter - 1'b1;
		end
	end
	
	assign x_out = x + counter[1:0];
	assign y_out = y + counter[3:2];
endmodule

module directionRegister(clk, resetn, enable, x, y, direction);
	input clk;
	input resetn;
	input enable; 
	input [7:0]x; 
	input [7:0]y;
	output reg [1:0] direction;
	
	always@(posedge clk)
	begin
		if(!resetn)
			direction <= 2'b11;
		else if(enable)
		begin
			if(x == 0)
				direction[1] <= 1'b1;
			else if(x == 8'd156)
				direction[1] <= 1'b0;
			
			if(y == 0)
				direction[0] <= 1'b1;
			else if(y == 8'd116)
				direction[0] <= 1'b0;
		end
		else
			direction <= direction;
	end
endmodule

module RateDivider(d, enable, clk, resetn, q);
	input [19:0] d;
	input clk, enable, resetn;
	output reg [19:0] q;
	
	always @(posedge clk)
	begin	
		if(resetn == 1'b0)
			q <= d;
		else if(enable)
		begin
			if(q == 20'd0)
				q <= d;
			else
				q <= q - 1'b1;
		end	
	end 
endmodule

module Counter(reset, direction, enable, clk, resetn, coord_out);
	input [7:0] reset;
	input clk, enable, resetn, direction; //dir = 1 : right
	output [7:0] coord_out;
	
	reg [7:0] coord;
	
	always@(posedge clk)
	begin
		if(!resetn)
			coord <= reset;
		else if(enable)
		begin
			if(direction)
				coord <= coord + 1'b1;
			else
				coord <= coord - 1'b1;
		end
	end	
	
	assign coord_out = coord;
endmodule

module control(clk, go, resetn, writeEn, enable, loadC);
	input clk, go;
	input resetn;
	output reg writeEn, enable, loadC;
	
	reg [1:0] current_state, next_state;

	localparam S_LOADC = 2'b00,
				  S_LOADC_WAIT = 2'b01,
				  S_START = 2'b10;
	
	always@(*)
	begin: state_table
		case(current_state)
			S_LOADC: next_state = go ? S_LOADC_WAIT : S_LOADC;
			S_LOADC_WAIT: next_state = go ? S_LOADC_WAIT : S_START;
			S_START: next_state = S_START;
			default: next_state = S_LOADC;
		endcase
	end
	
	always@(*)
	begin: enable_signals
		writeEn = 1'b0;
		enable = 1'b0;
		loadC = 1'b0;
		
		case(current_state)
			S_START: begin
				loadC = 1'b1;
				writeEn = 1'b1;
				enable = 1'b1;
			end
		endcase
	end
	
	always@(posedge clk)
	begin: state_FFS
		if(!resetn)
			current_state <= S_LOADC;
		else
			current_state <= next_state;
	end
endmodule
