# Configuració de l'agent Linux

Configuració bàsica aplicada a l'agent Zabbix del client Linux monitoritzat.

---

## Instal·lació

Instal·lació del paquet de l'agent Zabbix:

```bash
apt install zabbix-agent
```

---

## Fitxer de configuració

```text
/etc/zabbix/zabbix_agentd.conf
```

### Paràmetres configurats

```text
Server=192.168.100.10
ServerActive=192.168.100.10
Hostname=Client-Linux
AllowKey=system.run[*]
```

> `AllowKey=system.run[*]` és necessari per permetre l'execució remota de scripts des del servidor Zabbix.

---

## Reinici del servei

Un cop aplicats els canvis al fitxer de configuració, cal reiniciar el servei:

```bash
systemctl restart zabbix-agent
```

---

## Funcionalitats habilitades

- Comunicació activa i passiva amb el servidor Zabbix (`192.168.100.10`)
- Monitorització de sistema mitjançant agent
- Execució remota de scripts per a processos d'autorecuperació

---

## Validació

S'ha verificat el funcionament correcte de l'agent:

- Connexió establerta correctament amb el servidor Zabbix
- Recepció de dades del host `Client-Linux`
- Execució remota correcta del script de recuperació Apache

---

## Vegeu també

- [`accions-zabbix.md`](../configuracions/zabbix/accions-zabbix.md) — Acció d'execució remota del script de recuperació Apache sobre aquest host
