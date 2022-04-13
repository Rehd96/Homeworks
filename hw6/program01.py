'''
Abbiamo una immagine formata da N rettangoli colorati (vuoti, è disegnato solo il bordo) su sfondo nero che vogliamo comprimere.
Per comprimerla bisogna trovare nell'immagine tutti gli N rettangoli presenti, anche se intersecati.
Dobbiamo ordinare i rettangoli in modo che la sequenza di operazioni di disegno riproduca fedelmente l'immagine originale.
Potete assumere che:
    - tutti i rettangoli hanno colori diversi
    - ciascun rettangolo ne interseca almeno un altro
    - i lati di rettangoli diversi non si sovrappongono per lungo ma si incrociano solamente
    - gli angoli di rettangoli diversi non si sovrappongono
    - la sequenza è unica (esiste una sola sovrapposizione tra rettangoli che li ordina)

Per ciascuno degli N rettangoli individuati abbiamo 5 informazioni da codificare sotto forma di una immagine:
    - x, y: coordinate dell'angolo superiore sinistro (x=colonna, y=riga)
    - w, h: larghezza ed altezza in pixel
    - C:    colore del rettangolo

Lo schema di compressione costruisce una seconda immagine di dimensioni 5xN.
La nuova immagine contiene, nello stesso ordine della sequenza di disegno, 
su righe successive dall'alto in basso i dati di ciascun rettangolo 
codificati come 5 pixel consecutivi in orizzontale come segue:
    x, y, w, h: sono codificati ciascuno con un pixel: i tre canali RGB del pixel rappresentano il valore in base 256.
        Esempio: (1,2,3) = 1*255*(2*255+3)=130815
    C: è il colore del 5° pixel

Infine vogliamo conoscere il bounding-box del gruppo di rettangoli, ovvero il rettangolo minimo,
con angolo superiore sinistro in (xmin, ymin) ed angolo inferiore destro (xmax, ymax)
che racchiude tutti i rettangoli.

Progettate ed implementate la funzione ex1(image_filename, encoded_filename) che:
    - legge il file indicato dal parametro 'image_filename' usando la libreria 'images' allegata
    - individua gli N rettangoli e li ordina
    - costruisce l'immagine 5xN che codifica le informazioni dei rettangoli
    - salva l'immagine codificata nel file indicato dal parametro 'encoded_filename'
    - ritorna la tupla con le 4 coordinate (xmin, ymin, xmax, ymax) del bounding box

ATTENZIONE: non importate altre librerie e non aprite file diversi da quelli passati per argomento.
'''


import images

def ex1(image_filename, encoded_filename):
    img = images.load(image_filename)
    w= width(img)
    h = height(img)
    Seen = first(img,w,h)
    ListaR = []
    
    for mele in Seen.items():
        mele = list(mele)
        w = find_w(img, mele)
        h = find_h(img, mele,w)
        mele.insert(1,(w,h))
        mele[0],mele[2] = mele[2], mele[0]
        ListaR.append(mele)
        
    Ordine = Ordina_Quadrati(img,ListaR)
    
    bound = bounding_box(img, ListaR)
    
    for elemento in range(len(Ordine)) :
        Color = Ordine[elemento][2]
        ListaR[elemento] = Cambio_base([Ordine[elemento][0][0],Ordine[elemento][0][1],Ordine[elemento][1][0],Ordine[elemento][1][1]])
        ListaR[elemento].append(Color)
    
    img = creazione_immagine(ListaR)
    images.save(img,encoded_filename)
    return bound
  
def first(img,w,h):
    #per prima cosa mi assicuro di ignorare tutti le righe vuote, sia quelle di sopra
    for y in range(h):
        if max(img[y]) != (0,0,0):
            ymin = y
            break
    reverse = range(h-1,0,-1)
    #che quelle di sotto
    for a in reverse:
        if max(img[a]) != (0,0,0):
            ymax= a+1
            break
    return Seen(img,ymin,ymax,w)    

def Seen(img,ymin,ymax,w):
    #Vado a lavorare solo sulle righe dove so che ci sono elementi
    Seen ={}
    for y in range(ymin,ymax):
        for x in range(w):
            if img[y][x] != (0,0,0) and img[y][x] not in Seen:
                Seen[img[y][x]] = (x,y)
    return Seen

def find_w(img,mela):
    for ind in range(mela[1][0],width(img)):
        #controllo se: il colore è lo stesso, se non lo è
        #vedo se il pixel precedente è l'angolo destro del rettangolo
        if img[mela[1][1]][ind] != mela[0] and img[mela[1][1]+1][ind-1] == mela[0] and ind-1 != mela[1][0] :
            w= ind-mela[1][0]
        
            return w
    #arrivo qui se i precedenti controlli falliscono.
    #potrebbero essersi sovrapposti dei colori di seguito e l'angolo destro è di un altro rettangolo
    return find_w2(img,mela)
    
def find_w2(img,mela):
    """" in questa funzione mi fermo non appena trovo un pixel nero """
    for ind in range(mela[1][0],width(img)):
        if img[mela[1][1]][ind] != mela[0] and  img[mela[1][1]][ind] == (0,0,0):
            w = ind-mela[1][0]
            return  w
   
def find_h(img,mela,w):
    #stesso ragionameno di find_w, applicato all'angolo destro/basso
    for ind in range(mela[1][1],height(img)):
        if img[ind][mela[1][0]] != mela[0] and img[ind-1][mela[1][0]+1] == mela[0] and ind-1 != mela[1][1]:
            h = ind-mela[1][1]
            return h
    #anche qui in casi di sovrapposizione faccio un altro test, più basilare
    return find_h2(img,mela,w)
    
def find_h2(img,mela,w):
    x2 = mela[1][0]+w-1
    for ind in range(mela[1][1],height(img)):
        if img[ind][x2] != mela[0] and img[ind-1][x2-1] == mela[0]:
            h = ind-mela[1][1]
            return h

def width(img):
    #larghezza
    return len(img[0])


def height(img):
    #altezza
    return len(img)

def Ordina_Quadrati(img,Q):
    
    Colori_ordinati = []
    indice= 0
    Quadrati_ordinati= []
    copia_Q = Q.copy()
    do = True
    while do == True:
        Diz={}
        #mi creo un dizionario che in pratica va ad auto-crearsi ad ogni chiamata
        #in modo da essere sempre uguale a copia_q, altrimenti rischio di sfallare gli indici
        for a in range(len(copia_Q)):
            Diz[a] = copia_Q[a][2]
        if len(copia_Q) == 0:
            do= False
            break
        #x = copia_Q[indice][0][0]
        #y = copia_Q[indice][0][1]
        #Colore = copia_Q[indice][2]
        cond = True
        
        #controllo pixel per pixel lungo i lati del rettangolo
        #se trovo che interseca un colore che non è nella lista, non è lui il prossimo
        
        cond = larghezza_su(img,copia_Q,indice,Colori_ordinati,cond)
        cond = altezza_sinistra(img, copia_Q, indice, Colori_ordinati, cond)
        
        x2 = copia_Q[indice][0][0] + copia_Q[indice][1][0]-1
        y2=  copia_Q[indice][0][1] + copia_Q[indice][1][1]-1
       
        
        cond = larghezza_giu(img, copia_Q, indice, y2, x2, Colori_ordinati,cond)
        cond = altezza_destra(img, copia_Q, indice, y2, x2, Colori_ordinati,cond)
        
        #se il rettangolo incrocia solo pixel che sono nella lista dei colori, aggiorno la lista
        if cond == True:
            Colori_ordinati.append(copia_Q[indice][2])
            Quadrati_ordinati.append(copia_Q[indice])
            Diz.pop(indice)
            copia_Q.pop(indice)
            indice =-1
                    
        indice +=1
        
    return Quadrati_ordinati

def larghezza_su(img,copia_Q,indice,Colori_ordinati,cond):
    for i in range(copia_Q[indice][0][0],copia_Q[indice][1][0]+copia_Q[indice][0][0]):
            if img[copia_Q[indice][0][1]][i] != copia_Q[indice][2]:
                if img[copia_Q[indice][0][1]][i] not in Colori_ordinati:
                    cond = False
                    break
    return cond
    
def altezza_sinistra(img,copia_Q,indice,Colori_ordinati,cond):
    for i in range(copia_Q[indice][0][1],copia_Q[indice][1][1]+copia_Q[indice][0][1]):
            if cond== False:
                break
            if img[i][copia_Q[indice][0][0]] != copia_Q[indice][2]:
                if img[i][copia_Q[indice][0][0]] not in Colori_ordinati:
                    cond = False
                    break
    return cond

def larghezza_giu(img,copia_Q,indice,y2,x2,Colori_ordinati,cond):
    for i in range(copia_Q[indice][0][0],x2+1):
            if cond== False:
                break
            if img[y2][i] != copia_Q[indice][2]:
                if img[y2][i] not in Colori_ordinati:
                    cond = False
                    break
    
    return cond

def altezza_destra(img,copia_Q,indice,y2,x2,Colori_ordinati,cond):
    for i in range(copia_Q[indice][0][1],y2+1):
            if cond== False:
                break
            #print(i,x2,img[i][x2])
            if img[i][x2] != copia_Q[indice][2]:
                if img[i][x2] not in Colori_ordinati:
                    
                    cond = False
                    break
    return cond

def Cambio_base(intro):
    cambiato = []
    for i in intro:
        primo = int(i/65536)
        secondo= i%65536
        secondo= int(secondo/256)
        terzo = i%256
        cambiato.append((primo,secondo,terzo))
    return cambiato

def bounding_box(img,Ordine):
    x_max = 0
    y_max = 0
    x_min = len(img[0])
    y_min = len(img)
    for ele in range(len(Ordine)):
        x = Ordine[ele][0][0]
        y = Ordine[ele][0][1]
        x2 = x + Ordine[ele][1][0] -1
        y2 = y + Ordine[ele][1][1] -1
        if x < x_min:
            x_min=x
        if y < y_min:
            y_min = y
        if x2 > x_max:
            x_max = x2
        if y2 > y_max:
            y_max = y2
    return (x_min,y_min,x_max,y_max)
        
def creazione_immagine(Ins):
    immagin = []
    for c in range(len(Ins)):
        riga = []
        riga = Ins[c]
        immagin.insert(0,riga)
    return immagin