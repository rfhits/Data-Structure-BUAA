module Adder(
    input a, 
    input b, 
    input cin, 
    output sum, 
    output overflow
    );
    wire s1, s2, s3;
    //xor与and均为原语，是系统预定义的模块
    xor xor1(sum, a, b, cin);
    and and1(s1, a, b);
    and and2(s2, a, cin);
    and and3(s3, b, cin);
    or or1(overflow, s1, s2, s3);
endmodule
initial begin
    always @() begin
        
    end
end