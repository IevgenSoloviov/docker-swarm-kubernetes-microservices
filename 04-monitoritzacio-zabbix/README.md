# Monitorització de Xarxes amb Zabbix

Miniprojecte ASIX2 · Eric Guerrero

Implementació d'un sistema de monitorització en entorn de laboratori virtualitzat, amb supervisió de dispositius Linux, Windows i SNMP, detecció d'incidències, notificacions automàtiques i mecanismes d'autorecuperació.

---

## Objectiu

Desplegar un sistema de monitorització amb Zabbix capaç de supervisar múltiples dispositius i serveis, configurar alertes i triggers, enviar notificacions automàtiques per Email i Telegram, i aplicar scripts d'autorecuperació davant incidències crítiques.

---

## Entorn del laboratori

| Rol                  | Sistema operatiu |
|----------------------|------------------|
| Servidor Zabbix      | Linux            |
| Client Linux         | Linux            |
| Client Windows       | Windows          |
| Dispositiu SNMP      | Linux (snmpd)    |

---

## Funcionalitats implementades

- Monitorització de CPU, memòria i espai en disc
- Monitorització de serveis: Apache (Linux) i Print Spooler (Windows)
- Configuració de triggers i alertes per llindar crític
- Notificacions automàtiques per **Email** i **Telegram**
- Scripts d'autorecuperació per a serveis caiguts
- Integració SNMP per a dispositius de xarxa
- Dashboards personalitzats amb visualització en temps real
- Generació d'informes periòdics en PDF
- Proves i validació del sistema complet

---

## Tecnologies utilitzades

| Tecnologia  | Ús                                      |
|-------------|------------------------------------------|
| Zabbix      | Plataforma de monitorització central     |
| Linux       | Servidor Zabbix i agent Linux            |
| Windows     | Agent Windows i servei Print Spooler     |
| SNMP        | Monitorització de dispositiu de xarxa    |
| Bash        | Script d'autorecuperació Apache          |
| PowerShell  | Script d'autorecuperació Print Spooler   |

---

## Estructura del repositori

```text
monitoritzacio-zabbix/
├── README.md
├── agents/
│   ├── agent-linux.md
│   └── agent-windows.md
├── captures/
│   ├── dashboard-informes/
│   ├── installacio-configuracio/
│   ├── scripts-plugins/
│   ├── snmp/
│   └── triggers-alertes/
├── configuracions/
│   └── zabbix/
│       ├── accions-zabbix.md
│       ├── dashboard.md
│       ├── informes.md
│       ├── notificacions.md
│       └── triggers.md
├── scripts/
│   ├── recuperacio_apache.sh
│   └── recuperacio_spooler.ps1
└── snmp/
    └── snmpd.md
```

---

## Contingut del repositori

### Configuracions Zabbix
Documentació de totes les configuracions aplicades al servidor Zabbix:
- [`triggers.md`](configuracions/zabbix/triggers.md) — Triggers configurats per CPU, memòria, disc i serveis
- [`accions-zabbix.md`](configuracions/zabbix/accions-zabbix.md) — Accions automàtiques i execució de scripts remots
- [`notificacions.md`](configuracions/zabbix/notificacions.md) — Canals de notificació: Email i Telegram
- [`dashboard.md`](configuracions/zabbix/dashboard.md) — Configuració del dashboard personalitzat
- [`informes.md`](configuracions/zabbix/informes.md) — Generació d'informes periòdics en PDF

### Agents
Documentació de la instal·lació i configuració dels agents Zabbix:
- [`agent-linux.md`](agents/agent-linux.md) — Agent en el client Linux
- [`agent-windows.md`](agents/agent-windows.md) — Agent en el client Windows

### SNMP
- [`snmpd.md`](snmp/snmpd.md) — Configuració del servei `snmpd` i integració amb Zabbix

### Scripts d'autorecuperació
- [`recuperacio_apache.sh`](scripts/recuperacio_apache.sh) — Reinici automàtic del servei Apache en Linux
- [`recuperacio_spooler.ps1`](scripts/recuperacio_spooler.ps1) — Reinici automàtic del Print Spooler en Windows

### Captures
El directori `captures/` conté evidències visuals organitzades per categoria:

| Carpeta                  | Contingut                                      |
|--------------------------|------------------------------------------------|
| `installacio-configuracio/` | Instal·lació del servidor i agents Zabbix   |
| `snmp/`                  | Configuració i test SNMP                       |
| `triggers-alertes/`      | Triggers actius i alertes generades            |
| `scripts-plugins/`       | Execució dels scripts d'autorecuperació        |
| `dashboard-informes/`    | Dashboards en temps real i informes PDF        |

---

## Autor

**Eric Guerrero**  
Miniprojecte ASIX2 — Monitorització de Xarxes amb Zabbix
