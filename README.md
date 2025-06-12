
Hvordan hoste nettsiden din på apache2

1.	Det første du  må gjøre er å gå inn i terminalen ved hjelp av Ctrl+alt+T, deretter skriver du «sudo apt update». Dette gjør du for å sjekke om du har din package installer er oppdatert

2.	Neste steg er å installere apache2, dette gjør du ved å skrive: Sudo apt install apache2. Hvis du allerede har det installert så er ikke dette steget nødvendig

3.	Neste steg er å gå inn i /var/www/html, når du er i denne mappen trenger du admin privilegier så du må alltid bruke sudo før kommandoer for å gjør noen endringer.

4.	Neste steg er å starte webserveren, dette gjør du ved å skrive sudo systemctl start apache2. Det skal ikke komme opp noe når du kjører denne kommandoen

5.	Neste steg er å sjekke om serveren er opp å kjører ved å skrive sudo systemctl status apache2 

Tips: 
•	Du kan endre hvilken fil den kjører webserveren fra ved å bruke nano og skrive sudo nano /etc/apache2/apache2.conf
•	Ta utgangspunkt i at den bruker et spesifikt navn for index så vis du har skrevet index med stor I så kan det hende at den ikke finner riktig fil.
•	Lær deg viktige kommandoer som mv, rm, cat, touch for å kunne gjøre endringer og flytte ting i terminalen

