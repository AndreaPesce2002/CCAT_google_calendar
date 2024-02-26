# CCAT_google_calendar
This Cheshire Cat tool allows you to ask the cat for Google Calendar events and create new ones, but for now it is not able to modify or delete them

## tutorial
1) andate nel sito https://console.cloud.google.com/apis/library/calendar-json.googleapis.com?project=hardy-answer-374309&authuser=0
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img1.png)
2) premi il tasto abilita
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img2.png)
3) vai su **scermata consenso OAut**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img3.png)
4) premi crea e riempi i campi
5) ti troverai nella scermata **Ambiti**, aggiungi solo gli agenti mostrati nell'imagine
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img5.png)
6) premi il pulsante **aggiorna** e poi **salva e continua**
7) procedi aggiungendo un user
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img6.png)
8) unsa volta comletato dovresti trovarti in questa situazioe:
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img7.png)
9) ora andimom in **credenzili**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img8.png)
10) creiamo un nuovo **ID client OAuth 2.0**, per farlo dobbimo premere su **crea credenzili** e poi su **ID client OAuth**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img9.png)
11) selezionata applicazione **dekstop** e poi **crea**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img10.png)
12) scaricate il json
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img11.png)
13) aprite un tavolo di lavoro sulla cartella **creaToken**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img12.png)
14) all'interno di **credentials.json** inserite il contenuto del json scaricato ed avviate il file **creaToken.py**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img13.png)
15) premete accedete ad account google
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img13.png)
16) premete su continua
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img14.png)
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img15.png)
17) vi ritroverete con il file **token.json**
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img16.png)
18) ora avviamo il gatto ed una volta avviato andiamo nei plugion e attiviamo il plugion
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img17.png)
19) in fine dobbimo aggiungere negli dobbimo inserire i corrispottivi json nelle corrispettive opzioni (NON il percporso del file ma propio il codice json)
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img18.png)
![alt text](https://github.com/AndreaPesce2002/CCAT_google_calendar/blob/main/img/img19.png)