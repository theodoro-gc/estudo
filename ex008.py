sts = float (input('Qual salario do funcionario?:'))
stu = float (input('quanto porcento você quer de aumento'))
str = sts + (sts * stu / 100)
print ('o funcionari que ganhava {}reais agora com {} de aumento vai passar a ganhar {:.2f}'.format(sts,stu,str))
