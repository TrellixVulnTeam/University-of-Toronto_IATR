module memory(
	input SW,
	input KEY,
	output HEX5, HEX4, HEX2, HEX0
	);
	
	wire [3:0] q;
	wire [3:0] data;
	wire [4:0] address;
	
	assign data = SW[3:0];
	assign address = SW[8:4];
	
	ram32x4 r0(
		.address(address),
		.clock(KEY[0]),
		.data(data),
		.wren(SW[9]),
		.q(q));
	
	seven_seg_decoder h5 (.S(address[4]), .HEX(HEX5));
	seven_seg_decoder h4 (.S(address[3:0]), .HEX(HEX4));
	seven_seg_decoder h2 (.S(data), .HEX(HEX2));
	seven_seg_decoder h0 (.S(q), .HEX(HEX0))

endmodule
