# Configuració de l'agent Windows

Configuració bàsica aplicada a l'agent Zabbix del client Windows monitoritzat.

---

## Instal·lació

L'agent Zabbix s'ha instal·lat mitjançant l'executable oficial per a Windows, seguint el procés estàndard d'instal·lació.

---

## Fitxer de configuració

```text
C:\Program Files\Zabbix Agent\zabbix_agentd.conf
```

### Paràmetres configurats

```text
Server=192.168.100.10
ServerActive=192.168.100.10
Hostname=Client-WIndows
AllowKey=system.run[*]
```

> `AllowKey=system.run[*]` és necessari per permetre l'execució remota de scripts des del servidor Zabbix.

---

## Configuració addicional

Per permetre l'execució de scripts PowerShell des del servidor Zabbix, s'ha configurat la política d'execució del sistema:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
```

---

## Reinici del servei

Un cop aplicats els canvis al fitxer de configuració, cal reiniciar el servei:

```powershell
Restart-Service "Zabbix Agent"
```

---

## Funcionalitats habilitades

- Comunicació activa i passiva amb el servidor Zabbix (`192.168.100.10`)
- Monitorització de sistema mitjançant agent
- Execució remota de scripts PowerShell
- Autorecuperació del servei Print Spooler

---

## Validació

S'ha verificat el funcionament correcte de l'agent:

- Connexió establerta correctament amb el servidor Zabbix
- Recepció de dades del host `Client-WIndows`
- Execució remota correcta del script de recuperació del servei Print Spooler

---

## Vegeu també

- [`accions-zabbix.md`](../configuracions/zabbix/accions-zabbix.md) — Acció d'execució remota del script de recuperació Print Spooler sobre aquest host
