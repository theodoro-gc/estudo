seguimentoUm = float(input('primeiro seguimento'))
seguimentoDois = float(input('segundo seguimento'))
seguimentoTres = float(input('segimento tres'))
if seguimentoUm < seguimentoDois + seguimentoTres and seguimentoDois < seguimentoUm + seguimentoTres and seguimentoTres < seguimentoDois + seguimentoUm:
    print('os seguimentos a seguir formão um trangulo')
else:
    print('os seguimentos nao formão um triangulo')