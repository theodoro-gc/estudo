import math

cat  = float(input('comprimento do cateto oposto'))
catadj =  float(input('comprimento do cateto adjecente'))
potencia = math.hypot(cat,catadj)
print ('o cateto da hipotenusa vai medir {:.2f}'.format(potencia))


