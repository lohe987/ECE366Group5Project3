SAR 0 #R0 IS ACTIVE
MOVI 0 #R0=0
STOR 0 #MEM[0]=0 #counter 
SAR 1
MOVI 1 #R1=1
SAR 0  #Ra=R0
STOR 1 #MEM[1]=0 #current max hamming distance
SAR 1
MOVI 3 #R1=3
ADDI 3 #R1=6
SAR 0
STOR 1 #MEM[6]=0 #number of value with max hamming distance
SAR 1
ADDI 1 #R1=7
SAR 0
MOV 1 #R0=7
ADDI 1 #R0=8
STOR 1 #MEM[7]=8 #address of array
SAR 0
MOVI 2 #R0=2
ADDI 2 #R0=4
ADDI 2 #R0=6
ADDI 2 #R0=8
ADDI 2 #R0=10
MLT 0 #R0=10*10=100
SAR 1
MOVI 2 #R1=2
ADDI 2 #R1=4
SAR 0 
STOR 1 #MEM[4]=100



MAIN:
SAR 0
MOVI 0
LOAD 0 #R0=counter
SAR 1
MOVI 3
ADDI 1
LOAD 1 #R1=100
SAR 6
#
