SAR 3 #R3 IS ACTIVE
LOAD 0 #R3=P

SAR 5 #R5 IS ACTIVE
MOVI 1 #R5=1
SAR 4
LOAD 5 #R4=MEM[1]=Q

##start of main loop
## have comparison statement for checking if loop is done
## if not done
## checks if counter just begun and jumps to setting the current value to six
## else jumps to multiplication

#counter to begin
SAR 2
MOVI 6
B MOD

#multiplication loop
SAR 2
MLT 5
B MOD

#begining of MOD branch
SAR 2
BSLT #branches out if currentValue is less than Q branches out 
SUB 4
B    #branches back to main

#begining of done branch
SAR 1
MOVI 2
SAR 2 #R2 IS ACTIVE
STOR 1 #R2=MEM[2]
DONE


