"""
Sia dato un testo che contiene un poema, ovvero una successione di versi in rima.
Il poema è contenuto in un file, un verso per riga.

Vogliamo analizzarlo per estrarne la struttura prosodica, ovvero lo schema poetico in esso usato.
Per far questo sono utili le seguenti definizioni:
    - un 'elemento sonoro' (ES) è una successione massimale di 1 o più consonanti seguite da 1 o più vocali
        - prima tutte le consonanti
        - poi tutte le vocali (aeiouyj)
        - ignorando eventuali caratteri non alfabetici come spazi, numeri e segni di interpunzione 
        - togliendo gli accenti dalle lettere accentate
        - e ignorando la differenza tra maiuscole e minuscole
        NOTA:   fanno eccezione il primo ES di un verso, che può essere composto da sole vocali
                e l'ultimo ES, che può essere composto di sole consonanti
    - un verso è composto da una successione di elementi sonori, l'ultimo dei quali è chiamato 'finale'
        Esempio:      
        Se il verso è "Paperino andò al mare a pescare" 
            - gli elementi sonori sono     ["pa", "pe", "ri", "noa", "ndoa", "lma", "rea", "pe", "sca", "re"]
            - la finale è                   "re"
            - il verso è lungo              10 ES
        notate che le lettere accentate hanno perso l'accento e non ci interessa la distinzione tra maiuscole e minuscole
    - la struttura prosodica di una poesia è una lista di interi, uno per ciascun verso
    - per ciascun verso si considerano sia il numero di ES (#ES) che la sua finale
    - al primo verso va associato il numero 0
    - a ciascuno dei versi successivi va associato:
        - l'intero che è stato già associato ad un verso precedente che ha stesso #ES e finale
        - altrimenti un nuovo intero (che segue l'ultimo già usato)
    Esempio:
        se la poesia è quella qui sotto                     gli elementi sonori sono                                    #ES finale   prosodia
        '''
        Dì pestaggio tessessi allarmai, Partenopea!         di pe sta ggio te sse ssia lla rmai pa rte no pea           13  pea         0
        Sembrò svieremo imbarcate, aumentarono usurpai?     se mbro svie re moi mba rca teau me nta ro nou su rpai      14  rpai        1
        Flash privé spirereste? Pentecoste deturpai         fla shpri ve spi re re ste pe nte co ste de tu rpai         14  rpai        1
        scrost, direttamante arrischiai,                    scro stdi re tta ma ntea rri schiai                          8  schiai      2
        odi attuazione vernicera Partenopea.                o dia ttua zio ne ve rni ce ra pa rte no pea                13  pea         0
        Psion trentacinque preesistiti calzascarpe          psio ntre nta ci nque pree si sti ti ca lza sca rpe         13  rpe         3
        nobilt fiacchi vedesti avvertirsi spermatozoi?      no bi ltfia cchi ve de stia vve rti rsi spe rma to zoi      14  zoi         4
        Igloo rubi incassando giurati spermatozoi!          i gloo ru bii nca ssa ndo giu ra ti spe rma to zoi          14  zoi         4
        Saprai reputasse inebriai                           sa prai re pu ta ssei ne briai                               8  briai       5
        man l'ballaste segnaleremo soprascarpe.             ma nlba lla ste se gna le re mo so pra sca rpe              13  rpe         3
        '''
        l'elenco dei numeri di ES è     [13,    14,     14,     8,        13,    13,    14,    14,    8,       13   ]
        l'elenco delle finali è         ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
        quindi la struttura prosodica è [0,     1,      1,      2,        0,     3,     4,     4,     5,       3    ]

        Dalla struttura prosodica dovete determinare il periodo, ovvero la lunghezza minima di un gruppo di versi che si ripete
        con lo stesso schema. 
        In questo esempio il modulo = 5, infatti la prosodia è formata da due sequenze uguali di 5 elementi 
        che seguono lo schema [0, 1, 1, 2, 0], infatti [0, 1, 1, 2, 0] è equivalente a [3, 4, 4, 5, 3]

        La funzione deve tornare la tupla che contiene nell'ordine i 4 valori: 
            - prosodia: ovvero la lista di interi che avete calcolato da #ES e lunghezza dei versi
            - periodo:  ovvero la lunghezza minima dello schema prosodico che si ripete
            - lunghezze: ovvero la lista delle lunghezze (#ES) dei versi
            - finali:   ovvero la lista degli ES finali di ciascun verso

        Quindi per questo esempio la funzione deve tornare la tupla:
          ( [0, 1, 1, 2, 0, 3, 4, 4, 5, 3], 5, [13, 14, 14, 8, 13, 13, 14, 14, 8, 13 ], 
            ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])

    ATTENZIONE: non potete usare altre librerie o aprire altri file.
    TIMEOUT: Il timeout per questo esercizio è di 100ms (0.1 secondi)
"""

def ex1(poem_filename):
    
        testo= inizio(poem_filename)
        vocali='aeiouyj'
        
    
        es = [calcoloes(rigo,vocali) for rigo in testo if rigo!= ''  ]
        listafinali = [calcola_lista_finali(rigo,vocali) for rigo in testo if rigo!= ''  ]
            

        prosodia = trovaprosodia(es,listafinali)    
        
        
        periodo = funzione_vera(prosodia)
        
    
    
        listafinale= []
        tuplafinale=()
        listafinale.append(prosodia)
        listafinale.append(periodo)
        listafinale.append(es)
        listafinale.append(listafinali)
        tuplafinale= tuple(listafinale)
        
        return tuplafinale
    


def calcoloes(riga,vocali):
    es1=0
    isvocale= True
    if riga[0] in vocali :
        es1+=1
        #pe ogni lettera
    for a in riga:
        #se è una consonante
        if a not in vocali:
            if isvocale==True:
                es1+=1
                isvocale= False
        else:
            isvocale=True
        
    return es1



def calcola_lista_finali(riga,vocali):
    isvocale=True
    z=len(riga)-1
    parola=''
    for ind in range(len(riga)):
        if isvocale==False and riga[z] in vocali:
            break
        if riga[z] not in vocali:
            parola = riga[z] + parola 
            if isvocale==True:
                isvocale= False
        else:
            parola = riga[z] + parola
            isvocale=True
        z-=1
    return parola



def trovaprosodia(es,listafinali):
    diz={}
    indice=0
    prosodia=[]
    for i in range(len(es)):
        coppiavalori = (listafinali[i],es[i])
        
        if coppiavalori not in diz:
            
            diz[coppiavalori] = indice
            prosodia.append(indice)
            indice+=1
        else:
            x = diz.setdefault(coppiavalori)
            prosodia.append(x)
    return prosodia



def tutti_diversi(y):
    seen = list()
    return not any(i in seen or seen.append(i) for i in y)




def prod_controllo(ingresso):
    lista_valori_incontrati = []
    lista_prosodica = ingresso.copy()
    numero_massimo_prosodia=0
    
    for i in range(len(ingresso)):
        
        if ingresso[i] not in lista_valori_incontrati:
            lista_valori_incontrati.append(ingresso[i])
            lista_prosodica[i] = numero_massimo_prosodia
            numero_massimo_prosodia+=1
            
        else:
            lista_prosodica[i] = -1
            
    return lista_prosodica,lista_valori_incontrati



def controllo_corrente(controllo_di_adesso,nuovo):
    lista_valori_incontrati = controllo_di_adesso[1]
    lista_prosodica = controllo_di_adesso[0]
    numero_massimo_prosodia=max(lista_prosodica) +1
    
    if nuovo not in lista_valori_incontrati:
        
        lista_valori_incontrati.append(nuovo)
        lista_prosodica.append(numero_massimo_prosodia)
        numero_massimo_prosodia+=1
        
    else:
        lista_prosodica.append(-1)
        
    return lista_prosodica,lista_valori_incontrati
    



def prod_verifica(ingresso,lista_controllo):
    lista= lista_controllo
    lista_valori_incontrati = []
    lista_prosodica = ingresso.copy()
    numero_massimo_prosodia=0
    
    for i in range(len(ingresso)):
        
        if ingresso[i] not in lista_valori_incontrati:
            
            lista_valori_incontrati.append(ingresso[i])
            lista_prosodica[i] = numero_massimo_prosodia
            numero_massimo_prosodia+=1
            
            if lista_prosodica[i] != lista[i]:
                return 0
                break
                
        else:
            
            lista_prosodica[i] = -1
            
    return lista_prosodica


def funzione_vera(prosodia):
    listacontrollobase= prod_controllo(prosodia[0:2])
    for n in range(3,len(prosodia)//2+1):
        prod= [prosodia[i:i + n] for i in range(0, len(prosodia), n)]
        
        controau = tutti_diversi(prod[0])
        eccolo = False
        controllo_di_adesso = controllo_corrente(listacontrollobase,prod[0][-1])
        
        for i in range(1,len(prod)):
            
            if controau == True:
                
                risultati_tutti_diversi = [tutti_diversi(prod[valore]) for valore in range(1,len(prod)) if tutti_diversi(prod[valore]) == False]
                
                if risultati_tutti_diversi[0] == False:
                    break
            
            isvocale= prod_verifica(prod[i],controllo_di_adesso[0])
            
            if isvocale== 0: 
                eccolo = False
                break
            
            else:
                eccolo= True
                
        if eccolo == True:
            periodo= len(prod[0])
            return periodo


def fwords(fname):
    with open(fname, encoding='UTF-8') as f:
        testo = f.read()
    return testo

def inizio(poem_filename):
    with open(poem_filename, encoding='UTF-8') as file:
        
        testo = file.read()
        testo = testo.lower()
        
        punc = '''!()-[]{};:'", <>./?@#$%^&*_~'''
        
        testo = testo.translate(testo.maketrans('àáâãäåèéêëìíîïýÿòóôõöøöùúûü','aaaaaaeeeeiiiiyyooooooouuuu',punc))
        testo.splitlines()
        testo= testo.split('\n')
        return testo

