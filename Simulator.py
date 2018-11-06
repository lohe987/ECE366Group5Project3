from assembler import assemble

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
        "p": 0
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
    ProgramData = []
    LabelLocations = []
    Memory = []
    ActiveRegister = '0'

    def __LoadMemory(self) -> list:
        with open(f'{self.source.split(".")[0]}_mem.txt') as memFile:
            for line in memFile:
                self.Memory.append(int(line, 2))                

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

    def __GetLabels(self) -> None:
        # read the source file
        # find the labels and add their locations in the file to a list
        if '.asm' not in self.source:
            print('Hey that\'s not an asm file!')
            return None
        with open(self.source, 'r') as file:
            for i, line in enumerate(file):
                if ':' in line:
                    self.LabelLocations.append(i + 1)
                   
    def __PrepareProgram(self):
        # assemble the program if it's an asm file
        # else just consider it a binary. will maybe add error handling later
        if '.asm' in self.source:
            assembled_program = assemble(self.source)
        else:
            assembled_program = self.source
        # put every line of program into a list
        with open(assembled_program, 'r') as source:
            for line in source:
                self.ProgramData.append(line)

    def __init__(self, file_name:str):
        self.source = file_name
        self.__PrepareProgram()
        self.__GetLabels()
        self.__LoadMemory()

    def Run(self):
        # needs to be a while loop to enable jumping
        i = 0
        dic = 0
        while i < len(self.ProgramData):
            print(f'Instruction {i}')
            line = self.ProgramData[i]
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
                # if the last number in the op is 1 then it's movi
                if opcode[-1] == "1":
                    self.registers[self.ActiveRegister] = number
                else:
                    self.registers[self.ActiveRegister] = self.registers[number]
            # B
            elif opcode == "1110":
                # make the pc(i) = jump location dictated by the label holder register
                i = self.LabelLocations[self.registers['p']] - 1 # -1 because 0 indexed
                dic += 1
                continue
            # BSLT
            elif opcode == "1010":
                # if Ra < Rs then branch else continue
                if self.registers[self.ActiveRegister] < self.registers[str(number)]:
                    i = self.LabelLocations[self.registers['p']] - 1 # -1 because 0 indexed
                dic += 1
                continue
            # SPC
            elif opcode == "1101":
                # set the pc holder register equal to Rs + Rs
                # this will be the position of the label in the LabelHolder array
                # so if the label the program wants is the first one in the program
                # then the Rp = 0 + 0
                self.registers['p'] = self.registers[self.ActiveRegister] + self.registers[str(number)]
            # LOAD
            elif opcode == "0110":
                # Ra = MEM[Rs]
                self.registers[self.ActiveRegister] = self.Memory[self.registers[str(number)]]
            #STOR
            elif opcode == "0111":
                # Rs = MEM[Ra]
                self.Memory[self.registers[str(number)]] = self.registers[self.ActiveRegister]
            # all arthmetic instructions
            else:
                if self.__RunArthmeticInstruction([opcode, str(number)], None if '1100' != opcode else number) is False:
                    break
            i += 1
            dic += 1 # after the instruction is run increase Dynamic instruction count
        print(f'Registers: {self.registers}\nDynamic Instrcution Count: {dic}\n')
        