# Challenge DATASET  -  PERSONAGGI STORICI 
import os
import csv
import pdb

from typing import List # to enlist content directory


path_dir: str = r"C:\Users\chiar\Google Drive\GIT\PRV\Python\Jupyter\formats"
content_dir: List[str] = os.listdir(path_dir)

filename = 'personaggi-storici-trentino.csv'

path_file = os.sep.join([path_dir, filename])
print(path_file)
print("-" * 45)


# Dictionaries
map_unknown = {
  'sconosciuto': '',
  'sconosciuto ': '',
  'sconosciuto (forse Pavia)': '',
  'sconosciuto (in Slesia)': '',
  'probabilmente Termeno': ''
}
province = {
    'TN': 'Trento',
    'PI': 'Pisa',
    'MC': 'Macerata',
    'CO': 'Como',
    'ME': 'Messina',
    'MI': 'Milano'
}
secoli = {
     'I': 0,
     'II':100,
     'III':200,
     'IV':300,
     'V':400,
     'VI':500,
     'VII':600,
     'VIII':700,
     'IX':800,
     'X':900,
     'XI':1000,
     'XII':1100,
     'XIII':1200,
     'XIV': 1300,
     'XV':1400,
     'XVI':1500,
     'XVII':1600,
     'XVIII':1700,
     'XIX':1800,
     'XX':1900,
     'XXI':2000,
}


with open(path_file,encoding='latin-1') as f_lettura:

  lettore = csv.reader(f_lettura)
  header = next(lettore)
  nome = header[3]
  data_nascita = header[4]
  luogo_nascita = header[6]

  print(nome,data_nascita,luogo_nascita)
  next(lettore)

  with open('dascrivere.csv', 'w', encoding='utf-8') as f_scrittura:
    # header del csv da scrivere
    intestazione = [nome.lower(),  luogo_nascita.lower(),data_nascita.lower(), 'secolo']
    scrittore = csv.writer(f_scrittura, delimiter=',')    
    scrittore.writerow(intestazione)
    print("-" * 45)

    for riga in f_lettura:     
      
      iriga = next(lettore)        
      inome = iriga[3]
      idata = iriga[4]
      iluogo = iriga[6]
      # Fixed 'sconosciuto'
      if iluogo in map_unknown:
         iluogo = ''
      # Fixed 'Sigle province'
      for ikey in province: 
        iluogo = iluogo.replace(ikey,province[ikey])
        iluogo = iluogo.replace(',','')
        if not '(' in iluogo:
          iluogo = iluogo.replace(province[ikey],'('+province[ikey]+')')
        if not ' (' in iluogo:
          iluogo = iluogo.replace('(',' (')
          
      # Fixed 'Secolo'
      print("Conversione:")  
      isecolo = idata.replace('/',' ')

      data_split = isecolo.split()    #temp = idata.translate(None,not "123456789 ")
      # data_split = ['s1','s2','s3','s4']
      print(data_split)
      for iword in reversed(data_split):
        # iword = s1 --> s2 --> ...
        iword2check = ""
        for ichar in iword:
        # ichar = i-character di iword
          if ichar in "0123456789XIV ":
          # costruisci variabile numerica secolo
            iword2check += ichar
        if iword2check != '':                            
          print("Anno/Secolo da gestire:",iword2check)   # L'indentaone da qui in già è giusta?

        try:                                             # questo try chiude l'IF di prima... rendendolo banale (ha solo una print dentro)
          if iword2check in secoli:
            #print("dentro dizionario",iword2check)
            #print("convertito",isecolo)
            if secoli.get(iword2check) != '':            # Tendenzialmente assegnare e utilizzare subito quello che tiri fuori da un dizionario può portare a problematiche a valle
              isecolo = secoli.get(iword2check)          # quindi prima fai il check poi assegni di solito
              print("Secolo identificato: ", isecolo)
            break
        except Exception:
          print("KKK: non ho trovato il secolo da convertire!")     

        try:  
          temp = int(iword2check) 
          if (isinstance(temp, int)):    #Questo If non serve, perchè se temp non è un intero la 126 tira eccezzione e si salta alla 133
            temp -= temp % +100
            isecolo = temp
          if isecolo != '':
            print("Secolo identificato: ", isecolo)
          break
        except ValueError:
          print(isecolo)
          pass #print("Riprova: ", iword)      

      print("-" * 55)
  
      i_stampa = [inome,iluogo,idata,isecolo]

      scrittore.writerow(i_stampa)     
     # print(i_stampa)
