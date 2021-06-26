two_operand = {
    '100010': 'mov',
    '000000': 'add',
    '000100': 'adc',
    '001110': 'cmp',
    "100001": ["test",'xchg'],
    ("100001","0", "1"):"test", 
    ("100001","1","1"):"xchg", 
    '00001111101011': 'imul',
    '001100': 'xor',
    '00001111110000': 'xadd',
    "00001111101111": ["bsf",'bsr'],
    ("00001111101111","0"):"bsf", 
    ("00001111101111","1"):"bsr", 
    '001010': 'sub',
    '000110': 'sbb',
    '001000': 'and', 
    '000010': 'or',
}

regCode = {
    "idiv": "111",
    "jmp" : "100",
    "inc" : "000",
    "dec" : "001",
    "shl" : "100",
    "shr" : "101",
    "neg" : "011",
    "not" : "010",
    "call": "010",
    "push": "110",
    "pop" : "000"
}

one_operand = {
    "111111": ["jmp" ,"dec", "inc", 'push'],
    ("111111", "100") : "jmp",
    ("111111", "001") : "dec",
    ("111111", "000") : "inc",
    ("111111", "110") : "push",
    '111101': ['not','neg', "idiv"],
    ("111101", "010") : "not",
    ("111101", "011") : "neg",
    ("111101", "111") : "idiv",
    "110100": ["shl0", "shr0"],
    ("110100", "100") : "shl",
    ("110100", "101") : "shr",
    ("110000", "100") : "shl",
    ("110000", "101") : "shr",
    "110000": ["shl1", "shr1"],
    '11101000': 'call',
    '11000011': 'ret',
    '10001111': 'pop',

}

no_operand = {
    'f9': 'stc',
    'f8': 'clc',
    'fd': 'std',
    'fc': 'cld',
    '0f05': 'syscall',
}

immediate = {
    '010': 'adc', 
    '100': 'and', 
    '001': 'or', 
    '000': 'add', 
    '111': 'cmp', 
    '011': 'sbb', 
    '101': 'sub', 
    '110': 'xor'
}

size = {
    8: "BYTE", 
    16: "WORD", 
    32: "DWORD", 
    64: "QWORD"
}

register_bits = {
    "al" : 8,
    "ax" : 16,
    "eax" : 32,
    "rax" : 64,
    "cl" : 8,
    "cx" : 16,
    "ecx" : 32,
    "rcx" : 64,
    "dl" : 8,
    "dx" : 16,
    "edx" : 32,
    "rdx" : 64,
    "bl" : 8,
    "bx" : 16,
    "ebx" :32,
    "rbx" : 64,
    "ah" : 8,
    "sp" : 16,
    "esp" : 32,
    "rsp" : 64,
    "ch" : 8,
    "bp" : 16,
    "ebp" : 32,
    "rbp" : 64,
    "dh" : 8,
    "si" : 16,
    "esi" : 32,
    "rsi" : 64,
    "dh" : 8,
    "di" : 16,
    "edi" : 32,
    "rdi" : 64,
    #add r registers
    "r8b" : 8,
    "r8w" : 16,
    "r8d" : 32,
    "r8"  : 64,
    "r9b" : 8,
    "r9w" : 16,
    "r9d" : 32,
    "r9"  : 64,
    "r10b" : 8,
    "r10w" : 16,
    "r10d" : 32,
    "r10"  : 64,
    "r11b" : 8,
    "r11w" : 16,
    "r11d" : 32,
    "r11"  : 64,
    "r12b" : 8,
    "r12w" : 16,
    "r12d" : 32,
    "r12"  : 64,
    "r13b" : 8,
    "r13w" : 16,
    "r13d" : 32,
    "r13"  : 64,
    "r14b" : 8,
    "r14w" : 16,
    "r14d" : 32,
    "r14"  : 64,
    "r15b" : 8,
    "r15w" : 16,
    "r15d" : 32,
    "r15"  : 64,
}

Scale = {
    "00": "1",
    "01": "2",
    "10": "4",
    "11": "8"
}

hex_equal = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"
}
Reg ={
    ('0', '000', 8): 'al',
    ('0', '000', 16): 'ax',
    ('0', '000', 32): 'eax',
    ('0', '000', 64): 'rax',
    ('0', '001', 8): 'cl',
    ('0', '001', 16): 'cx',
    ('0', '001', 32): 'ecx',
    ('0', '001', 64): 'rcx',
    ('0', '010', 8): 'dl',
    ('0', '010', 16): 'dx',
    ('0', '010', 32): 'edx',
    ('0', '010', 64): 'rdx',
    ('0', '011', 8): 'bl',
    ('0', '011', 16): 'bx',
    ('0', '011', 32): 'ebx',
    ('0', '011', 64): 'rbx',
    ('0', '100', 8): 'ah',
    ('0', '100', 16): 'sp',
    ('0', '100', 32): 'esp',
    ('0', '100', 64): 'rsp',
    ('0', '101', 8): 'ch',
    ('0', '101', 16): 'bp',
    ('0', '101', 32): 'ebp',
    ('0', '101', 64): 'rbp',
    ('0', '110', 8): 'dh',
    ('0', '110', 16): 'si',
    ('0', '110', 32): 'esi',
    ('0', '110', 64): 'rsi',
    ('0', '111', 8): 'bh',
    ('0', '111', 16): 'di',
    ('0', '111', 32): 'edi',
    ('0', '111', 64): 'rdi',
    ('1', '000', 8): 'r8b',
    ('1', '000', 16): 'r8w',
    ('1', '000', 32): 'r8d',
    ('1', '000', 64): 'r8',
    ('1', '001', 8): 'r9b',
    ('1', '001', 16): 'r9w',
    ('1', '001', 32): 'r9d',
    ('1', '001', 64): 'r9',
    ('1', '010', 8): 'r10b',
    ('1', '010', 16): 'r10w', 
    ('1', '010', 32): 'r10d',
    ('1', '010', 64): 'r10',
    ('1', '011', 8): 'r11b',
    ('1', '011', 16): 'r11w',
    ('1', '011', 32): 'r11d',
    ('1', '011', 64): 'r11',
    ('1', '100', 8): 'r12b',
    ('1', '100', 16): 'r12w',
    ('1', '100', 32): 'r12d',
    ('1', '100', 64): 'r12',
    ('1', '101', 8): 'r13b',
    ('1', '101', 16): 'r13w',
    ('1', '101', 32): 'r13d',
    ('1', '101', 64): 'r13',
    ('1', '110', 8): 'r14b',
    ('1', '110', 16): 'r14w',
    ('1', '110', 32): 'r14d',
    ('1', '110', 64): 'r14',
    ('1', '111', 8): 'r15b',
    ('1', '111', 16): 'r15w',
    ('1', '111', 32): 'r15d',
    ('1', '111', 64): 'r15'
    }

def hex2bin(hex):
    answer = ""
    for i in hex:
        answer += hex_equal[i]
    
    return answer


def Process_Code(code):
    code_dict = {}
    if code[0:2] == "67":
        code_dict["address-size"] = 32
        code = code[2::]
    if code[0:2] == "66":
        code_dict["operand-size"] = 16
        code = code[2::]
    binary_code = hex2bin(code)
    if binary_code[0:4] == "0100":
        code_dict["Rex"] = "0100"
        code_dict["Rex_W"] = binary_code[4]
        code_dict["Rex_R"] = binary_code[5]
        code_dict["Rex_X"] = binary_code[6]
        code_dict["Rex_B"]= binary_code[7]
        binary_code = binary_code[8::]
    else:
        code_dict["Rex_W"] = "0"
        code_dict["Rex_R"] = "0"
        code_dict["Rex_X"] = "0"
        code_dict["Rex_B"]= "0"
    if binary_code[0:8] == "00001111":
        code_dict["Opcode"] = binary_code[0:14]
        binary_code = binary_code[14::]
    else:
        code_dict["Opcode"] = binary_code[0:6]
        binary_code = binary_code[6::]
    code_dict["D"] = binary_code[0]
    code_dict["W"] = binary_code[1]
    code_dict["mod"] = binary_code[2:4]
    code_dict["reg"] = binary_code[4:7]
    code_dict["R/M"] = binary_code[7:10]
    binary_code = binary_code[10::]
    if code_dict["R/M"] == "100" and code_dict["mod"] != "11":
        code_dict["SS"] = binary_code[0:2]
        code_dict["Inx"] = binary_code[2:5]
        code_dict["Bas"] = binary_code[5:8]
        binary_code = binary_code[8::]
    
    if binary_code != "":
        disp = ""
        i = len(binary_code)
        i = i // 4
        j = len(code)-1
        i = j - i
        while j > i:
            disp += code[j-1:j+1]
            j -= 2
        if code_dict["Opcode"] == "110000":
            shift_count = disp[0:2]
            if shift_count[0] == "0":
                shift_count = shift_count[1::]
            code_dict["shift_count"] = "0x"+shift_count
            disp = disp[2::] 
        elif code_dict["Opcode"] == "110100":
            code_dict["shift_count"] = "1"
        if disp != "":
            while disp != "" and disp[0] == "0" :
                disp = disp[1::]
            if disp == "":
                disp = "0"
            disp = "0x" + disp
            code_dict["Disp"] = disp
    
    return code_dict

def find_operand_size(code_dict):
    operand_size = 0
    if code_dict.get("operand-size") != None:
        operand_size = 16
    if code_dict.get("Rex") != None and operand_size == 0:
        if code_dict["Rex_W"] == "1":
            operand_size = 64
    if code_dict["W"] == "1" and operand_size == 0:
        operand_size = 32
    if operand_size == 0:
        operand_size = 8
    
    return operand_size

def find_address_size(code_dict):
    address_size = 0
    if code_dict.get("address-size") != None:
        address_size = 32
    else:
        address_size = 64
    
    return address_size


def calc(code_dict):
    operand = ""
    part1 = ""
    operand_size = find_operand_size(code_dict)
    address_size = find_address_size(code_dict)       


    if two_operand.get(code_dict["Opcode"]) != None:
        part2 = ""
        if  type(two_operand.get(code_dict["Opcode"])) != type([]):
            operand = two_operand[code_dict["Opcode"]]
        else:
            if two_operand.get((code_dict["Opcode"], code_dict["W"])) != None:
                operand = two_operand[(code_dict["Opcode"], code_dict["W"])]
            else:
                operand = two_operand[(code_dict["Opcode"], code_dict["D"], "1")]
        if operand == "bsf" or operand == "bsr":
            if operand_size == 8:
                operand_size = 32
        if code_dict["mod"] == "11":
            part1 = Reg[(code_dict["Rex_B"], code_dict["R/M"], operand_size)]
            part2 = Reg[(code_dict["Rex_R"], code_dict["reg"], operand_size)]
            if operand == "bsf" or operand == "bsr" or operand == "imul":
                temp = part1
                part1 = part2
                part2 = temp
                
        else:
            if code_dict.get("R/M") != "100":
                part1 = Reg[(code_dict["Rex_R"], code_dict["reg"], operand_size)]
                part2 = size[operand_size] + " PTR " + "["
                part2 += Reg[(code_dict["Rex_B"], code_dict["R/M"], address_size)]
                if code_dict.get("Disp") != None:
                    part2 += "+" + code_dict["Disp"]
                part2 += "]"
                if code_dict["D"] == "0" and operand != "bsf" and operand != "bsr":
                    temp = part1
                    part1 = part2
                    part2 = temp
            else:
                part1 = Reg[(code_dict["Rex_R"], code_dict["reg"], operand_size)]
                part2 = size[operand_size] + " PTR " + "["
                if not(code_dict["Bas"] == "101" and code_dict["mod"] == "00"):
                    part2 += Reg[(code_dict["Rex_B"], code_dict["Bas"], address_size)]
                if not(code_dict["Inx"] == "100" and code_dict["Rex_X"] == "0"):
                    if part2[-1] != "[":
                        part2 += "+"
                    part2 += Reg[(code_dict["Rex_X"], code_dict["Inx"], address_size)]
                    part2 += "*" + Scale[code_dict["SS"]]
                if code_dict.get("Disp") != None:
                    if part2[-1] != "[":
                        part2 += "+"
                    part2 += code_dict["Disp"]
                part2 += "]"
                if code_dict["D"] == "0" and operand != "bsf" and operand != "bsr":
                    temp = part1
                    part1 = part2
                    part2 = temp
        return operand + " " + part1 + ","+ part2 
    
    elif one_operand.get(code_dict["Opcode"]) != None: 
        if  type(one_operand.get(code_dict["Opcode"])) != type([]):
            operand = one_operand[code_dict["Opcode"]]
        else:
            operand = one_operand[(code_dict["Opcode"], code_dict["reg"])]
        if operand == "call" or operand == "push" or operand == "pop" or operand == "jmp":
            operand_size = 64
        
        if code_dict["mod"] == "11":
            part1 = Reg[(code_dict["Rex_B"], code_dict["R/M"], operand_size)]
            if operand == "shr" or operand == "shl":
                part1 += ","
                if code_dict.get("shift_count") != None:
                    part1 += code_dict["shift_count"]
                else:
                   part1+= "1"
        else:
            if code_dict["R/M"] != "100":
                part1 = size[operand_size] + " PTR " + "["
                part1 += Reg[(code_dict["Rex_B"], code_dict["R/M"], address_size)]
                if code_dict.get("Disp") != None:
                    part1 += "+" + code_dict["Disp"]
                part1 += "]"
            else:
                part1 = size[operand_size] + " PTR " + "["
                if not(code_dict["Bas"] == "101" and code_dict["mod"] == "00"):
                    part1 += Reg[(code_dict["Rex_B"], code_dict["Bas"], address_size)]
                if not(code_dict["Inx"] == "100" and code_dict["Rex_X"] == "0"):
                    if part1[-1] != "[":
                        part1 += "+"
                    part1 += Reg[(code_dict["Rex_X"], code_dict["Inx"], address_size)]
                    part1 += "*" + Scale[code_dict["SS"]]
                if code_dict.get("Disp") != None:
                    if part1[-1] != "[":
                        part1 += "+"
                    part1 += code_dict["Disp"]
                part1 += "]"
        
            if code_dict.get("shift_count") != None:
                if code_dict["shift_count"][0:2] == "0x":
                    part1 +="," + code_dict["shift_count"]
                else:
                    part1 +="," + code_dict["shift_count"]
        return operand + " " + part1
    elif code_dict["Opcode"] == "100000":
        operand = immediate[code_dict["reg"]]
        part1 = Reg[(code_dict["Rex_B"], code_dict["R/M"], operand_size)]
        part2 = code_dict["Disp"]
        return operand + " " + part1 + "," + part2
    elif code_dict["Opcode"] == "111101":
        operand = "test"
        part1 = Reg[(code_dict["Rex_B"], code_dict["R/M"], operand_size)]
        part2 = code_dict["Disp"]
        return operand + " " + part1 + "," + part2 
    elif code_dict["Opcode"] == "11010":
        operand = "jmp"
        part1 = Reg[(code_dict["Rex_B"], code_dict["R/M"], operand_size)]
        part2 = code_dict["Disp"]
        return operand + " " + part1 + "," + part2 
        
    #elif code_dict["Opcode"][0:4] == "0111":


code = input()
if  no_operand.get(code) != None:
    print(no_operand[code])

else:
    print(calc(Process_Code(code)))
