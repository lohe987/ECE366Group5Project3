SAR 3 #R3 IS ACTIVE
LOAD 0 #R3=P

SAR 5 #R5 IS ACTIVE
MOVI 1 #R5=1
SAR 4
LOAD 5 #R4=MEM[1]=Q

SAR 5 
MOVI 3 #R5=3
ADDI 3 #R5=6


##start of main loop
MAIN:
SAR 6
MOVI 3
SJL 6 #RP=3
SAR 3
BSLT 1 #branches out of the loop
SAR 6
MOVI 1
SJL 6 #RP=1
SAR 1
BSLT 6 



#counter to begin
MULTI:
SAR 2
MOVI 6
SAR 6
MOVI 2 #R6=2
SJL 6  #RP=2
B 


MULT:
SAR 2
MLT 5
SAR 6
MOVI 2 #R6=2
SJL 6  #RP=2
B 

#begining of MOD branch
MOD:
SAR 6
MOVI 3 #R6=3
SJL 6  #RP=3
SAR 3
BSLT 2
SAR 2
SUB 4
SAR 6
MOVI 2 #R6=2
SJL 6  #RP=2
B    #branches back to beg of MOD

#begining of done branch
PROGRAMFINISH:
SAR 1
MOVI 2
SAR 2 #R2 IS ACTIVE
STOR 1 #R2=MEM[2]
DONE


