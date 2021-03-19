


module morseencoder (SW,CLOCK_50,KEY,LEDR);
   input [2:0] SW;
   input [1:0] KEY;
   input CLOCK_50;
   output [7:0] LEDR;
	assign LEDR[7] = E;
   wire [13:0] LETTER;
   wire [13:0] VLUS;
   wire E,reset;
   assign reset = KEY[0];
   shifter s2(
    .clock(CLOCK_50),
    .reset_n(reset),
    .d(LETTER),
    .par_load(~KEY[1]),
    .enable(E),
    .OUT(VLUS)
    );

   assign LEDR[0] = VLUS[13];
   lut l2(
    .SW(SW),
    .Q(LETTER)
    );

   fivehzclk c2(
        .d(25'b0000000000000000000000001),
        .clock(CLOCK_50),
        .enable(1),
        .par_load(~KEY[1]),
        .reset_n(1),
        .out(E)
        );

endmodule

module fivehzclk (d,clock, enable,par_load,reset_n,out);
input [24:0] d ;                  // Declare d
input clock;                     // Declare clock
input reset_n;                   // Declare reset_n
input par_load, enable;          // Declare par_load and enable
output out;
reg [24:0] q;                    // Declare q
always @(posedge clock)         // Triggered every time clock rises
begin
    if (reset_n == 1'b0)        // When reset_n is 0
        q <= 0 ;                // Set q to 0
    else if ( par_load == 1'b1) // Check if parallel load
        q <= d ;                // Load d
    else if ( enable == 1'b1 )  // Increment q only when enable is 1
        begin
            if ( q == 25'b1011111010101000100110000 ) // When q is the maximum value for the counter
                q <= 0 ;        // Reset q into 0
            else                // When q is not the maximum value
                q <= q + 1'b1 ; // Increment q
        end
end
reg final;
always @(q)
begin
    case (q[24:0])
    25'b0000000000000000000000000: final = 1;
    default: final = 0;
endcase
end
assign out = final;

endmodule
module shifter (clock,reset_n,d,par_load,enable,OUT);

    wire [13:0] QQ;
    output [13:0] OUT;
    input [13:0] d ;                  // Declare d
    input clock;                     // Declare clock
    input reset_n;                   // Declare reset_n
    input par_load, enable;          // Declare par_load and enable
    reg [13:0] q;                    // Declare q
    always @(posedge clock)         // Triggered every time clock rises
    begin
        if (reset_n == 1'b0)        // When reset_n is 0
            q <= 0 ;                // Set q to 0
        else if ( par_load == 1'b1) // Check if parallel load
            q <= d ;                // Load d
        else if ( enable == 1'b1 )  // Increment q only when enable is 1
            q <= QQ ; // Increment q

    end

    assign OUT[13:0] = q[13:0];
    shifting s4(
            .N(q),
            .Q(QQ)
            );


endmodule

module shifting (N,Q);
	input [13:0]N;
	output [13:0] Q;
    assign Q[13:1] = N[12:0];
    assign Q[0] = 0;


endmodule


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
