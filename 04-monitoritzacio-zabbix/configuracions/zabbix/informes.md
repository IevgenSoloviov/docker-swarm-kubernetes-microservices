# Configuració d'informes

S'ha configurat la generació automàtica d'informes periòdics a Zabbix per facilitar el seguiment de l'estat del sistema i automatitzar l'enviament d'informació rellevant per correu electrònic.

---

## Informes implementats

### Informe global setmanal de monitorització

Informe basat en el dashboard principal del sistema.

| Paràmetre  | Valor                                 |
|------------|---------------------------------------|
| Freqüència | Setmanal                              |
| Base       | Dashboard principal de monitorització |
| Format     | PDF                                   |
| Enviament  | Automàtic per correu electrònic       |

---

### Informe diari d'incidències crítiques

Informe basat en el dashboard d'incidències crítiques.

| Paràmetre  | Valor                             |
|------------|-----------------------------------|
| Freqüència | Diària                            |
| Base       | Dashboard d'incidències crítiques |
| Format     | PDF                               |
| Enviament  | Automàtic per correu electrònic   |

---

## Configuració

Els informes s'han configurat des de la següent ruta de la interfície de Zabbix:

```text
Reports → Scheduled reports
```

Cada informe està associat al dashboard corresponent creat al sistema. Vegeu [`dashboard.md`](dashboard.md) per als detalls dels dashboards utilitzats.

---

## Funcionalitats utilitzades

- Programació automàtica periòdica (diària i setmanal)
- Integració directa amb dashboards personalitzats
- Exportació automàtica en format PDF
- Enviament automàtic per correu electrònic

---

## Validació

S'ha verificat el funcionament complet del sistema d'informes:

- Generació correcta dels informes en format PDF
- Programació diària i setmanal operativa
- Enviament correcte per correu electrònic
- Visualització adequada de la informació exportada

---

## Vegeu també

- [`dashboard.md`](dashboard.md) — Dashboards utilitzats com a base dels informes
- [`notificacions.md`](notificacions.md) — Configuració del canal d'enviament per correu electrònic
