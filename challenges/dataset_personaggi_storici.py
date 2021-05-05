# Challenge DATASET  -  PERSONAGGI STORICI 
import os
import csv

from typing import List # to enlist content directory


path_dir: str = r"C:\Users\chiar\Google Drive\GIT\PRV\Python\Jupyter\formats"
content_dir: List[str] = os.listdir(path_dir)

filename = 'personaggi-storici-trentino.csv'

path_file = os.sep.join([path_dir, filename])
print(path_file)

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
      isecolo = ""

      if 'secolo' in idata:
        temp = ""
        for el in idata:
          if el in ['X','I','V',' ']:
            temp += el

        temp2 = temp.split()
        temp = temp2[-1]

        if temp in secoli:
          isecolo = secoli[temp]
      
      elif idata != '':
        print((idata))
        data_split = idata.split()    #temp = idata.translate(None,not "123456789 ")
        # data_split = ['s1','s2','s3','s4']
        print(data_split)
        for iword in reversed(data_split):
          # iword = s1 --> s2 --> ...
          iword2check = ""
          for ichar in iword:
            # ichar = i-character di iword
            if ichar in "0123456789 ":
            # costruisci variabile numerica secolo
              iword2check += ichar
          print(iword2check)
          try:  
            temp = int(iword2check)
            if (isinstance(temp, int)):
              isecolo = temp
              print("Stampa ultimo intero: ", isecolo)
            break
          except ValueError:
            print("Riprova: ", iword)


#        for iel in range(len(temp),0):
#          int(temp)
#        isecolo = temp[-1]
#      print(isecolo)
      

      i_stampa = [inome,iluogo,idata,isecolo]

      scrittore.writerow(i_stampa)     
     # print(i_stampa)






#  print(next(lettore))
#  print(type(lettore))


#  print(nome)
#  with open()
#  print()
