module project	(
		CLOCK_50,						//	On Board 50 MHz
		// Your inputs and outputs here
        KEY,
		  HEX0,
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

	input			CLOCK_50;				//	50 MHz
	input   [3:0]   KEY;

   output [6:0] HEX0;
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

	wire resetn;
	assign resetn = KEY[0];

	wire forward;
	wire backward;
	wire not_pressed;

	assign forward = ((~KEY[1]) && (KEY[2]));
	assign backward = ((~KEY[2]) && (KEY[1]));
	assign not_pressed = (KEY[1] && KEY[2]);

	// Create the colour, x, y and writeEn wires that are inputs to the controller.
	wire [2:0] colour;
	wire [7:0] x;
	wire [6:0] y;
	wire writeEn;

	reg reset_fsm = 1;
	reg [1:0] score = 2'd0;

	wire [7:0] speed = {6'd0, score};

	hex_decoder H0(
        .hex_digit({2'd0, score}),
        .segments(HEX0)
        );

  //states ?
	localparam nothing_pressed = 5'd0,
				  forward_wait = 5'd1,
				  backward_wait = 5'd2;

	reg [4:0] current_state = nothing_pressed;
	reg [4:0] next_state = nothing_pressed;
	reg [1:0] dfrog = 2'd0;

	//FSM Table
	always@(*)
	begin: state_table
		case(current_state)
			nothing_pressed:
									if(forward)
										next_state = forward_wait;
									else if(backward)
										next_state = backward_wait;
									else
										next_state = nothing_pressed;
			forward_wait:
									if(not_pressed)
										next_state = nothing_pressed;
									else
										next_state = forward_wait;
			backward_wait:
									if(not_pressed)
										next_state = nothing_pressed;
									else
										next_state = backward_wait;
		   default: next_state = nothing_pressed;
		endcase
	end




	plot p(
		.clock(CLOCK_50),
		.writeEn(writeEn)
	);



	reg [7:0] frogx = 8'd74;
	reg [6:0] frogy = 7'd100;

	reg [7:0] log1x = 8'd14;
	reg [6:0] log1y = 8'd84;

	reg [7:0] log2x = 8'd04;
	reg [6:0] log2y = 8'd68;

	reg [7:0] log3x = 8'd34;
	reg [6:0] log3y = 8'd52;

	reg [7:0] log4x = 8'd08;
	reg [6:0] log4y = 8'd36;

	reg [7:0] log5x = 8'd54;
	reg [6:0] log5y = 8'd20;




	wire Edge, begin_grass, win_grass, frog, log1, log2, log3, log4, log5;

	assign Edge = ((x >= 8'd0) && (y >= 7'd0) && (x <= 8'd160) && (y <= 7'd120));
	assign begin_grass = ((x >= 8'd0) && (y >= 7'd100) && (x <= 8'd160) && (y <= 7'd120));
	assign win_grass = ((x >= 8'd0) && (y >= 7'd0) && (x <= 8'd159) && (y <= 7'd20));

	//长宽
	localparam frogr = 8'd16;
	localparam frogb = 7'd16;
	localparam logr = 8'd48;
	localparam logb = 7'd16;

	assign frog = ((x >= frogx) && (x <= frogx + frogr) && (y >= frogy) && (y <= frogy + frogb));
	assign log1 = ((x >= log1x) && (x <= log1x + logr) && (y >= log1y) && (y <= log1y + logb));
	assign log2 = ((x >= log2x) && (x <= log2x + logr) && (y >= log2y) && (y <= log2y + logb));
	assign log3 = ((x >= log3x) && (x <= log3x + logr) && (y >= log3y) && (y <= log3y + logb));
	assign log4 = ((x >= log4x) && (x <= log4x + logr) && (y >= log4y) && (y <= log4y + logb));
	assign log5 = ((x >= log5x) && (x <= log5x + logr) && (y >= log5y) && (y <= log5y + logb));

	reg d1 = 1'b1;
	reg d2 = 1'b1;
	reg d3 = 1'b1;
	reg d4 = 1'b1;
	reg d5 = 1'b1;

	//turn around the logs
	always @(posedge CLOCK_50)
	begin
		if (log1x <= 8'd2 + speed)
			d1 <= 1;
		if ((log1x + logr) >= 8'd158)
			d1 <= 0;
		if (log2x <= 8'd4 + speed)
			d2 <= 1;
		if ((log2x + logr) >= 8'd158)
			d2 <= 0;
		if (log3x<= 8'd2 + speed)
			d3 <= 1;
		if ((log3x + logr) >= 8'd158)
			d3 <= 0;
		if (log4x <= 8'd8 + speed)
			d4 <= 1;
		if ((log4x + logr) >= 8'd158)
			d4 <= 0;
		if (log5x <= 8'd2 + speed)
			d5 <= 1;
		if ((log5x + logr) >= 8'd158)
			d5 <= 0;
	end


	reg [24:0] count_to = 25'd0;

	//动木头 + 动青蛙
	always @(posedge CLOCK_50)
	begin
		if (count_to >= 25'd25000000) begin
			count_to <= 0;
		end

		else begin
			count_to <= count_to + 1'd1;

			if(count_to == 25'd1) begin

				if(frogy == 7'd84) begin
					if(d1 == 1)
						frogx <= (frogx + 8'd2 + speed);
					else
						frogx <= (frogx - 8'd2 - speed);
				end

				else if(frogy == 7'd68) begin
					if(d2 == 1)
						frogx <= (frogx + 8'd4 + speed);
					else
						frogx <= (frogx - 8'd4 - speed);
				end

				else if(frogy == 7'd52) begin
					if(d3 == 1)
						frogx <= (frogx + 8'd2 + speed);
					else
						frogx <= (frogx - 8'd2 - speed);
				end

				else if(frogy == 7'd36) begin
					if(d4 == 1)
						frogx <= (frogx + 8'd8 + speed);
					else
						frogx <= (frogx - 8'd8 - speed);
				end

				else if(frogy == 7'd20) begin
					if(d5 == 1)
						frogx <= (frogx + 8'd2 + speed);
					else
						frogx <= (frogx - 8'd2 - speed);
				end

				//move the logs
				if(d1 == 1)
					log1x <= (log1x + 8'd2 + speed);
				else
					log1x <= (log1x - 8'd2 - speed);
				if(d2 == 1)
					log2x <= (log2x + 8'd4 + speed);
				else
					log2x <= (log2x - 8'd4 - speed);
				if(d3 == 1)
					log3x <= (log3x + 8'd2 + speed);
				else
					log3x <= (log3x - 8'd2 - speed);
				if(d4 == 1)
					log4x <= (log4x + 8'd8 + speed);
				else
					log4x <= (log4x - 8'd8 - speed);
				if(d5 == 1)
					log5x <= (log5x + 8'd2 + speed);
				else
					log5x <= (log5x - 8'd2 - speed);
			end
		end
	end

	reg [25:0] count_1second = 0;
	reg whatever = 0; //?
	reg game_over = 0;
	wire Game_Over;
	assign Game_Over = game_over;


	always@(posedge CLOCK_50)

	begin: enable_signals
		case(current_state)
			nothing_pressed: begin

				if(count_1second >= 26'd50000000)
					count_1second <= 0;
				else begin
					count_1second <= count_1second + 1;
					if(count_1second == 26'd49999999) begin
						if(game_over == 1)
							game_over <= 0;
					end
				end

				reset_fsm <= 1;

				if (dfrog == 2'd2) begin
					dfrog <= 2'd0;

					if(frogy == 7'd100)begin
						if((frogx < log1x) || ((frogx + frogr) > (log1x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd84;
					end

					else if(frogy == 7'd84)begin
						if((frogx < log2x) || ((frogx + frogr) > (log2x + logr)))begin
							frogy <= 7'd100;
							reset_fsm <= 0;
							score <= 0;
							game_over <= 1;
						end
						else
						frogy <= 7'd68;
					end

					else if(frogy == 7'd68)begin
						if((frogx < log3x) || ((frogx + frogr) > (log3x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
						frogy <= 7'd52;
					end

					else if(frogy == 7'd52)begin
						if((frogx < log4x) || ((frogx + frogr) > (log4x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd36;
					end

					else if(frogy == 7'd36)begin
						if((frogx < log5x) || ((frogx + frogr) > (log5x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd20;
					end

					else if(frogy == 7'd20)begin
						score <= score + 1;
						frogy <= 7'd100;
					end
				end

				else if (dfrog == 2'd1) begin
					dfrog = 0;
					if(frogy == 7'd100)begin
						frogy <= 7'd100;
					end
					else if(frogy == 7'd84)begin
						frogy <= 7'd100;
					end
					else if(frogy == 7'd68)begin
						if((frogx < log1x) || ((frogx + frogr) > (log1x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd84;
					end
					else if(frogy == 7'd52)begin
						if((frogx < log2x) || ((frogx + frogr) > (log2x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd68;
					end
					else if(frogy == 7'd36)begin
						if((frogx < log3x) || ((frogx + frogr) > (log3x + logr)))begin
							score <= 0;
							frogy <= 7'd100;
							reset_fsm <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd52;
					end
					else if(frogy == 7'd20)begin
						if((frogx < log4x) || ((frogx + frogr) > (log4x + logr)))begin
							reset_fsm <= 0;
							frogy <= 7'd100;
							score <= 0;
							game_over <= 1;
						end
						else
							frogy <= 7'd36;
					end
				end
				else
					whatever <= 0;


			end
			forward_wait: dfrog <= 2'd2;
			backward_wait: dfrog <= 2'd1;
		endcase
	end


	always@(posedge CLOCK_50)
	begin: state_FFs
		if(!reset_fsm)
			current_state <= nothing_pressed;
		else
			current_state <= next_state;
	end





	color c(
		.clock(CLOCK_50),
		.end_game(Game_Over),
		.begin_grass(begin_grass),
	   .win_grass(win_grass),
   	.frog(frog),
	   .log1(log1),
	   .log2(log2),
		.log3(log3),
		.log4(log4),
		.log5(log5),
		.colour(colour),
		.x(x),
		.y(y)
	);


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

endmodule

module color(clock, end_game, begin_grass, win_grass, frog, log1, log2, log3, log4, log5, colour, x ,y);

	input clock;
	input end_game;
	input begin_grass;
	input win_grass;
	input frog;
	input log1;
	input log2;
	input log3;
	input log4;
	input log5;
	output reg [2:0] colour;
	wire [7:0] wx;
	wire [6:0] wy;
	wire [14:0] address;
	wire [2:0] game_over_color;
	output [7:0] x;
	output [6:0] y;
	assign x = wx;
	assign y = wy;


	always @(posedge clock)

	begin
		if(end_game)
			colour <= game_over_color;
		else if(frog)
			colour <= 3'b000;
		else if(win_grass | begin_grass)
			colour <= 3'b010;
		else if(log1|log2|log3|log4|log5)
			colour <= 3'b110;
		else
			colour = 3'b001;
	end

	refresh_screen r(
		.clock(clock),
		.x(wx),
		.y(wy)
		);
	vga_address_translator v(
		.x(wx),
		.y(wy),
		.mem_address(address)
		);
	Image (
		.address(address),
		.clock(clock),
		.q(game_over_color)
		);

endmodule


module refresh_screen(clock, x, y);

	input clock;
	reg [7:0] xcount = 8'd0;
	reg [6:0] ycount = 7'd0;
	output [7:0] x;
	output [6:0] y;

	always @(posedge clock)
	begin
		if((ycount >= 7'd119) && (xcount >= 8'd159)) begin
			xcount <= 0;
			ycount <= 0;
		end
		else if(xcount >= 8'd159)begin
			xcount <= 0;
			ycount <= y + 1;
		end
		else
			xcount <= x + 1;
	end
	assign x = xcount;
	assign y = ycount;
endmodule


module plot(clock, writeEn);

	input clock;
	output writeEn;
	reg [23:0] timer = 24'b0;
	always @(posedge clock)
	begin
		if (timer >= 24'd12500000)
			timer <= 0;
		else
			timer <= timer + 1;
	end
	assign writeEn = (timer < 24'd2500000) ? 1 : 0;

endmodule

module hex_decoder(hex_digit, segments);
    input [3:0] hex_digit;
    output reg [6:0] segments;

    always @(*)
        case (hex_digit)
            4'h0: segments = 7'b100_0000;
            4'h1: segments = 7'b111_1001;
            4'h2: segments = 7'b010_0100;
            4'h3: segments = 7'b011_0000;
            4'h4: segments = 7'b001_1001;
            4'h5: segments = 7'b001_0010;
            4'h6: segments = 7'b000_0010;
            4'h7: segments = 7'b111_1000;
            4'h8: segments = 7'b000_0000;
            4'h9: segments = 7'b001_1000;
            4'hA: segments = 7'b000_1000;
            4'hB: segments = 7'b000_0011;
            4'hC: segments = 7'b100_0110;
            4'hD: segments = 7'b010_0001;
            4'hE: segments = 7'b000_0110;
            4'hF: segments = 7'b000_1110;
            default: segments = 7'h7f;
        endcase
endmodule


`timescale 1 ps / 1 ps
// synopsys translate_on
module Image (
	address,
	clock,
	q);

	input	[14:0]  address;
	input	  clock;
	output	[2:0]  q;
`ifndef ALTERA_RESERVED_QIS
// synopsys translate_off
`endif
	tri1	  clock;
`ifndef ALTERA_RESERVED_QIS
// synopsys translate_on
`endif

	wire [2:0] sub_wire0;
	wire [2:0] q = sub_wire0[2:0];

	altsyncram	altsyncram_component (
				.address_a (address),
				.clock0 (clock),
				.q_a (sub_wire0),
				.aclr0 (1'b0),
				.aclr1 (1'b0),
				.address_b (1'b1),
				.addressstall_a (1'b0),
				.addressstall_b (1'b0),
				.byteena_a (1'b1),
				.byteena_b (1'b1),
				.clock1 (1'b1),
				.clocken0 (1'b1),
				.clocken1 (1'b1),
				.clocken2 (1'b1),
				.clocken3 (1'b1),
				.data_a ({3{1'b1}}),
				.data_b (1'b1),
				.eccstatus (),
				.q_b (),
				.rden_a (1'b1),
				.rden_b (1'b1),
				.wren_a (1'b0),
				.wren_b (1'b0));
	defparam
		altsyncram_component.address_aclr_a = "NONE",
		altsyncram_component.clock_enable_input_a = "BYPASS",
		altsyncram_component.clock_enable_output_a = "BYPASS",
		altsyncram_component.init_file = "image.mif",
		altsyncram_component.intended_device_family = "Cyclone V",
		altsyncram_component.lpm_hint = "ENABLE_RUNTIME_MOD=NO",
		altsyncram_component.lpm_type = "altsyncram",
		altsyncram_component.numwords_a = 19200,
		altsyncram_component.operation_mode = "ROM",
		altsyncram_component.outdata_aclr_a = "NONE",
		altsyncram_component.outdata_reg_a = "UNREGISTERED",
		altsyncram_component.widthad_a = 15,
		altsyncram_component.width_a = 3,
		altsyncram_component.width_byteena_a = 1;


endmodule
