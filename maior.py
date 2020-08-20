import time


def maior(arquivo):
    nome = arquivo.split('.')[0]
    arq = open(arquivo,'r')
    conteudo = arq.read().split('\n')
    ma = 0
    ini = time.time()
    for i in conteudo:
        if i != '':
            if int(i) > ma:
                ma = int(i)
    fim = time.time()
    x = str((fim-ini)*1000)
    print(x)
    print(ma)
    arq.close()

    nome = 'resposta-'+nome+'.txt'
    arq = open(nome,'w')
    arq.write(str(ma)+'\n')
    arq.write(x)
    arq.close()


maior('dataset-2-a.csv')
maior('dataset-2-b.csv')
maior('dataset-2-c.csv')
maior('dataset-2-d.csv')
maior('dataset-2-e.csv')

