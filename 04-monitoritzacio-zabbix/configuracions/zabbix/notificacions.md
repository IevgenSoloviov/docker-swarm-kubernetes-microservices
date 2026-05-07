# Configuració de notificacions

Recull de la configuració de notificacions implementada a Zabbix per informar automàticament sobre incidències detectades al sistema.

---

## Email

### Configuració

S'ha configurat un media type de tipus **Email** dins de Zabbix mitjançant un servidor SMTP extern.

### Funcionalitats

- Enviament automàtic d'alertes en el moment de la detecció
- Notificació tant d'incidències com de recuperacions
- Associació directa als triggers configurats

### Validació

S'ha verificat la recepció correcta de correus electrònics generats automàticament per Zabbix després de provocar incidències controlades.

---

## Telegram

### Configuració

S'ha implementat la integració amb Telegram com a media type a Zabbix mitjançant:

- Creació d'un bot de Telegram
- Configuració del token d'accés al bot
- Configuració del `chat_id` de destinació

### Funcionalitats

- Enviament automàtic de notificacions en temps real
- Recepció d'alertes associades als triggers configurats

### Validació

S'ha verificat la recepció correcta de notificacions a Telegram després de provocar incidències controlades al sistema.

---

## Integració amb accions

Les notificacions s'executen automàticament a través de les accions configurades a Zabbix. Cada acció té associats els media types d'Email i Telegram, de manera que qualsevol trigger actiu genera notificació simultània pels dos canals.

Vegeu [`accions-zabbix.md`](accions-zabbix.md) per als detalls de les accions configurades.
