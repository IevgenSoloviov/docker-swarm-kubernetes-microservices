# Accions configurades a Zabbix

Recull de les principals accions configurades a Zabbix per automatitzar notificacions i processos de recuperació davant incidències detectades pels triggers.

---

## Acció: Recuperació Apache

### Condició

| Camp    | Valor                                            |
|---------|--------------------------------------------------|
| Trigger | `Client-Linux: Linux - Servei HTTP (Apache) aturat` |

### Operació

Execució remota del script de recuperació sobre el host afectat.

```bash
/usr/local/bin/recuperacio_apache.sh
```

---

## Acció: Recuperació Print Spooler

### Condició

| Camp    | Valor                                                  |
|---------|--------------------------------------------------------|
| Trigger | `Client-WIndows: Windows - Servei Spooler aturat` |

### Operació

Execució remota del script de recuperació sobre el host afectat.

```powershell
powershell.exe -ExecutionPolicy Bypass -File C:\Zabbix\recuperacio_spooler.ps1
```

---

## Acció: Notificacions automàtiques

### Operació

Enviament automàtic de notificacions als usuaris configurats quan s'activa qualsevol trigger crític.

### Canals configurats

| Canal    | Tipus         |
|----------|---------------|
| Email    | Media type    |
| Telegram | Media type    |

---

## Validació

S'ha verificat el funcionament correcte de les següents accions:

- Execució dels scripts de recuperació davant la caiguda dels serveis
- Recepció de notificacions per Email i Telegram
- Detecció automàtica de problemes mitjançant triggers
