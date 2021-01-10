module tfilpflop (clock,reset, t,out);
    output out;
    input t,clock,reset;
    reg nq,q;
    initial
       begin
        nq=1'b1;
        q=1'b0;
       end
     always @ (clock)
        begin
            if(clock)
                 begin
                   if (t==1'b0) begin nq=nq; q=q; end
                   else begin nq=~nq; q=~q; end
                 end
         end
    assign out = q;
endmodule
