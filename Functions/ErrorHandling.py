file = open('Youtube.txt','w')
try:
    file.write('Archit')
finally:
    file.close()

with open('Youtube.txt','w') as file2:
    file2.write('Pathak')