'''
_______________________________
|# Lista de exercícios 1       |
|# Aluna: Débora P. Campos     |
|# Data: 29/01/2021            |
|______________________________|
'''

# exercise 1
TNF = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
print(TNF)

print(len(TNF)) #A

print(TNF.count('LL')) #B

#C
print(TNF.find('GG'))
print(TNF.find('RR'))

#D
print(TNF[:101])

#E
TNF=TNF.replace('SSSR', 'AAAA')
print(TNF)

