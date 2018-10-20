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
        "add": lambda x,y: x + y,
        "sub": lambda x,y: x - y,
        "mlt": lambda x,y: x * y,
        "srl": lambda x,y: x << y,
        "sll": lambda x,y: x >> y,
        "and": lambda x,y: x & y
    }
    ActiveRegister = '0'

    def __SanatizeLine(self, line:str) -> list:
        return [i for i in line.strip().lower().split(' ') if i != '' and i != ' '] 

    def __RunArthmeticInstruction(self, instruction:list, immediate:int) -> bool:
        """
        Runs the instruction specified and updates the registers object
            :param instruction:list: 
            :param immediate:int=None: 
        """
        try:
            if immediate is not None:
                # cut off the last letter
                instruction[0] = instruction[0][:-1]
                self.registers[self.ActiveRegister] = self.artihmetic_ins[instruction[0]](self.registers[self.ActiveRegister], immediate)
            else:
                self.registers[self.ActiveRegister] = self.artihmetic_ins[instruction[0]](self.registers[self.ActiveRegister], self.registers[instruction[1]])
            return True
        except KeyError as error:
            print(error)
            return False

    def __init__(self, file_name:str):
        self.source = open(file_name, 'r')

    def Run(self):
        try:
            for i, line in enumerate(self.source):
                # sanatize the line
                line = self.__SanatizeLine(line)
                print(line)
                if line[0] == "sar":
                    self.ActiveRegister = line[1]
                elif line[0] == "b":
                    print(i + 1)
                    self.source.seek()
                elif line[0] == "stop":
                    break
                elif "mov" in line[0]:
                    if "i" in line[0]:
                        self.registers[self.ActiveRegister] = int(line[1])
                    else:
                        self.registers[self.ActiveRegister] = self.registers[line[1]]
                else:
                    if self.__RunArthmeticInstruction(line, None if 'i' not in line[0] else int(line[1])):
                        continue
                    else:
                        break
            print(self.registers)
        except IOError as error:
            print(error)