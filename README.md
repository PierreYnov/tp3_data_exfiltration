# Post Exploitation & Data Exfiltration

### Élèves : Emma Durand **[@emmadrd912](https://github.com/emmadrd912)** et Pierre Ceberio **[@PierreYnov](https://github.com/PierreYnov)** 

### Classe : B3 B

## Scénario

Nous sommes dans un cadre post-exploitation, nous devons exfiltrer le fichier `save_shaddow` de la machine victime et l'envoyer sur notre machine distante (afin de les casser).

Pour ne pas se faire détecter du Firewall, nous devons détourner le protocole ``ICMP`` grâce à la librairie ``scapy``, pour pouvoir forger nos propres paquets avec des bouts du fichier `save_shaddow` à l'intérieur de chaque.

## Le projet

- Le programme ``exfiltrator.py`` :
    - envoie la trame de début à l'IP de la machine distante(``header``).
    - découpe chaque ligne du fichier `save_shaddow`, et les envoie une par une, encodé en ``Base64``, avec un pattern pour qu'on soit sûr de leur intégrité.
    - envoie la trame de fin (``end``).

- Le programme ``server.py`` :
    - capture uniquement les trames ICMP venant de l'IP du client (la machine victime).
    - commence à reconstruire le fichier, uniquement à partir du moment où il recoit la trame de début.
    - supprime le pattern d'intégrité, et décode la ``Base64`` afin de retrouver le texte original puis met le tout dans un fichier nommé `save_shaddow`

## Comment lancer ?

- Sur les 2 machines : 

    ``pip install -r requirements.txt``

- Sur la machine victime : 

    Soyer sûr d'avoir défini la bonne IP vers où vous souhaitez envoyer les trames ICMP et le nom du fichier, puis :

    ``python exfiltrator.py``

- Sur la machine distante :

    Soyer sûr d'avoir défini la bonne IP dont vous souhaitez écouter les pings, puis :

    ``python server.py``

## Autres

Pour vérifier l'intégrité du fichier, on regarde si il y a une différence de hash MD5 (à faire sur les 2 machines), avec cette commande :

``md5sum save_shaddow``

Il se peut que les hashs soient différents à cause de la présence de CRLF, pour les enlever, tapez :

``cat save_shaddow | tr -d '\r' > save_shaddow3``

puis

``mv save_shaddow3 save_shaddow``
