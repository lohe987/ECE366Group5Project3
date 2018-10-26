class Simulator:
    registers = {  
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "a": 0
    }
    artihmetic_ins = {
        "0001": lambda x,y: x + y,  # add
        "1100": lambda x,y: x + y,  # addi
        "1000": lambda x,y: x - y,  # sub
        "1001": lambda x,y: x * y,  # mlt
        "0101": lambda x,y: x << y, # sll
        "0100": lambda x,y: x >> y, # srl
        "0011": lambda x,y: x & y   # and
    }
    ActiveRegister = '0'

    def __SanatizeLine(self, line:str) -> list:
        return [i for i in line.strip().lower().split(' ') if i != '' and i != ' '] 
    
    def __BinToNumber(self, bin_str:str) -> int:
        return int(bin_str, base=2)

    def __RunArthmeticInstruction(self, instruction:list, immediate:int) -> bool:
        """
        Runs the instruction specified and updates the registers object
            :param instruction:list: 
            :param immediate:int=None: 
        """
        try:
            if immediate is not None:
                # cut off the last letter
                self.registers[self.ActiveRegister] = self.artihmetic_ins[instruction[0]](self.registers[self.ActiveRegister], immediate)
            else:
                self.registers[self.ActiveRegister] = self.artihmetic_ins[instruction[0]](self.registers[self.ActiveRegister], self.registers[instruction[1]])
            return True
        except KeyError as error:
            print(error)
            return False

    def __init__(self, file_name:str):
        self.source = file_name

    def Run(self):
        try:
            with open(self.source, 'r') as source:
                for i, line in enumerate(source):
                    line = line.strip()
                    opcode = line[1:5]
                    number = self.__BinToNumber(line[5:8])
                    # SAR
                    if opcode == "0000":
                        self.ActiveRegister = str(number) # needs to be stored as a string
                    # STOP
                    elif opcode == "1111":
                        break
                    # MOV
                    elif opcode == "0010" or opcode == "1011":
                        if opcode[-1] == "1":
                            self.registers[self.ActiveRegister] = number
                        else:
                            self.registers[self.ActiveRegister] = self.registers[number]
                    else:
                        if self.__RunArthmeticInstruction([opcode, str(number)], None if '1100' != opcode else number):
                            continue
                        else:
                            break
            print(self.registers)
        except IOError as error:
            print(error)