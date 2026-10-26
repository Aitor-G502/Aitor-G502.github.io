n = int(input('Introdueix un nombre enter positiu: '))
patron = ''
index = 1
while index < n:
    patron += "* "*index + "\n"
    index += 1

llista_patron = patron.split('\n')
llista_patron.reverse()
print(f'{patron + '* '*n + '\n'.join(llista_patron) }')