module tfilpflop (clock,reset, t,q);
    output q;
    input t,clock,reset;
    reg q;
    initial
       begin
        q=1'b0;
       end
    always@(posedge clock, negedge reset)
    begin
        if(~reset)
            q <= 1'b0;
        else
            q <= q ^ t;
    end
endmodule
