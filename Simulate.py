from sys import argv

artihmetic_ins = {
    "add": lambda x,y: x + y,
    "sub": lambda x,y: x - y,
    "mlt": lambda x,y: x * y,
    "srl": lambda x,y: x << y,
    "sll": lambda x,y: x >> y,
    "and": lambda x,y: x & y
}

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

ActiveRegister = '0'

def SanatizeLine(line:str) -> list:
    return [i for i in line.strip().lower().split(' ') if i != '' and i != ' ']     

def RunArthmeticInstruction(instruction:list, immediate:int) -> bool:
    """
    Runs the instruction specified and updates the registers object
        :param instruction:list: 
        :param immediate:int=None: 
    """
    try:
        if immediate is not None:
            # cut off the last letter
            instruction[0] = instruction[0][:-1]
            registers[ActiveRegister] = artihmetic_ins[instruction[0]](registers[ActiveRegister], immediate)
        else:
            registers[ActiveRegister] = artihmetic_ins[instruction[0]](registers[ActiveRegister], registers[instruction[1]])
        return True
    except KeyError as error:
        print(error)
        return False



try:
    with open(argv[1], 'r') as source:
        for i, line in enumerate(source):
            # sanatize the line
            line = SanatizeLine(line)
            print(line)
            if line[0] == "sar":
                ActiveRegister = line[1]
            elif line[0] == "b":
                print(i + 1)
                source.seek()
            elif line[0] == "stop":
                break
            elif "mov" in line[0]:
                if "i" in line[0]:
                    registers[ActiveRegister] = int(line[1])
                else:
                    registers[ActiveRegister] = registers[line[1]]
            else:
                if RunArthmeticInstruction(line, None if 'i' not in line[0] else int(line[1])):
                    continue
                else:
                    break
    print(registers)
except IOError as error:
    print(error)
    