# Configuració SNMP

Configuració bàsica aplicada al dispositiu monitoritzat mitjançant SNMP i integració amb el servidor Zabbix.

---

## Instal·lació

Instal·lació dels paquets necessaris:

```bash
apt install snmp snmpd
```

---

## Fitxer de configuració

```text
/etc/snmp/snmpd.conf
```

### Configuració aplicada

```text
rocommunity public default -V systemonly
rocommunity6 public default -V systemonly
```

---

## Reinici del servei

Un cop aplicats els canvis al fitxer de configuració, cal reiniciar el servei:

```bash
systemctl restart snmpd
```

---

## Validació

Verificació del funcionament del servei SNMP mitjançant:

```bash
snmpwalk -v2c -c public IP_SNMP
```

---

## Integració amb Zabbix

El dispositiu SNMP s'ha afegit a Zabbix seguint els passos següents:

1. Creació d'un nou host de tipus SNMP
2. Assignació de la IP del dispositiu
3. Configuració de la interfície SNMP amb el port `161`
4. Assignació del template `Generic by SNMP`
5. Verificació de la recepció de dades des de la vista **Latest data**

---

## Funcionalitats habilitades

- Monitorització de disponibilitat del dispositiu
- Recollida de dades bàsiques del sistema mitjançant SNMP
- Integració de dispositius sense agent Zabbix instal·lat
