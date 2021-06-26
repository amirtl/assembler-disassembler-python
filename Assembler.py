opCode = {
    "mov" : "100010",
    "add" : "000000",
    "adc" : "000100",
    "cmp" : "001110",
    "test": "100001",
    "imul": "00001111101011",
    "xor" : "001100",
    "xadd": "00001111110000",
    "bsf" : "00001111101111",
    "bsr" : "00001111101111",
    "idiv": "111101",
    "stc" : "11111001",
    "jmp" : "111111",
    "xchg": "100001",
    "sub" : "001010",
    "sbb" : "000110",
    "inc" : "111111",
    "dec" : "111111",
    "shl0": "110100",
    "shl1": "110000",
    "shr0": "110100",
    "shr1": "110000",
    "neg" : "111101",
    "not" : "111101",
    "call": "11101000",
    "ret" : "11000011",
    "push": "111111",
    "pop" : "10001111",
    "clc" : "11111000",
    "std" : "11111101",
    "cld" : "11111100",
    "syscall" : "0000111100000101",
    "and": "001000" ,
    "or" : "000010" ,
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

tttnCode = {
    "jo" : "0000",
    "jno": "0001",
    "jb" : "0010",
    "jnae": "0010",
    "jnb" : "0011",
    "jae" : "0011",
    "je"  : "0100",
    "jz"  : "0100",
    "jne" : "0101",
    "jnz" : "0101",
    "jbe" : "0110",
    "jna" : "0110",
    "jnbe": "0111",
    "ja"  : "0111",
    }

jcc = {
    "jo", 
    "jno",
    "jb" ,
    "jnae",
    "jnb",
    "jae",
    "je" ,
    "jz" ,
    "jne",
    "jnz" ,
    "jbe",
    "jna" ,
    "jnbe",
    "ja"  ,
}

size = {
     "BYTE" : 8, 
     "WORD" : 16, 
     "DWORD": 32, 
     "QWORD" : 64
}

immediate = {
    "adc" : "010",
    "and" : "100",
    "or" : "001",
    "add" : "000",
    "test": "000",
    "cmp" : "111",
    "sbb" : "011",
    "sub" : "101",
    "xor" : "110",
}

Reg_W = {
    64 : "1",
    32:"1",
    16:"1",
    8:"0",
    }

Rex_W = {
    64 : "1",
    32:"0",
    16:"0",
    8:"0",
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

#add op_prefix
op_prefix = {
    8 : "",
    32 : "",
    16 : "66",
    64 : ""
}

address_prefix = {
    16: "66",
    8 : "",
    32 : "67",
    (8,8) : "",
    (16, 8) : "",
    (8, 16) : "",
    (8,32) : "",
    (32,8) : "",
    (32, 64) : "",
    (32, 32) : "67",
    (16, 64) : "66",
    (16, 32) : "6766",
    ("0", 32) : "",
    ("0", 8, 64) : "",
    ("0", 32, 64) : "",
    ("0", 32, 32) : "67",
    ("0", 16, 64) : "66",
    ("0", 16, 32) : "6766",
    ("1", 16,64)  : "66",
    ("1", 16,32)  : "6766",
    ("1", 64,64)  : "",
    ("1",64,32)  : "67",
    ("0", 64, 64): "",
    ("1", 64) : "",
    ("0", 8) : "",
    ("0", 16) : "66",
    ("0", 32) : "",
    ("0", 64) : "",


}

Reg = {
    "al" : "000",
    "ax" : "000",
    "eax" : "000",
    "rax" : "000",
    "cl" : "001",
    "cx" : "001",
    "ecx" :"001",
    "rcx" : "001",
    "dl" : "010",
    "dx" : "010",
    "edx" :"010",
    "rdx" : "010",
    "bl" : "011",
    "bx" : "011",
    "ebx" :"011",
    "rbx" : "011",
    "ah" : "100",
    "sp" : "100",
    "esp" : "100",
    "rsp" : "100",
    "ch" : "101",
    "bp" : "101",
    "ebp" : "101",
    "rbp" : "101",
    "dh" : "110",
    "si" : "110",
    "esi" : "110",
    "rsi" : "110",
    "bh" : "111",
    "di" : "111",
    "edi" : "111",
    "rdi" : "111",
    #add r registers
    "r8b" : "000",
    "r8w" : "000",
    "r8d" : "000",
    "r8"  : "000",
    "r9b" : "001",
    "r9w" : "001",
    "r9d" : "001",
    "r9"  : "001",
    "r10b" : "010",
    "r10w" : "010",
    "r10d" : "010",
    "r10"  : "010",
    "r11b" : "011",
    "r11w" : "011",
    "r11d" : "011",
    "r11"  : "011",
    "r12b" : "100",
    "r12w" : "100",
    "r12d" : "100",
    "r12"  : "100",
    "r13b" : "101",
    "r13w" : "101",
    "r13d" : "101",
    "r13"  : "101",
    "r14b" : "110",
    "r14w" : "110",
    "r14d" : "110",
    "r14"  : "110",
    "r15b" : "111",
    "r15w" : "111",
    "r15d" : "111",
    "r15"  : "111",
}

mod = {
    0:"00", 
    8:"01", 
    16: "10", 
    32: "10",
    "reg":"11"
    }

Scale = {
    "1": "00",
    "2": "01",
    "4": "10",
    "8": "11"
}

Index = {
    "eax" : "000",
    "ecx" :"001",
    "edx" :"010",
    "ebx" :"011",
    "Illegal" : "100",
    "ebp" : "101",
    "esi" : "110",
    "edi" : "111",
}

Base = {
    "eax" : "000",
    "ecx" :"001",
    "edx" :"010",
    "ebx" :"011",
    "esp" : "100",
    "ebp" : "101",
    "esi" : "110",
    "edi" : "111",
}

registers = [
    "al","ah","ax", "eax", "rax",
    "bl","bh","bx", "ebx", "rbx",
    "cl","ch","cx", "ecx", "rcx",
    "dl","dh","dx", "edx", "rdx",
    "sp", "esp", "rsp",
    "bp", "ebp", "rbp",
    "si", "esi", "rsi",
    "di", "edi", "rdi",
    "r8b", "r8w", "r8d", "r8",
    "r9b", "r9w", "r9d", "r9",
    "r10b", "r10w", "r10d", "r10",
    "r11b", "r11w", "r11d", "r11",
    "r12b", "r12w", "r12d", "r12",
    "r13b", "r13w", "r13d", "r13",
    "r14b", "r14w", "r14d", "r14",
    "r15b", "r15w", "r15d", "r15",
    ]


def is_new(register):
    if register[1] == "8" or register[1] == "9" or register[1] == "1":
        return "1"
    else:
        return "0"

def classify(operand, part1, part2):
    code_dict = {}
    if part1 in registers:
        code_dict["D"] = "1"
        code_dict["W"] = Reg_W[register_bits[part1]]
        if operand == "bsf":
            code_dict["D"] = "0"
            code_dict["W"] = "0"
        if operand == "bsr":
            code_dict["D"] = "0"
            code_dict["W"] = "1"
        if operand == "test":
            code_dict["D"] = "0"
        code_dict["reg"] = part1
        code_dict["type1"] = "register"
        if part1[0] == "r":
            code_dict["Rex"] = "0100"
            code_dict["Rex_W"] = Rex_W[register_bits[part1]]
            code_dict["Rex_R"] = is_new(part1)
        address = part2
    else:
        code_dict["D"] = "0"
        if operand == "xchg" or operand == "imul":
            code_dict["D"] = "1"
        code_dict["W"] = Reg_W[register_bits[part2]]
        code_dict["reg"] = part2
        code_dict["type1"] = "register"
        if part2[0] == "r":
            code_dict["Rex"] = "0100"
            code_dict["Rex_W"] = Rex_W[register_bits[part2]]
            code_dict["Rex_R"] = is_new(part2)
        address = part1
    if address in registers:
        code_dict["type2"] = "register"
        code_dict["D"] = "0"
        if operand == "xchg" or operand == "imul":
            code_dict["D"] = "1"
        code_dict["mod"] = "11"
        code_dict["reg"] = address
        code_dict["R/M"] = part1
        if operand == "imul" or operand == "bsr" or operand == "bsf":
            code_dict["reg"] = part1
            code_dict["R/M"] = address
            code_dict["Rex_R"] = is_new(address)
            code_dict["Rex_B"] = is_new(part1)
        if code_dict.get("Rex") == None:
            if address[0] == "r":
                code_dict["Rex"] = "0100"
                code_dict["Rex_W"] = Rex_W[register_bits[code_dict["R/M"]]]
                code_dict["Rex_R"] = is_new(address)
                code_dict["Rex_B"] = is_new(part1)
                code_dict["Rex_X"] = "0"
        else:
            code_dict["Rex_R"] = is_new(address)
            code_dict["Rex_B"] = is_new(part1)
            code_dict["Rex_X"] = "0"
        if operand == "imul" or operand == "bsr" or operand == "bsf":
            code_dict["reg"] = part1
            code_dict["R/M"] = address
            if code_dict.get("Rex") != None:
                code_dict["Rex_R"] = is_new(part1)
                code_dict["Rex_B"] = is_new(address)
    elif address[0:2] == "0x" or address.isdigit():
        if address.isdigit():
            address = hex(int(address))
        code_dict["type2"] = "immediate"
        code_dict["mod"] = "11"
        if code_dict.get("Rex") != None:
            code_dict["Rex_R"] = "0"
            code_dict["Rex_B"] = is_new(part1)
            code_dict["Rex_X"] = "0"
        code_dict["S"] = "0"
        if operand == "mov" or operand == "test":
            code_dict["S"] = "1"
        if register_bits[code_dict["reg"]] > 8 and (len(address)-2) <= 2:
            code_dict["S"] = "1"
        disp = ""
        if len(address) % 2 == 1:
            address = "0x0" + address[2::]
        i = len(address)
        while address[i-1] != "x":
            disp += address[i-2: i] 
            i -= 2
        bytes = register_bits[code_dict["reg"]]//8
        if bytes == 4:
            bytes = 8
        if len(disp) != 2:
            while len(disp) < bytes :
                disp += "0"
        code_dict["immData"] = disp
    else:
        code_dict["memory_bytes"], address = find_size(address)
        address = address[1:-1]
        address = address.split("+")
        if len(address) == 1:
            if address[0][0:2] == "0x":
                code_dict["type2"] = "memory2"
                code_dict["mod"] = "00"
                code_dict["R/M"] = "100"
                code_dict["SS"] = "00"
                code_dict["Inx"] = "esp"
                code_dict["Bas"] = "ebp"
                if code_dict.get("Rex") != None:
                    code_dict["Rex_B"] = "0"
                    code_dict["Rex_X"] = "0"
                    code_dict["Inx"] = "rsp"
                    code_dict["Bas"] = "rbp"
                disp = ""
                if len(address[0]) % 2 == 1:
                    address[0] = "0x0" + address[0][2::]
                i = len(address[0])
                while address[0][i-1] != "x":
                    disp += address[0][i-2: i] 
                    i -= 2
                bytes = register_bits[code_dict["reg"]]//8
                if bytes == 4:
                    bytes = 8
                while len(disp) < bytes :
                    disp += "0"
                code_dict["Disp"] = disp
            elif address[0] in registers:
                code_dict["type2"] = "memory1"
                if code_dict.get("Rex") == None:
                    if int(is_new(address[0])):
                        code_dict["Rex"] = "0100"
                        code_dict["Rex_W"] = Rex_W[register_bits[code_dict["reg"]]]
                        code_dict["Rex_R"] = is_new(code_dict["reg"])
                        code_dict["Rex_B"] = is_new(address[0])
                        code_dict["Rex_X"] = "0"
                else:
                    code_dict["Rex_B"] = is_new(address[0])
                    code_dict["Rex_X"] = "0"
                
                code_dict["mod"] = "00"
                code_dict["R/M"] = address[0]
                if address[0] == "ebp" or address[0] == "rbp":
                    code_dict["Disp"] = "00"
                    code_dict["mod"] = "01"
            else:
                code_dict["type2"] = "memory2"
                code_dict["R/M"] = "100"
                code_dict["Bas"] = "ebp"
                code_dict["mod"] = "00"
                code_dict["Disp"] = "00000000"
                a = address[0].split("*")
                if code_dict.get("Rex") == None:
                    if int(is_new(a[0])):
                        code_dict["Rex"] == "0100"
                        code_dict["Rex_W"] = Rex_W[register_bits[part1]]
                        code_dict["Rex_R"] = "0"
                        code_dict["Rex_X"] = is_new(a[0])
                        code_dict["Rex_B"] = "0"
                else:
                    code_dict["Rex_X"] = is_new(a[0])
                    code_dict["Rex_B"] = "0"
                if a[0][0] == "r":
                        code_dict["Bas"] = "rbp"
                code_dict["Inx"] = a[0]
                if len(a) == 2:
                    code_dict["SS"] = Scale[a[1]]
                else:
                    code_dict["SS"] = "00"
        elif len(address) == 2:
            code_dict["type2"] = "memory2"
            if address[0] in registers:
                if address[1][0:2] == "0x":
                    code_dict["type2"] = "memory1"
                    code_dict["R/M"] = address[0]
                    if code_dict.get("Rex") == None:
                        if int(is_new(address[0])):
                            code_dict["Rex"] = "0100"
                            code_dict["Rex_W"] = "0"
                            code_dict["Rex_R"] = "0"
                            code_dict["Rex_X"] = "0"
                            code_dict["Rex_B"] = is_new(address[0])
                    else:
                        code_dict["Rex_X"] = "0"
                        code_dict["Rex_B"] = is_new(address[0])
                    disp = ""
                    if len(address[1]) % 2 == 1:
                        address[1] = "0x0" + address[1][2::]
                    i = len(address[1])
                    while address[1][i-1] != "x":
                        disp += address[1][i-2: i] 
                        i -= 2
                    if len(disp) >= 4 :
                        while len(disp) != 8:
                            disp += "0"
                    code_dict["Disp"] = disp
                    code_dict["mod"] = mod[len(disp)*4]
                else:
                    code_dict["R/M"] = "100"
                    code_dict["Bas"] = address[0]
                    if code_dict.get("Rex") == None:
                        if int(is_new(address[0])):
                            code_dict["Rex"] = "0100"
                            code_dict["Rex_W"] = "0"
                            code_dict["Rex_R"] = "0"
                            code_dict["Rex_X"] = "0"
                            code_dict["Rex_B"] = is_new(address[0])
                    else:
                        code_dict["Rex_X"] = "0"
                        code_dict["Rex_B"] = is_new(address[0])
                    
                    a = address[1].split("*")
                    code_dict["Inx"] = a[0]
                    if code_dict.get("Rex") == None:
                        if int(is_new(a[0])):
                            code_dict["Rex"] = "0100"
                            code_dict["Rex_W"] = "0"
                            code_dict["Rex_R"] = "0"
                            code_dict["Rex_X"] = is_new(a[0])
                            code_dict["Rex_B"] = "0"
                    else:
                        code_dict["Rex_X"] = is_new(a[0])
                    code_dict["mod"] = "00"
                    if len(a) == 2:
                        code_dict["SS"] = Scale[a[1]]
                    else:
                        code_dict["SS"] = "00"
                    if address[0] == "ebp" or address[0] == "rbp":
                        code_dict["Disp"] = "00"
                        code_dict["mod"] = "01"
            else:
                code_dict["mod"] = "00"
                code_dict["R/M"] = "100"
                code_dict["Bas"] = "ebp"
                a = address[0].split("*")
                code_dict["Inx"] = a[0]
                if code_dict.get("Rex") == None:
                    if int(is_new(a[0])):
                        code_dict["Rex"] = "0100"
                        code_dict["Rex_W"] = "0"
                        code_dict["Rex_R"] = "0"
                        code_dict["Rex_X"] = is_new(a[0])
                        code_dict["Rex_B"] = "0"
                else:
                    code_dict["Rex_X"] = is_new(a[0])
                    code_dict["Rex_B"] = "0"
                if a[0][0] == "r":
                        code_dict["Bas"] = "rbp"
                if len(a) == 2:
                    code_dict["SS"] = Scale[a[1]]
                else:
                    code_dict["SS"] = "00"
                disp = ""
                if len(address[1]) % 2 == 1:
                    address[1] = "0x0" + address[1][2::]
                i = len(address[1])
                while i != 2:
                    disp += address[1][i-2: i] 
                    i -= 2
                while len(disp) != 8:
                    disp += "0"
                code_dict["Disp"] = disp
        else:
            code_dict["type2"] = "memory2"
            code_dict["R/M"] = "100"
            code_dict["Bas"] = address[0]
            if code_dict.get("Rex") == None:
                if int(is_new(address[0])):
                    code_dict["Rex"] = "0100"
                    code_dict["Rex_W"] = "0"
                    code_dict["Rex_R"] = "0"
                    code_dict["Rex_B"] = is_new(address[0])
            else:
                code_dict["Rex_B"] = is_new(address[0])
            a = address[1].split("*")
            code_dict["Inx"] = a[0]
            if code_dict.get("Rex") == None:
                if int(is_new(a[0])):
                    code_dict["Rex"] = "0100"
                    code_dict["Rex_W"] = "0"
                    code_dict["Rex_R"] = "0"
                    code_dict["Rex_B"] = "0"
                    code_dict["Rex_X"] = is_new(a[0])
            else:
                code_dict["Rex_X"] = is_new(a[0])
            if len(a) == 2:
                code_dict["SS"] = Scale[a[1]]
            else:
                code_dict["SS"] = "00"
            disp = ""
            if len(address[2]) % 2 == 1:
                address[2] = "0x0" + address[2][2::]
            i = len(address[2])
            while address[2][i-1] != "x":
                disp += address[2][i-2: i] 
                i -= 2
            if len(disp) >= 4 :
                while len(disp) != 8:
                    disp += "0"
            code_dict["Disp"] = disp
            code_dict["mod"] = mod[len(disp)*4]

    return code_dict

def bin2hex(string):
    output = ""
    i = 0
    while i < len(string):
        output += hex(int(string[i:i+4], 2))[2:]
        i += 4
    return output

def calc(operand, part1, part2):
    output = ""
    code_dict = classify(operand, part1, part2)
    if code_dict["type1"] == "register":
        if code_dict["type2"] == "register":
            if code_dict.get("Rex") != None:
                output = code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"]
                output += opCode[operand] + code_dict["D"] + code_dict["W"] + code_dict["mod"] + Reg[code_dict["reg"]] + Reg[code_dict["R/M"]]
                output = bin2hex(output)
                output = address_prefix[(code_dict["Rex_W"],register_bits[code_dict["R/M"]])] + output
            else: 
                output = opCode[operand]+ code_dict["D"] + code_dict["W"] + code_dict["mod"] + Reg[code_dict["reg"]] + Reg[code_dict["R/M"]] 
                output = bin2hex(output)
                output = op_prefix[register_bits[part1]] + output
        elif code_dict["type2"] == "immediate":
            if code_dict.get("Rex") != None:
                output += code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"]
            if operand == "mov":
                output = "1011" + code_dict["W"] + Reg[code_dict["reg"]]
            elif operand == "test":
                output += "111101"  + code_dict["S"] + code_dict["W"] + "11" + immediate[operand] + Reg[code_dict["reg"]]
            else:
                output += "100000" + code_dict["S"] + code_dict["W"] + "11" + immediate[operand] + Reg[code_dict["reg"]]
            output = bin2hex(output)
            output += code_dict["immData"]
            output = op_prefix[register_bits[code_dict["reg"]]] + output
        elif code_dict["type2"] == "memory1":
            if code_dict.get("Rex") != None:
                output = code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"] 
                output += opCode[operand] + code_dict["D"] + code_dict["W"] + code_dict["mod"] + Reg[code_dict["reg"]] + Reg[code_dict["R/M"]]
                output = bin2hex(output)
                if code_dict.get("Disp") != None:
                    output += code_dict["Disp"]
                output = address_prefix[(code_dict["Rex_W"],register_bits[code_dict["reg"]], register_bits[code_dict["R/M"]])] + output
            else:
                output = opCode[operand] + code_dict["D"] + code_dict["W"] + code_dict["mod"] + Reg[code_dict["reg"]] + Reg[code_dict["R/M"]]
                output = bin2hex(output)
                if code_dict.get("Disp") != None:
                    output += code_dict["Disp"]
                output = address_prefix[(register_bits[code_dict["reg"]],register_bits[code_dict["R/M"]])] + output
        elif code_dict["type2"] == "memory2":
            if code_dict.get("Rex") != None:
                output = code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"] + opCode[operand] + code_dict["D"] + code_dict["W"] + code_dict["mod"] + Reg[code_dict["reg"]] + code_dict["R/M"] + code_dict["SS"] + Reg[code_dict["Inx"]] + Reg[code_dict["Bas"]]
                output = bin2hex(output)
                if code_dict.get("Disp") != None:
                    output += code_dict["Disp"]
                if not(code_dict.get("Disp") != None and Reg[code_dict["Inx"]] == "100" and Reg[code_dict["Bas"]] == "101"):
                    output = address_prefix[(code_dict["Rex_W"],register_bits[code_dict["reg"]], register_bits[code_dict["Bas"]])] + output
            else:
                output = opCode[operand] + code_dict["D"] + code_dict["W"] + code_dict["mod"] + Reg[code_dict["reg"]] + code_dict["R/M"] + code_dict["SS"] + Reg[code_dict["Inx"]] + Reg[code_dict["Bas"]]
                output = bin2hex(output)
                if code_dict.get("Disp") != None:
                    output += code_dict["Disp"]
                if not(code_dict.get("Disp") != None and Reg[code_dict["Inx"]] == "100" and Reg[code_dict["Bas"]] == "101"):
                    output = address_prefix[(register_bits[code_dict["reg"]],register_bits[code_dict["Bas"]])] + output
        

    print(output)


def calc_one(operand, part1):
    output = ""
    code_dict = classify_one(operand, part1)
    if code_dict["type"] == "register":
        if code_dict.get("Rex") != None:
            output = code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"]
            if operand == "call":
                    output += "1111111111010" + Reg[code_dict["R/M"]]
            elif operand == "push":
                output += "1111111111110" + Reg[code_dict["R/M"]]
            elif operand == "pop":
                output += "01011" + Reg[code_dict["R/M"]]
            elif operand == "shr" or operand == "shl":
                if shift_count != "":
                    output += opCode[operand+"1"]
                else:
                    output += opCode[operand+"0"]
                output += code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + Reg[code_dict["R/M"]] 
            else:    
                output += opCode[operand] + code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + Reg[code_dict["R/M"]]
            output = bin2hex(output)
            output = address_prefix[(code_dict["Rex_W"],register_bits[code_dict["R/M"]])] + output
        else: 
            if operand == "call":
                    output += "1111111111010" + Reg[code_dict["R/M"]]
            elif operand == "shr" or operand == "shl":
                if shift_count != "":
                    output += opCode[operand+"1"]
                else:
                    output += opCode[operand+"0"]
                output += code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + Reg[code_dict["R/M"]]
            else:    
                output = opCode[operand]+ code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + Reg[code_dict["R/M"]]
            output = bin2hex(output)
            output = op_prefix[register_bits[part1]] + output
    elif code_dict["type"] == "immediate":
        if operand == "jmp":
            output = "111010" + code_dict["D"] + "1"
        elif operand in jcc:
            if  len(code_dict["immData"]) == 2:
                output += "0111" + tttnCode[operand]
            else:
                output += "000011111000" + tttnCode[operand]
        elif operand == "jrcxz":
            output += "11100011"
        else:
            output += opCode[operand]
        output = bin2hex(output)
        output += code_dict["immData"]
        #output = op_prefix[register_bits[code_dict["reg"]]] + output
    elif code_dict["type"] == "memory1":
        if code_dict.get("Rex") != None:
            output = code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"] 
            if operand == "shr" or operand == "shl":
                if shift_count != "":
                    output += opCode[operand+"1"]
                else:
                    output += opCode[operand+"0"]
            else:
                output += opCode[operand]
            output += code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + Reg[code_dict["R/M"]]
            output = bin2hex(output)
            if code_dict.get("Disp") != None:
                output += code_dict["Disp"]
            output = address_prefix[(code_dict["Rex_W"], code_dict["memory_bytes"], register_bits[code_dict["R/M"]])] + output
        else:
            if operand == "shr" or operand == "shl":
                if shift_count != "":
                    output += opCode[operand+"1"]
                else:
                    output += opCode[operand+"0"]
            else:
                output+=opCode[operand]
            
            output += code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + Reg[code_dict["R/M"]]
            output = bin2hex(output)
            if code_dict.get("Disp") != None:
                output += code_dict["Disp"]
            output = address_prefix[(code_dict["memory_bytes"], register_bits[code_dict["R/M"]])] + output
    elif code_dict["type"] == "memory2":
        if code_dict.get("Rex") != None:
            output = code_dict["Rex"] + code_dict["Rex_W"] + code_dict["Rex_R"] + code_dict["Rex_X"] + code_dict["Rex_B"] 
            if operand == "shr" or operand == "shl":
                if shift_count != "":
                    output += opCode[operand+"1"]
                else:
                    output += opCode[operand+"0"]
            else:
                output += opCode[operand]
            output += code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand] + code_dict["R/M"] + code_dict["SS"] + Reg[code_dict["Inx"]] + Reg[code_dict["Bas"]]
            output = bin2hex(output)
            if code_dict.get("Disp") != None:
                output += code_dict["Disp"] 
            output = address_prefix[(code_dict["Rex_W"],code_dict["memory_bytes"], register_bits[code_dict["Bas"]])] + output
        else:
            if operand == "shr" or operand == "shl":
                if shift_count != "":
                    output += opCode[operand+"1"]
                else:
                    output += opCode[operand+"0"]
            else:
                output += opCode[operand]
            output += code_dict["D"] + code_dict["W"] + code_dict["mod"] + regCode[operand]+ code_dict["R/M"] + code_dict["SS"] + Reg[code_dict["Inx"]] + Reg[code_dict["Bas"]]
            output = bin2hex(output)
            if code_dict.get("Disp") != None:
                output += code_dict["Disp"]
            if code_dict.get("Disp") != None and Reg[code_dict["Inx"]] == "100" and Reg[code_dict["Bas"]] == "101":
                output = op_prefix[code_dict["memory_bytes"]] + output
            else:
                output = address_prefix[(code_dict["memory_bytes"],register_bits[code_dict["Bas"]])] + output
    

    if operand == "shr" or operand == "shl":
                output += shift_count
    print(output)


def classify_one(operand, part1):
    code_dict = {}
    if part1 in registers:
        code_dict["type"] = "register"
        if part1[0] == "r" :
            code_dict["Rex"] = "0100"
            code_dict["Rex_W"] =  Rex_W[register_bits[part1]]
            code_dict["Rex_R"] = "0"
            code_dict["Rex_X"] = "0"
            code_dict["Rex_B"] = is_new(part1)
            if operand == "call" or operand == "pop" or operand == "push":
                code_dict["Rex_W"] = "0"
        code_dict["mod"] = "11"   
        code_dict["D"] = "1"
        if operand == "shl" or operand == "shr":
            code_dict["D"] = "0"
        code_dict["W"] =  Reg_W[register_bits[part1]]
        code_dict["R/M"] = part1
    elif part1[0:2] == "0x" or part1.isdigit():
        if part1.isdigit():
            part1 = hex(int(part1))
        code_dict["type"] = "immediate"
        #code_dict["mod"] = "11"
        disp = ""
        if len(part1) % 2 == 1:
            part1 = "0x0" + part1[2::]
        i = len(part1)
        while part1[i-1] != "x":
            disp += part1[i-2: i] 
            i -= 2
        if len(disp) >= 4 :
            while len(disp) != 8:
                disp += "0"
        code_dict["immData"] = disp
        if len(disp) == 2:
            code_dict["D"] = "1"
        else:
            code_dict["D"] = "0"        
    else:
        code_dict["memory_bytes"], part1 = find_size(part1)
        part1 = part1[1:-1]
        part1 = part1.split("+")
        if len(part1) == 1:
            if part1[0][0:2] == "0x":
                code_dict["type"] = "memory2"
                code_dict["D"] = "1"
                code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
                code_dict["mod"] = "00"
                code_dict["R/M"] = "100"
                code_dict["SS"] = "00"
                code_dict["Inx"] = "esp"
                code_dict["Bas"] = "ebp"
                if code_dict["memory_bytes"] == 64:
                    code_dict["Rex"] = "0100"
                    code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                    code_dict["Rex_R"] = "0"
                    code_dict["Rex_B"] = "0"
                    code_dict["Rex_X"] = "0"
                    code_dict["Inx"] = "rsp"
                    code_dict["Bas"] = "rbp"
                disp = ""
                if len(part1[0]) % 2 == 1:
                    part1[0] = "0x0" + part1[0][2::]
                i = len(part1[0])
                while part1[0][i-1] != "x":
                    disp += part1[0][i-2: i] 
                    i -= 2
                while len(disp) != 8:
                    disp += "0"
                code_dict["Disp"] = disp
            elif part1[0] in registers:
                code_dict["type"] = "memory1"
                code_dict["D"] = "1"
                if operand == "shl" or operand == "shr":
                    code_dict["D"] = "0"
                code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
                code_dict["mod"] = "00"
                code_dict["R/M"] = part1[0]
                if int(is_new(part1[0])) or code_dict["memory_bytes"] == 64:
                    code_dict["Rex"] = "0100"
                    code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                    code_dict["Rex_R"] = "0"
                    code_dict["Rex_B"] = is_new(part1[0])
                    code_dict["Rex_X"] = "0"
                if part1[0] == "ebp" or part1[0] == "rbp":
                    code_dict["Disp"] = "00"
                    code_dict["mod"] = "01"
            else:
                code_dict["type"] = "memory2"
                code_dict["D"] = "1"
                if operand == "shl" or operand == "shr":
                    code_dict["D"] = "0"
                code_dict["R/M"] = "100"
                code_dict["Bas"] = "ebp"
                code_dict["mod"] = "00"
                code_dict["Disp"] = "00000000"
                a = part1[0].split("*")
                code_dict["Inx"] = a[0]
                code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
                if code_dict.get("Rex") == None:
                    if int(is_new(a[0])) or code_dict["memory_bytes"] == 64:
                        code_dict["Rex"] = "0100"
                        code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                        code_dict["Rex_R"] = "0"
                        code_dict["Rex_X"] = is_new(a[0])
                        code_dict["Rex_B"] = "0"
                        code_dict["Bas"] = "rbp"
                if len(a) == 2:
                    code_dict["SS"] = Scale[a[1]]
                else:
                    code_dict["SS"] = "00"
        elif len(part1) == 2:
            code_dict["type"] = "memory2"
            if part1[0] in registers:
                if part1[1][0:2] == "0x":
                    code_dict["type"] = "memory1"
                    code_dict["D"] = "1"
                    if operand == "shl" or operand == "shr":
                        code_dict["D"] = "0"
                    code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
                    code_dict["R/M"] = part1[0]
                    if code_dict.get("Rex") == None:
                        if int(is_new(part1[0])) or code_dict["memory_bytes"] == 64:
                            code_dict["Rex"] = "0100"
                            code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                            code_dict["Rex_R"] = "0"
                            code_dict["Rex_X"] = "0"
                            code_dict["Rex_B"] = is_new(part1[0])
                    disp = ""
                    if len(part1[1]) % 2 == 1:
                        part1[1] = "0x0" + part1[1][2::]
                    i = len(part1[1])
                    while part1[1][i-1] != "x":
                        disp += part1[1][i-2: i] 
                        i -= 2
                    if len(disp)*4 == 16:
                        disp += "0000"
                    code_dict["Disp"] = disp
                    code_dict["mod"] = mod[len(disp)*4]
                else:
                    code_dict["R/M"] = "100"
                    code_dict["Bas"] = part1[0]
                    code_dict["D"] = "1"
                    if operand == "shl" or operand == "shr":
                        code_dict["D"] = "0"
                    code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
                    a = part1[1].split("*")
                    code_dict["Inx"] = a[0]
                    if int(is_new(a[0])) or int(is_new(part1[0])) or code_dict["memory_bytes"] == 64:
                        code_dict["Rex"] = "0100"
                        code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                        code_dict["Rex_R"] = "0"
                        code_dict["Rex_B"] = is_new(part1[0])
                        code_dict["Rex_X"] = is_new(a[0])
                    code_dict["mod"] = "00"
                    if len(a) == 2:
                        code_dict["SS"] = Scale[a[1]]
                    else:
                        code_dict["SS"] = "00"
                    if part1[0] == "ebp":
                        code_dict["Disp"] = "00"
                        code_dict["mod"] = "01"
            else:
                code_dict["mod"] = "00"
                code_dict["R/M"] = "100"
                code_dict["Bas"] = "ebp"
                code_dict["D"] = "1"
                if operand == "shl" or operand == "shr":
                    code_dict["D"] = "0"
                a = part1[0].split("*")
                code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
                code_dict["Inx"] = a[0]
                if int(is_new(a[0])) or code_dict["memory_bytes"] == 64:
                        code_dict["Rex"] = "0100"
                        code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                        code_dict["Rex_R"] = "0"
                        code_dict["Rex_B"] = "0"
                        code_dict["Rex_X"] = is_new(a[0])
                        code_dict["Bas"] = "rbp"
                if len(a) == 2:
                    code_dict["SS"] = Scale[a[1]]
                else:
                    code_dict["SS"] = "00"
                disp = ""
                if len(part1[1]) % 2 == 1:
                    part1[1] = "0x0" + part1[1][2::]
                i = len(part1[1])
                while part1[1][i-1] != "x":
                    disp += part1[1][i-2: i] 
                    i -= 2
                if len(disp)*4 == 8:
                    disp += "000000"
                elif len(disp)*4 == 16:
                    disp += "0000"
                code_dict["Disp"] = disp
        else:
            code_dict["type"] = "memory2"
            code_dict["W"] = Reg_W[code_dict["memory_bytes"]]
            code_dict["D"] = "1"
            if operand == "shl" or operand == "shr":
                code_dict["D"] = "0"
            code_dict["R/M"] = "100"
            code_dict["Bas"] = part1[0]

            a = part1[1].split("*")
            code_dict["Inx"] = a[0]
            if code_dict.get("Rex") == None:
                if  int(is_new(a[0])) or int(is_new(part1[0])) or code_dict["memory_bytes"] == 64:
                    code_dict["Rex"] = "0100"
                    code_dict["Rex_W"] = Rex_W[code_dict["memory_bytes"]]
                    code_dict["Rex_R"] = "0"
                    code_dict["Rex_B"] = is_new(part1[0])
                    code_dict["Rex_X"] = is_new(a[0])
            if len(a) == 2:
                code_dict["SS"] = Scale[a[1]]
            else:
                code_dict["SS"] = "00"
            disp = ""
            if len(part1[2]) % 2 == 1:
                part1[2] = "0x0" + part1[2][2::]
            i = len(part1[2])
            while part1[2][i-1] != "x":
                disp += part1[2][i-2: i] 
                i -= 2
            if len(disp)*4 == 16:
                disp += "0000"
            code_dict["Disp"] = disp
            code_dict["mod"] = mod[len(disp)*4]

    return code_dict



def find_size(string):
    i = 0
    while string[i] != " ":
        i += 1
    bytes = size[string[0:i]]
    while string[i] != "[":
        i += 1
    
    return bytes, string[i::]


def one_operand(input):
    i = 0
    while(input[i] != " "):
        i += 1

    operand = input[0:i]

    while input[i] == " ":
            i += 1
    part1 = input[i::]
    
    calc_one(operand, part1)


#main 
input = input()
shift_count = None
if input[0:3] == "shl" or input[0:3] == "shr":
    i = 0 
    while i < len(input) and input[i] != ",":
        i += 1
    j = i
    if i < len(input)-1:
        i += 1
    while  i < len(input) and input[i] == " ":
        i += 1

    shift_count = input[i::]
    if shift_count[0:2] == "0x":
        shift_count = shift_count[2::]
    if shift_count == "1":
        shift_count = ""
    if len(shift_count) == 1:
        shift_count = "0" + shift_count
    
    input = input[0:j]

if opCode.get(input) != None:
    print(bin2hex(opCode[input]))
elif input[0:3] == "ret":
    disp = ""
    i = 3
    while input[i] == " ":
        i += 1
    disp = input[i::]
    if disp[0:2] != "0x":
        disp = hex(int(disp)).split('x')[-1]
    disp = disp[2::]
    while len(disp) < 4:
        disp += "0"
    output = "11000010"
    output = bin2hex(output)
    output += disp
    print(output)
else:
    is_one_operand = True
    for i in input:
        if i == ",":
            is_one_operand = False
            break
    if is_one_operand:
        one_operand(input)
    else:
        i = 0
        while(input[i] != " "):
            i += 1

        operand = input[0:i]

        while input[i] == " ":
                i += 1
        j = i
        while input[i] != ",":
            i += 1
        part1 = input[j:i]
        i += 1
        while input[i] == " ":
            i += 1
        part2 = input[i::]

        calc(operand, part1, part2)