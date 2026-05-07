# Configuració del dashboard

S'ha creat un dashboard personalitzat a Zabbix per centralitzar la visualització de l'estat del sistema de monitorització, integrant informació de tots els hosts del laboratori.

---

## Dashboards implementats

S'han creat dos dashboards diferenciats segons el seu objectiu:

### Dashboard principal

Supervisió global del sistema, amb informació agregada de Linux, Windows i SNMP.

### Dashboard d'incidències crítiques

Visualització d'incidències de severitat alta o crítica. S'utilitza també com a base per a la generació d'informes específics.

---

## Widgets utilitzats

| Widget                | Funció                                            |
|-----------------------|---------------------------------------------------|
| Problems              | Llista d'incidències actives al sistema           |
| Host availability     | Estat de disponibilitat dels hosts monitoritzats  |
| Graphs                | Mètriques de CPU, memòria i disc en temps real    |
| Incidències crítiques | Visualització filtrada per severitat alta/crítica |
| Resum per severitat   | Resum global de l'estat del sistema per nivells   |

---

## Sistemes monitoritzats

El dashboard integra informació dels següents hosts del laboratori:

- `Client-Linux`
- `Client-WIndows`
- Dispositiu monitoritzat mitjançant SNMP

---

## Funcionalitats

- Visualització d'incidències actives en temps real
- Supervisió de la disponibilitat dels hosts
- Consulta de mètriques de CPU, memòria i disc
- Centralització de tota la informació del sistema en una sola vista

---

## Validació

S'ha verificat el funcionament correcte de tots els widgets i l'actualització de les dades mostrades al dashboard.

---

## Vegeu també

- [`informes.md`](informes.md) — Informes periòdics generats a partir dels dashboards
- [`accions-zabbix.md`](accions-zabbix.md) — Accions automàtiques associades als triggers del sistema
