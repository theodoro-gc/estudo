sts = int(input('quantos dias alugados?'))
str = float(input('quantos km andados?'))
stf = sts * 60
stu = str * 0.15
stg = stf + stu
print ('o valor total a paga é {} '.format(stg))