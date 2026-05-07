# Triggers configurats

Recull dels principals triggers configurats a Zabbix per detectar incidències als hosts monitoritzats.

---

## Client-Linux

### Ús elevat de disc (arrel `/`)

Detecta quan l'ús del disc principal supera el **80%**.

```text
last(/Client-Linux/vfs.fs.dependent.size[/,pused])>80
```

---

### Memòria disponible baixa

Detecta quan la memòria disponible cau per sota del **20%**.

```text
last(/Client-Linux/vm.memory.size[pavailable])<20
```

---

### Servei HTTP (Apache) aturat

Detecta quan el servei web Apache deixa d'estar disponible.

```text
last(/Client-Linux/net.tcp.service[http])=0
```

---

## Client-WIndows

### Ús elevat de disc (`C:`)

Detecta quan l'ús del disc principal supera el **80%**.

```text
last(/Client-WIndows/vfs.fs.dependent.size[C:,pused])>80
```

---

### Ús elevat de CPU

Detecta quan l'ús mitjà de CPU supera el **85%** durant 5 minuts consecutius.

```text
avg(/Client-WIndows/system.cpu.util,5m)>85
```

---

### Servei Print Spooler aturat

Detecta quan el servei Print Spooler no es troba en estat operatiu correcte.

```text
last(/Client-WIndows/service.info[Spooler,state])<>0
```

---

## Vegeu també

- [`accions-zabbix.md`](accions-zabbix.md) — Accions associades als triggers de Servei HTTP (Apache) i Servei Spooler
