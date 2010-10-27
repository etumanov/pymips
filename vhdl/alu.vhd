-- File: alu.vhd
-- Generated by MyHDL 0.6
-- Date: Wed Oct 27 16:36:17 2010

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_06.all;

entity alu is
    port (
        control: in unsigned(3 downto 0);
        op1: in unsigned(31 downto 0);
        op2: in unsigned(31 downto 0);
        out_: inout signed (31 downto 0);
        zero: out std_logic
    );
end entity alu;

architecture MyHDL of alu is


begin


ALU_LOGIC_ALU: process (control, op1, op2) is
begin
    if (signed(resize(control, 5)) = 0, 2) then
        out_ <= (op1 and op2);
    elsif (signed(resize(control, 5)) = 1, 2) then
        out_ <= (op1 or op2);
    elsif (signed(resize(control, 5)) = 10, 2) then
        out_ <= signed(op1 + op2);
    elsif (signed(resize(control, 5)) = 110, 2) then
        out_ <= signed(op1 - op2);
    elsif (signed(resize(control, 5)) = 111, 2) then
        out_ <= "00000000000000000000000000000000";
    elsif (bin(control, 4) = string'("1100")) then
        out_ <= signed((not (op1 or op2)));
    end if;
end process ALU_LOGIC_ALU;

ALU_ZERO_DECTOR: process (out_) is
begin
    if (out_ = 0) then
        zero <= '1';
    else
        zero <= '0';
    end if;
end process ALU_ZERO_DECTOR;

end architecture MyHDL;