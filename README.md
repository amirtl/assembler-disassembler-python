# assembler-disassembler-python
A compiler and reverse compiler for  assembly language
# Explanation
in assembler.py it gets an assembly instruction and outputs the hexadecimal compiled form.
in disassembler.py it gets a hexadecimal code and return itrs assembly instruction.
it only supports this instructions:
![image](https://user-images.githubusercontent.com/47561586/123507421-76a9e080-d67e-11eb-9e30-026c8192063a.png)
# input and output:
- assembly.py :

* input:

- * xor edx,DWORD PTR [ebp+r9d*4+0x55]

* output:

- * 674233548d55

- disassembler.py:
* input:

- * 674233548d55

* output:

- * xor edx,DWORD PTR [ebp+r9d*4+0x55]
