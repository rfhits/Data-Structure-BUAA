`define s0 0
`define stime 1
`define pc 2
`define space0 3
`define grf 4
`define addr 5
`define space1 6
`define eq0 7
`define eq1 8
`define data 9

module cpu_checker(
    input clk,
    input reset,
    input [7:0] char,
    input [15:0] freq,
    output reg[1:0] format_type,
    output reg[3:0] error_code
    );
reg [3:0]cnt;
reg [3:0]state;
reg [1:0]type;
reg [31:0]shijian;
reg [3:0]error;
reg [31:0]pcnum;
reg [4:0]grfnum;
reg [31:0]addrnum;

initial
begin
 state <= `s0;
 cnt <= 0;
 type <= 0;
 format_type <= 0;
 error_code <= 0;
 error <= 0;
 shijian <= 0;
 pcnum <= 0;
 grfnum <= 0;
 addrnum <= 0;
end

always@(posedge clk)
begin
 if(reset)
 begin
  state <= `s0;
  cnt <= 0;
 end
 else
 begin
  case(state)
   `s0:
   begin
    state <= (char == "^")?`stime:`s0;
    format_type <= 0;
   end
   
   `stime:
   begin
    if(char >= "0" &&char <= "9")
    begin
     cnt <= cnt + 1;
     shijian <= (shijian << 3) + (shijian << 1) + char - "0";
     if(cnt < 4)
      state <= `stime;
     else
     begin
      cnt <= 0;
      state <= `s0;
      shijian <= 0;
     end
    end
    else if(char == "@" && cnt!=0)
    begin
     state <= `pc;
     cnt <= 0;
     if(shijian&((freq >> 1) - 1)!=0)
     begin
      error <= error + 1;
     end
    end
    else
    begin
     state <= `s0;
     cnt <= 0;
     shijian <= 0;
    end
   end
   
   `pc:
   begin
    if((char >= "0" && char <= "9")||(char >= "a" && char <= "f"))
    begin
     cnt <= cnt + 1;
     pcnum <= ((char >="0"&&char<="9"))?((pcnum<<4)+char-"0"):((pcnum<<4)+char-"a"+10);
     if(cnt < 8)
     begin
      state <= `pc;
     end
     else
     begin
      state <= `s0;
      cnt <= 0;
      pcnum <= 0;
      error <= 0;
     end
    end
    else if(char == ":" && cnt == 8)
    begin
     state <= `space0;
     cnt <= 0;
     if(!((pcnum & 2'b11 == 0) && (pcnum >= 32'h00003000 && pcnum<= 32'h00004fff)))
      error <= error + 2;
     pcnum <= 0;
    end
    else
    begin
     state <= `s0;
     cnt <= 0;
     pcnum <= 0;
     error <= 0;
    end
   end