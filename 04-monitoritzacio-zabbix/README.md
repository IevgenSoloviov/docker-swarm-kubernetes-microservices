<div align="center">

<br/>

```
███████╗ █████╗ ██████╗ ██████╗ ██╗██╗  ██╗
╚══███╔╝██╔══██╗██╔══██╗██╔══██╗██║╚██╗██╔╝
  ███╔╝ ███████║██████╔╝██████╔╝██║ ╚███╔╝ 
 ███╔╝  ██╔══██║██╔══██╗██╔══██╗██║ ██╔██╗ 
███████╗██║  ██║██████╔╝██████╔╝██║██╔╝ ██╗
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

     M o n i t o r i t z a c i ó   d e   X a r x e s
```

### Supervisió · Alertes · Autorecuperació · SNMP

*Linux · Windows · SNMP · Email · Telegram · Bash · PowerShell*

<br/>

![Zabbix](https://img.shields.io/badge/Zabbix-CC2936?style=for-the-badge&logo=zabbix&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![SNMP](https://img.shields.io/badge/SNMP-FF6600?style=for-the-badge&logoColor=white)

<br/>

</div>

---

##  Descripció del projecte

Implementació d'un sistema de **monitorització professional** en entorn de laboratori virtualitzat, amb supervisió de dispositius **Linux**, **Windows** i **SNMP**, detecció d'incidències, notificacions automàtiques i mecanismes d'**autorecuperació**.

El projecte simula un entorn real on un administrador de sistemes supervisa múltiples dispositius, rep alertes crítiques i el sistema és capaç de recuperar-se automàticament davant falles de serveis.

---

##  Objectiu

Desplegar un sistema de monitorització amb **Zabbix** capaç de:

- 👁️ Supervisar múltiples dispositius i serveis simultàniament
- ⚡ Configurar alertes i triggers per llindars crítics
- 📬 Enviar notificacions automàtiques per **Email** i **Telegram**
- 🔄 Aplicar scripts d'**autorecuperació** davant incidències crítiques
- 📊 Generar dashboards i informes periòdics en PDF

---

##  Entorn del laboratori

```
┌─────────────────────────────────────────────────────────┐
│                   LABORATORI ZABBIX                     │
│                                                         │
│  ┌─────────────────┐        ┌──────────────────────┐   │
│  │  Servidor Zabbix │◄──────►│    Client Linux      │   │
│  │     Linux        │        │  (Zabbix Agent)      │   │
│  └────────┬────────┘        └──────────────────────┘   │
│           │                                             │
│           │◄──────────────► ┌──────────────────────┐   │
│           │                 │    Client Windows     │   │
│           │                 │  (Zabbix Agent)       │   │
│           │                 └──────────────────────┘   │
│           │                                             │
│           │◄──────────────► ┌──────────────────────┐   │
│                             │  Dispositiu SNMP      │   │
│                             │  Linux (snmpd)        │   │
│                             └──────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

| Rol | Sistema operatiu |
|---|---|
| 🖥️ **Servidor Zabbix** | Linux |
| 🐧 **Client Linux** | Linux |
| 🪟 **Client Windows** | Windows |
| 📡 **Dispositiu SNMP** | Linux (snmpd) |

---

##  Funcionalitats implementades

| Funcionalitat | Descripció |
|---|---|
| 📊 **Monitorització de recursos** | CPU, memòria i espai en disc en temps real |
| ⚙️ **Monitorització de serveis** | Apache (Linux) i Print Spooler (Windows) |
| ⚡ **Triggers i alertes** | Configuració per llindar crític personalitzat |
| 📧 **Notificacions Email** | Alertes automàtiques per correu electrònic |
| 📲 **Notificacions Telegram** | Alertes instantànies via bot de Telegram |
| 🔄 **Autorecuperació** | Scripts automàtics per a serveis caiguts |
| 📡 **Integració SNMP** | Supervisió de dispositius de xarxa |
| 🎛️ **Dashboards personalitzats** | Visualització en temps real |
| 📄 **Informes PDF** | Generació periòdica automatitzada |
| ✅ **Proves i validació** | Test complet del sistema |

---

##  Tecnologies utilitzades

| Tecnologia | Ús |
|---|---|
| 🔵 **Zabbix** | Plataforma de monitorització central |
| 🐧 **Linux** | Servidor Zabbix i agent Linux |
| 🪟 **Windows** | Agent Windows i servei Print Spooler |
| 📡 **SNMP** | Monitorització de dispositiu de xarxa |
| 💻 **Bash** | Script d'autorecuperació Apache |
| 🔷 **PowerShell** | Script d'autorecuperació Print Spooler |

---

##  Estructura del repositori

```
04-monitoritzacio-zabbix/
│
├── 📄 README.md
│
├── 📁 agents/
│   ├── agent-linux.md
│   └── agent-windows.md
│
├── 📁 configuracions/
│   └── zabbix/
│       ├── triggers.md
│       ├── accions-zabbix.md
│       ├── notificacions.md
│       ├── dashboard.md
│       └── informes.md
│
├── 📁 scripts/
│   ├── recuperacio_apache.sh
│   └── recuperacio_spooler.ps1
│
├── 📁 snmp/
│   └── snmpd.md
│
└── 📁 captures/
    ├── installacio-configuracio/
    ├── snmp/
    ├── triggers-alertes/
    ├── scripts-plugins/
    └── dashboard-informes/
```

---

##  Contingut del repositori

### ⚙️ Configuracions Zabbix

Documentació de totes les configuracions aplicades al servidor Zabbix:

| Fitxer | Contingut |
|---|---|
| [`triggers.md`](configuracions/zabbix/triggers.md) | Triggers configurats per CPU, memòria, disc i serveis |
| [`accions-zabbix.md`](configuracions/zabbix/accions-zabbix.md) | Accions automàtiques i execució de scripts remots |
| [`notificacions.md`](configuracions/zabbix/notificacions.md) | Canals de notificació: Email i Telegram |
| [`dashboard.md`](configuracions/zabbix/dashboard.md) | Configuració del dashboard personalitzat |
| [`informes.md`](configuracions/zabbix/informes.md) | Generació d'informes periòdics en PDF |

---

### 🤖 Agents

| Fitxer | Contingut |
|---|---|
| [`agent-linux.md`](agents/agent-linux.md) | Instal·lació i configuració de l'agent en Linux |
| [`agent-windows.md`](agents/agent-windows.md) | Instal·lació i configuració de l'agent en Windows |

---

### 📡 SNMP

| Fitxer | Contingut |
|---|---|
| [`snmpd.md`](snmp/snmpd.md) | Configuració del servei `snmpd` i integració amb Zabbix |

---

### 🔄 Scripts d'autorecuperació

<details>
<summary><b>🐧 recuperacio_apache.sh — Reinici automàtic Apache (Linux)</b></summary>

<br/>

```bash
#!/bin/bash
# Script d'autorecuperació del servei Apache
SERVICE="apache2"

if ! systemctl is-active --quiet $SERVICE; then
    systemctl restart $SERVICE
    echo "$(date): $SERVICE reiniciat automàticament" >> /var/log/zabbix/recuperacio.log
fi
```

📄 [Veure script complet →](scripts/recuperacio_apache.sh)

</details>

<details>
<summary><b>🪟 recuperacio_spooler.ps1 — Reinici automàtic Print Spooler (Windows)</b></summary>

<br/>

```powershell
# Script d'autorecuperació del servei Print Spooler
$service = "Spooler"

if ((Get-Service -Name $service).Status -ne "Running") {
    Start-Service -Name $service
    Add-Content -Path "C:\zabbix\recuperacio.log" -Value "$(Get-Date): $service reiniciat automàticament"
}
```

📄 [Veure script complet →](scripts/recuperacio_spooler.ps1)

</details>

---

###  Captures

El directori `captures/` conté evidències visuals organitzades per categoria:

| Carpeta | Contingut |
|---|---|
| 📁 `installacio-configuracio/` | Instal·lació del servidor i agents Zabbix |
| 📁 `snmp/` | Configuració i test SNMP |
| 📁 `triggers-alertes/` | Triggers actius i alertes generades |
| 📁 `scripts-plugins/` | Execució dels scripts d'autorecuperació |
| 📁 `dashboard-informes/` | Dashboards en temps real i informes PDF |

---

##  Sistema de notificacions

```
Incidència detectada
        │
        ▼
   Trigger actiu
        │
        ├──────────────────────┐
        ▼                      ▼
  📧 Email              📲 Telegram
  Notificació           Notificació
  automàtica            instantània
        │                      │
        └──────────┬───────────┘
                   ▼
         🔄 Script autorecuperació
         (si acció configurada)
```

---

##  Conclusions

Aquest projecte permet demostrar competències en **administració de sistemes**, **monitorització de xarxes** i **automatització de respostes** davant incidències.

La integració de **Zabbix** amb múltiples dispositius, canals de notificació i scripts d'autorecuperació converteix el laboratori en un entorn de monitorització complet i funcional, proper als estàndards dels entorns professionals reals.

---

<div align="center">

*Miniprojecte ASIX2 — Monitorització de Xarxes amb Zabbix*

**Autor: Eric Guerrero**

<br/>

*Supervisió · Alertes · Autorecuperació · SNMP*

</div>
