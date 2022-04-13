"""Nikita è un'abile spia che deve trovare e seguire una serie di
indizi (una sequenza di parole) che la porteranno a scoprire una o più
informazioni segrete, sotto forma di sequenze di parole.  Per ottenere
il/i segreto/i Nikita deve visitare diverse città ed in ciascuna città
troverà un indizio che le rivelerà quale sia la prossima città in cui
dovrà spostarsi.  Per ogni città visitata, Nikita otterrà una nuova
parola del segreto.

Come in una caccia al tesoro, Nikita dovrà esplorare una rete di
città, raccogliendo informazioni in ognuna di esse.

NOTA: un indizio di una città può portare in più città alternative.
    Quindi i percorsi da esplorare potrebbero essere multipli ed i
    segreti più di uno.

NOTA: se in una certa città NON C'È l'istruzione corrispondente al
    prossimo indizio vuol dire che la rete di spie nemica ha scoperto
    e distrutto l'informazione, ed il segreto che Nikita stava
    costruendo con quella sequenza non può essere più completato.
    Nikita, quindi, abbandona quella pista e prova a completare gli
    altri segreti che ha già raccolto.

Vogliamo scoprire tutti i segreti che Nikita può ricostruire dati gli
indizi a disposizione e le istruzioni disseminate nelle diverse città.

Le indicazioni su come muoversi tra le città sono contenute nel file
file_istruzioni secondo il seguente formato:
- ogni riga che inizia con il carattere cancelletto '#' va ignorata
- le città sono sempre scritte in MAIUSCOLO
- gli indizi e le parole del/i segreto/i da scoprire sono sempre
  scritte in minuscolo
Il file contiene, separate da almeno uno spazio/tab/accapo, zero o più
istruzioni da seguire.  Ogni istruzione è scritta come la
concatenazione di quattro parole:
    - città         (parola MAIUSCOLA)
    - indizio       (parola minuscola)
    - destinazione  (parola MAIUSCOLA)
    - segreto       (parola minuscola)

Esempio:
    l'istruzione      ROMAcarciofoPARIGIchampagne     indica che
        - quando la spia è a                    'ROMA'
        - se l'indizio seguente è               'carciofo'
        - la spia deve andare a                 'PARIGI'
        - ed aggiungere al segreto la parola    'champagne'

NOTA: potete assumere che il file non contenga mai istruzioni uguali.
NOTA: possono essere presenti istruzioni diverse che, partendo dalla stessa città,
    per lo stesso indizio portano in città diverse e/o producono segreti diversi
    Esempio:
    ROMAcarciofoPARIGIchampagne
    ROMAcarciofoCANCUNchampagne
    ROMAcarciofoPARIGImitraglietta
    ROMAcarciofoCATANZAROcommissario

Progettate ed implementate la funzione ex1(istructions_file, initial_city, clues) 
ricorsiva o che usa funzioni o metodi ricorsivi, che riceve come argomenti:

 - instructions_file: il nome di un file di testo che contiene le
                      istruzioni da seguire in ogni città
 - initial_city:      il nome della città da cui parte Nikita (una parola MAIUSCOLA)
 - clues:             una lista di indizi (stringa formata da parole minuscole separate
                      da spazio)

che ricostruisce tutti i possibili segreti e che torna come risultato
l'insieme di TUTTE le possibili coppie (segreto, CITTÀ), dove:
 - segreto è uno dei possibili segreti scoperti da Nikita, ovvero una
           stringa ottenuta dalla concatenazione delle parole scoperte
           separate da spazio)
 - CITTÀ   è la città in cui la spia è arrivata quando ha completato il segreto

Esempio:
Se il file è 'esempio.txt', la città di partenza è 'ROMA' e gli indizi sono 
"la bocca sollevò dal fiero pasto" 
tutte le possibili coppie segreto/città finale saranno:
     ('vendita diamanti rubati stanotte ad anversa', 'CANCUN')
     ('vendita cannoni mercato nero del cairo',      'CANCUN')
     ('furto di diamanti a buckingham palace',       'MILANO')
     ('mata hari ha sedotto ambasciatore zambia',    'MILANO')

NOTA: è vietato importare/usare altre librerie o aprire file tranne quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se 
    la funzione/metodo ricorsivo è definita a livello esterno. 
    NON definite la funzione ricorsiva all'interno di un'altra funzione/metodo 
    altrimente fallirete tutti i test.

"""




def  ex1(istructions_file, initial_city, clues):
    f = open(istructions_file, encoding='UTF-8')
    f = f.read()
    clues = clues.split()
    
    f = f.replace(' ','\t')
    f = f.splitlines()
    
    city_list= []
    for i in f:
        if not i.startswith('#') and i != '':
            city_list+= i.strip().split('\t')
            
    f.clear()
    diz = {}
    city_list = pulisci(city_list)
    start = initial_city
    indizi= set()
    scoperte = ricorsione(city_list,clues,start,indizi,diz)
    return scoperte

def ricorsione(city_list,clues,start,indizi,diz,last=[],pista=''):
    if clues==[]:
        lista_appoggio = [pista[:-1],start]
        indizi.add(tuple(lista_appoggio))
        
        return indizi
    inizio = start+clues[0]
    for city in city_list:
        if city.startswith(inizio):
            city= city.partition(clues[0])
            ind,diz = dividi(city[2],diz)
            last.append([start,len(city[2][ind:])+1])
            start = city[2][:ind]
            pista += city[2][ind:] + ' '
            
            ricorsione(city_list,clues[1:],start,indizi,diz,last,pista)
            pista = pista[:-(last[-1][1])]
            
            start=last[-1][0]
            last.pop(-1)
    return indizi

def dividi(stringa,diz):
    if stringa in diz:
        a = diz[stringa]
        return a,diz
    for i in stringa:
        if i.islower():
            i = stringa.index(i)
            diz[stringa]=i
            return i,diz

def pulisci(cosa):
    cosa = set(cosa)
    cosa = list(cosa)
    if '' in cosa:
        cosa.remove('')
    return cosa
