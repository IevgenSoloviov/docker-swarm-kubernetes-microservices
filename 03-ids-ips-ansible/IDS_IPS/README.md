# Sistema IDS amb Suricata

## Instal·lació

```bash
sudo apt update
sudo apt install suricata -y
```

Verificació:

```bash
suricata --version
```

Execució manual:

```bash
sudo suricata -c /etc/suricata/suricata.yaml -i eth1
```
---

## Optimització de Suricata

Per millorar el rendiment del sistema IDS, s’ha optimitzat la configuració de Suricata modificant el fitxer:
```
/etc/suricata/suricata.yaml
```
### Mode d'execució

S’ha configurat el mode:
```
runmode: workers
```
Aquest mode permet processar paquets en paral·lel utilitzant múltiples fils, millorant el rendiment en sistemes multi-core.

### Configuració AF-Packet

S’ha utilitzat el mètode de captura **AF-Packet**, optimitzat amb:

- cluster-type: cluster_flow → distribució del trànsit per fluxos
- defrag: yes → reassemblatge de paquets fragmentats
- use-mmap: yes → millora del rendiment en l'accés a memòria
- mmap-locked: yes → evita swapping i millora estabilitat

### Optimització de rendiment

Paràmetres ajustats:
```
- detect-thread-ratio: 1.5  
- max-pending-packets: 2048  
```
Aquests valors permeten:

- augmentar la capacitat de processament de paquets  
- reduir la latència en la detecció  
- evitar pèrdua de paquets en situacions de càrrega  

### Resultat

Amb aquestes optimitzacions, Suricata és capaç de:

- processar més trànsit en temps real  
- millorar la detecció d’atacs  
- mantenir estabilitat sota càrrega  

Aquest ajust apropa el laboratori a un entorn real de producció.

---
## Configuració de Regles

### Instal·lació regles ET Open
```bash
sudo suricata-update
```
---

## Configuració de Regles IDS

Les regles personalitzades utilitzades en aquest projecte es defineixen al fitxer:
```bash
/var/lib/suricata/rules/local.rules
```
Aquestes regles estan dissenyades específicament per detectar activitats sospitoses contra la infraestructura desplegada amb Ansible.

### Regles d'entrada (EXTERNAL_NET → HOME_NET)
```bash
# Detectar escanejos contra la infraestructura
alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN detectat contra infraestructura"; flow:to_server; flags:S; threshold:type threshold, track by_src, count 10, seconds 5; sid:100001; rev:1;)

# Detectar intents d'acces SSH
alert tcp $EXTERNAL_NET any -> $HOME_NET [2221,2222] (msg:"Intent d'acces SSH detectat"; sid:100002; rev:1;)

# Detectar força bruta SSH
alert tcp $EXTERNAL_NET any -> $HOME_NET [2221,2222] (msg:"Possible brute force SSH"; flow:stateless; flags:S; detection_filter:track by_src, count 5, seconds 60; sid:100003; rev:2;)

# Detectar acces al servidor web desplegat amb Ansible
alert tcp $EXTERNAL_NET any -> $HOME_NET [8081,8082] (msg:"Acces HTTP a servidor web detectat"; sid:100004; rev:1;)

# Detectar escaneig de ports
alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"Possible escaneig de ports"; flow:to_server; flags:S; threshold:type threshold, track by_src, count 20, seconds 10; sid:100005; rev:1;)

# Detectar acces a serveis Docker exposats
alert tcp $EXTERNAL_NET any -> $HOME_NET [2221,2222,8081,8082] (msg:"Acces a serveis Docker Infraestructura Ansible"; sid:100006; rev:1;)
```
Aquestes regles permeten detectar diferents tipus d'activitat maliciosa dins del laboratori:

- escaneigs de ports  
- intents d'accés SSH  
- possibles atacs de força bruta  
- accessos als serveis desplegats amb Ansible  
- activitat de reconeixement contra la infraestructura  
---

## Regles de monitorització interna (LAN → INTERNET_NET)

A més de les regles d’entrada, s’han implementat regles orientades a detectar comportament sospitós originat des de la xarxa interna (LAN), amb l’objectiu d’identificar possibles màquines compromeses o activitat anòmala.
```bash
# Escaneig sortint (SYN)
alert tcp $HOME_NET any -> $INTERNET_NET any (msg:"SCAN sortint des de LAN"; flow:to_server; flags:S; threshold:type threshold, track by_src, count 20, seconds 10; sid:200001; rev:1;)

# Connexions a serveis administratius externs
alert tcp $HOME_NET any -> $INTERNET_NET [22,3389] (msg:"Connexio a serveis administratius externs"; sid:200002; rev:1;)

# Volum alt de connexions HTTP/HTTPS
alert tcp $HOME_NET any -> $INTERNET_NET [80,443] (msg:"Volum alt connexions web sortints"; flow:to_server; threshold:type threshold, track by_src, count 100, seconds 30; sid:200003; rev:1;)

# Connexions repetides sospitoses
alert tcp $HOME_NET any -> $INTERNET_NET any (msg:"Connexions repetides sospitoses des de LAN"; flow:to_server; detection_filter:track by_src, count 50, seconds 20; sid:200004; rev:1;)
```
Aquest conjunt de regles permet detectar:

- escaneigs de ports iniciats des de la xarxa interna  
- connexions a serveis administratius externs (SSH, RDP)  
- comportament anòmal amb alt volum de trànsit web  
- patrons de connexió repetitiva que poden indicar automatització o malware  

Aquest enfocament amplia el sistema IDS, permetent no només detectar atacs externs sinó també possibles compromisos interns dins de la infraestructura.

---

# Sistema d'Alerta Temprana

A més de la detecció amb Suricata i la visualització amb Elastic Stack, s'ha implementat un **sistema d'alerta temprana per correu electrònic**.

Aquest sistema permet avisar immediatament l'administrador quan es detecten determinats tipus d'atacs.

El sistema funciona monitoritzant el fitxer de logs estructurat de Suricata:

```text
/var/log/suricata/eve.json
```

Quan apareix una alerta rellevant, s'envia automàticament un correu electrònic amb la informació de l'atac.

---

## Característiques del Sistema d'Alerta

- monitorització contínua del fitxer `eve.json`
- detecció d'esdeveniments `alert` generats per Suricata
- filtratge de signatures específiques
- extracció automàtica d'informació de l'alerta
- enviament automàtic de correus electrònics
- integració amb servidor SMTP (Postfix + Gmail)
- sistema de deduplicació temporal d'alertes
- limitació d'enviament d'un correu cada 300 segons per signatura
- execució automatitzada com a servei systemd
- funcionament permanent en segon pla

---

## Script d'Alerta

El sistema d'alerta es basa en el següent script (Aquesta és la versió final amb el bloqueig d'IP temporal afegit):

```text
/usr/local/bin/suricata-alert.sh
```

```bash
#!/bin/bash

LOG="/var/log/suricata/eve.json"
EMAIL="admin@example.com"
STATE_DIR="/var/lib/suricata-alert"
COOLDOWN=300
BAN_TIME=600
BLOCK_LOG="/var/log/suricata-active-response.log"
CHAIN="SURICATA_BLOCK"

mkdir -p "$STATE_DIR"
touch "$BLOCK_LOG"

tail -Fn0 "$LOG" | while read -r line; do

    echo "$line" | grep '"event_type":"alert"' >/dev/null || continue

    SIGNATURE=$(echo "$line" | grep -oP '"signature":"\K[^"]+')
    SRC_IP=$(echo "$line" | grep -oP '"src_ip":"\K[^"]+')
    DEST_IP=$(echo "$line" | grep -oP '"dest_ip":"\K[^"]+')
    TIME=$(echo "$line" | grep -oP '"timestamp":"\K[^"]+')

    case "$SIGNATURE" in
        "Possible brute force SSH"|"Possible escaneig de ports"|"Acces a serveis Docker Infraestructura Ansible"|"SCAN detectat contra infraestructura"|"SCAN sortint des de LAN")
            ;;
        *)
            continue
            ;;
    esac

    SAFE_NAME=$(echo "$SIGNATURE" | tr ' /' '__' | tr -cd '[:alnum:]_-')
    STATE_FILE="$STATE_DIR/$SAFE_NAME.last"

    NOW=$(date +%s)

    if [ -f "$STATE_FILE" ]; then
        LAST_SENT=$(cat "$STATE_FILE" 2>/dev/null)
    else
        LAST_SENT=0
    fi

    ELAPSED=$((NOW - LAST_SENT))
    ACTION_MSG="Sense resposta automàtica."

    # Bloqueig immediat independent del cooldown
    if [ "$SIGNATURE" = "Possible brute force SSH" ]; then
        if ! iptables -C "$CHAIN" -s "$SRC_IP" -j DROP 2>/dev/null; then
            iptables -A "$CHAIN" -s "$SRC_IP" -j DROP
            echo "$(date '+%F %T') - IP $SRC_IP bloquejada temporalment durant $BAN_TIME segons" >> "$BLOCK_LOG"
            ACTION_MSG="IP atacant bloquejada temporalment durant $BAN_TIME segons."

            (
                sleep "$BAN_TIME"
                iptables -D "$CHAIN" -s "$SRC_IP" -j DROP 2>/dev/null
                echo "$(date '+%F %T') - IP $SRC_IP desbloquejada automàticament" >> "$BLOCK_LOG"
            ) &
        else
            ACTION_MSG="La IP atacant ja estava bloquejada temporalment."
        fi
    fi

    # Correu subjecte a cooldown
    if [ "$ELAPSED" -ge "$COOLDOWN" ]; then
        {
            echo "Alerta IDS detectada"
            echo
            echo "Hora: $TIME"
            echo "IP origen: $SRC_IP"
            echo "IP destí: $DEST_IP"
            echo "Signatura: $SIGNATURE"
            echo
            echo "Acció: $ACTION_MSG"
            echo
            echo "Revisa el dashboard de Kibana per més informació."
        } | mail -s "ALERTA IDS - $SIGNATURE" "$EMAIL"

        echo "$NOW" > "$STATE_FILE"
    fi

done

```

---

## Servei Systemd

Per garantir que el sistema d'alerta funcioni permanentment, l'script s'executa com a servei de systemd.

Fitxer del servei:

```text
/etc/systemd/system/suricata-alert.service
```

```ini
[Unit]
Description=Alerta per correu de Suricata
After=network.target postfix.service suricata.service

[Service]
Type=simple
ExecStart=/usr/local/bin/suricata-alert.sh
Restart=always
RestartSec=5
User=root

[Install]
WantedBy=multi-user.target
```

Activació del servei:

```bash
sudo systemctl daemon-reload
sudo systemctl enable suricata-alert.service
sudo systemctl start suricata-alert.service
```

Verificació:

```bash
sudo systemctl status suricata-alert.service
```

---

## Funcionament del Sistema d'Alerta

El flux complet del sistema és el següent:

```
Atac des de Kali
      ↓
Suricata detecta l'activitat sospitosa
      ↓
Suricata registra l'alerta a eve.json
      ↓
Script de monitorització detecta l'alerta
      ↓
Filtrat de signatures rellevants
      ↓
Sistema de deduplicació temporal
      ↓
Enviament d'alerta per correu electrònic
      ↓
Administrador rep notificació immediata
```

Aquest mecanisme permet implementar un **sistema d'alerta temprana davant possibles atacs contra la infraestructura**.

---

# Simulació d'Atacs amb Kali Linux

Per validar el funcionament del sistema IDS es van simular diferents atacs des d'una màquina **Kali Linux** situada al segment d'atac de la xarxa.

A més, es van realitzar proves de comportament sospitós des de la xarxa interna cap a l’exterior per simular possibles equips compromesos.

Aquestes proves permeten verificar que:

- Suricata detecta activitat sospitosa
- les regles personalitzades funcionen correctament
- es detecten tant atacs externs com comportament intern anòmal
- les alertes apareixen a Kibana
- el sistema d'alerta temprana envia correus electrònics

---

## Escaneig de Ports (Nmap)

Per simular una fase de reconeixement es va utilitzar **Nmap** per escanejar els ports del servidor.

```bash
nmap -sS -T4 -p- 192.168.200.1
```

Aquest escaneig activa les regles:

- `SCAN detectat contra infraestructura`
- `Possible escaneig de ports`

---

## Atac de Força Bruta SSH

Per provar la detecció d'intents d'accés SSH es va utilitzar **Hydra**.

```bash
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.200.1 -s 2221 -t 4
```

Aquest atac genera múltiples intents d'autenticació i activa les regles:

- `Intent d'acces SSH detectat`
- `Possible brute force SSH`

---

## Accés a Serveis Web

Per simular accessos als serveis web desplegats amb Ansible es va utilitzar **curl**.

```bash
curl http://192.168.200.1:8081
```

Aquest accés activa la regla:

- `Acces HTTP a servidor web detectat`

---

## Simulació d’Activitat Interna Sospitosa (LAN → Internet)

Per validar la detecció de comportament anòmal dins la xarxa, es van realitzar proves des de la LAN cap a serveis externs.

### Escaneig sortint

```bash
nmap -Pn -p 1-1000 8.8.8.8
```

Activa:

- `SCAN sortint des de LAN`

### Connexions a serveis administratius externs

```bash
nc -zv 8.8.8.8 22
nc -zv 8.8.8.8 3389
```

Activa:

- `Connexio a serveis administratius externs`

### Connexions repetides (comportament sospitós)

```bash
for i in {1..300}; do nc -z -w1 1.1.1.1 80 >/dev/null 2>&1; done
```

Activa:

- `Connexions repetides sospitoses des de LAN`

Aquestes proves simulen el comportament d’un equip intern potencialment compromès.

---

## Validació de les Alertes

Quan es detecta un atac:

1. Suricata genera una alerta a `eve.json`
2. Filebeat envia els logs a **Elasticsearch**
3. Les alertes es visualitzen a **Kibana**
4. El sistema d'alerta temprana envia un **correu electrònic automàtic**
5. En casos crítics, s’aplica bloqueig automàtic amb **iptables**

Aquest procés permet verificar el correcte funcionament del sistema IDS i la seva capacitat de resposta davant amenaces externes i internes.

---

# Sistema de Resposta Activa (Active Response)

A més de la detecció d'intrusions amb Suricata i el sistema d'alerta temprana per correu electrònic, el projecte implementa un mecanisme de **resposta activa automàtica** utilitzant **iptables**.

Aquest sistema permet **bloquejar temporalment les IP que generen alertes d’atac** detectades per Suricata.

Aquesta funcionalitat transforma el sistema en un model:

IDS + Active Response

similar al funcionament de moltes plataformes de seguretat modernes.

---

# Arquitectura de Resposta

El procés de resposta funciona de la següent manera:

```
Atac des de Kali
        ↓
Suricata detecta l'atac
        ↓
Alerta registrada a eve.json
        ↓
Script de monitorització detecta l'alerta
        ↓
Enviament d'alerta per correu
        ↓
Bloqueig automàtic de la IP amb iptables
        ↓
IP bloquejada temporalment
        ↓
Desbloqueig automàtic després del temps definit
```

Aquest sistema permet **reaccionar automàticament davant determinats tipus d'atac**.

---

# Bloqueig Automàtic amb iptables

Quan es detecta una alerta crítica (per exemple un atac de força bruta SSH), el sistema afegeix una regla de bloqueig al firewall.

Exemple de regla aplicada:

```bash
iptables -A SURICATA_BLOCK -s IP_ATACANT -j DROP
```

Aquesta regla impedeix que la IP atacant continuï enviant trànsit cap a la infraestructura.

---

# Cadena Personalitzada SURICATA_BLOCK

Per gestionar els bloquejos de manera organitzada es va crear una cadena específica d’iptables anomenada:

```
SURICATA_BLOCK
```

Aquesta cadena s'insereix dins de la cadena **FORWARD** del firewall.

```bash
iptables -I FORWARD 1 -j SURICATA_BLOCK
```

D’aquesta manera tots els paquets que travessen el router IDS són verificats contra les regles de bloqueig.

---

# Ús de la Cadena FORWARD

El bloqueig s’aplica a la cadena **FORWARD** perquè el servidor IDS actua com a **router entre dues xarxes internes**.

Topologia simplificada:

```
Kali (192.168.100.x)
        │
        │
 IDS / Suricata Router
        │
        │
Infraestructura (192.168.200.x)
```

En aquest escenari el servidor IDS **no és el destí del trànsit**, sinó que el reenvia entre xarxes.

Per aquest motiu el filtratge es realitza a la cadena:

```
FORWARD
```

en lloc de la cadena `INPUT`.

Això permet bloquejar el trànsit **abans que arribi als servidors interns**.

---

# Bloqueig Temporal d’IP

El sistema implementa un mecanisme de **bloqueig temporal automàtic**.

Quan es detecta una alerta crítica:

1. es registra l'incident  
2. s'envia un correu d'alerta  
3. s'aplica una regla de bloqueig a iptables  
4. s'espera el temps de bloqueig configurat  
5. la regla es elimina automàticament  

Durant el desenvolupament del laboratori es van utilitzar **60 segons de bloqueig per facilitar les proves**.

En un entorn real aquest valor pot augmentar-se (per exemple 10 o 15 minuts).

---

# Tipus d’Arquitectura Implementada

Encara que Suricata funciona principalment com a **IDS (Intrusion Detection System)**, la integració amb iptables permet implementar un comportament similar a un **IPS (Intrusion Prevention System)**.

Per aquest motiu el sistema es pot descriure com:

```
IDS + Active Response (quasi IPS)
```

Aquest model és similar al funcionament d’eines com:

- Fail2ban  
- CrowdSec  
- sistemes SOC amb resposta automatitzada  

---

# Visualització amb Elastic Stack

Logs enviats amb **Filebeat** cap a **Elasticsearch** i visualitzats a **Kibana**.

Filtre per alertes:

```
event.kind: alert
```

Filtre per regla:

```
rule.id: 1000001
```

---

# Firewall amb iptables

Per complementar el sistema IDS, s’ha implementat un firewall amb **iptables** per controlar el trànsit i aplicar mesures de seguretat a nivell de xarxa.

## Regles implementades

S’han configurat regles per bloquejar connexions sortints des de la LAN cap a ports sensibles:
```bash
sudo iptables -A FORWARD -i enp0s3 -o enp0s9 -p tcp --dport 23 -j DROP  
sudo iptables -A FORWARD -i enp0s3 -o enp0s9 -p tcp --dport 139 -j DROP  
sudo iptables -A FORWARD -i enp0s3 -o enp0s9 -p tcp --dport 445 -j DROP  
sudo iptables -A FORWARD -i enp0s3 -o enp0s9 -p tcp --dport 3389 -j DROP  
```
Aquests ports corresponen a serveis potencialment vulnerables o d’administració:

- Telnet (23)  
- NetBIOS / SMB (139, 445)  
- RDP (3389)  

L’objectiu és evitar que dispositius interns compromesos puguin accedir a aquests serveis.

---

## Validació del funcionament

S’ha validat el funcionament del firewall mitjançant proves de connexió:

- telnet google.com 23  
- nc -zv google.com 139  
- nc -zv google.com 445  
- nc -zv 8.8.8.8 3389  

Aquestes connexions han estat bloquejades correctament.

També s’ha verificat amb:
```
sudo iptables -L FORWARD -n -v  
```
on es pot observar l’increment dels comptadors en les regles DROP.

---

### Integració amb el sistema IDS

El firewall treballa conjuntament amb Suricata, permetent no només detectar activitats sospitoses sinó també limitar el trànsit potencialment perillós.

---
## Protecció d’accés als serveis (iptables)

Per evitar l’exposició del sistema a través de la IP pública, s’han afegit regles a `iptables` per restringir l’accés als serveis crítics.

S’ha limitat l’accés a:

- SSH (port 22)  
- Kibana (port 5601)  

Només es permet connexió des de la xarxa interna (`192.168.200.0/24`), mentre que qualsevol accés extern és bloquejat mitjançant:

-A INPUT -p tcp --dport 22 -j DROP  
-A INPUT -p tcp --dport 5601 -j DROP  

A més, es permet:

- trànsit local (loopback)  
- connexions establertes  

### Objectiu

- evitar accessos des de fora de la xarxa  
- reduir la superfície d’atac  
- protegir serveis d’administració i monitorització  

Aquesta configuració garanteix que els serveis només siguin accessibles des de la LAN i no des d’Internet.

---

# Antivirus amb ClamAV

Per reforçar la seguretat del sistema, s’ha implementat **ClamAV** com a antivirus complementari dins del laboratori.

ClamAV és una solució **lliure, lleugera i fàcil d’integrar** en entorns Linux, adequada per detectar fitxers maliciosos a nivell de sistema.

---

## Instal·lació i configuració

S’ha instal·lat ClamAV i el seu servei de monitorització:
```
sudo apt install clamav clamav-daemon -y  
```
Actualització de la base de dades de signatures:
```
sudo systemctl stop clamav-freshclam  
sudo freshclam  
```
Activació del servei d’actualització automàtica:
```
sudo systemctl start clamav-freshclam  
sudo systemctl enable clamav-freshclam  
```
Activació del servei antivirus:
```
sudo systemctl start clamav-daemon  
sudo systemctl enable clamav-daemon  
```
---

## Anàlisi del sistema

S’ha realitzat un escaneig del sistema per detectar possibles fitxers maliciosos:
```
clamscan -r /home  
```
Resultat:

- fitxers analitzats correctament  
- cap amenaça detectada  

---

## Validació del funcionament

Per validar el funcionament de l’antivirus, s’ha utilitzat el fitxer de prova **EICAR**:
```
echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!H+H*' > eicar.com  
```
Escaneig del fitxer:
```
clamscan eicar.com  
```
Resultat:

- fitxer detectat correctament com a maliciós  
- confirmació del correcte funcionament de ClamAV  

---

## Integració amb el sistema de seguretat

ClamAV complementa el sistema IDS basat en Suricata:

- Suricata → detecció d’amenaces a nivell de xarxa  
- ClamAV → detecció de malware a nivell de sistema  

Aquesta combinació permet implementar una estratègia de seguretat més completa dins del laboratori, combinant **monitorització de xarxa i protecció de fitxers**.

---

# Conclusions

Aquest projecte ha estat una experiència molt útil per introduir-me de manera pràctica en el món de la ciberseguretat. Al llarg del desenvolupament, he pogut entendre com funcionen realment sistemes de detecció d’intrusions com Suricata, així com la importància de la monitorització i l’anàlisi de logs amb eines com Elastic Stack.

Tot i que al principi la configuració de totes les eines i la seva integració ha estat complexa, especialment en aspectes com la xarxa, les regles de detecció o la resposta automàtica, aquestes dificultats m’han ajudat a aprofundir molt més en el funcionament intern dels sistemes. També he pogut veure problemes reals com falsos positius, configuracions insegures o exposició de serveis, i com solucionar-los.

Un dels punts més interessants ha estat implementar un sistema de resposta activa amb iptables, que permet actuar automàticament davant d’un atac, apropant el projecte a un entorn real de seguretat. A més, la detecció de comportament sospitós dins la LAN m’ha ajudat a entendre que les amenaces no només venen de fora, sinó també de dins de la xarxa.

En conclusió, aquest projecte no només m’ha permès assolir els objectius plantejats, sinó que també m’ha servit com una primera aproximació molt completa al món de la ciberseguretat, aportant-me coneixements pràctics que considero molt útils de cara al futur professional.

