<div align="center">

<br/>

```
 █████╗ ███████╗██╗██╗  ██╗    ██████╗ 
██╔══██╗██╔════╝██║╚██╗██╔╝    ╚════██╗
███████║███████╗██║ ╚███╔╝      █████╔╝
██╔══██║╚════██║██║ ██╔██╗     ██╔═══╝ 
██║  ██║███████║██║██╔╝ ██╗    ███████╗
╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝    ╚══════╝

     P r o j e c t e   I n t e r m o d u l a r
  A d m i n i s t r a c i ó   d e   S i s t e m e s
        I n f o r m à t i c s   e n   X a r x a
```

### Contenidors · Microserveis · Ciberseguretat · Automatització

*Docker · Kubernetes · Helm · Istio · Ansible · Suricata · Elastic Stack*

<br/>

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)
![Istio](https://img.shields.io/badge/Istio-466BB0?style=for-the-badge&logo=istio&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elastic_Stack-005571?style=for-the-badge&logo=elastic&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Suricata](https://img.shields.io/badge/Suricata-IDS%2FIPS-orange?style=for-the-badge)
![Nmap](https://img.shields.io/badge/Nmap-Network%20Scanning-004170?style=for-the-badge)
![iptables](https://img.shields.io/badge/iptables-Firewall%20%26%20NAT-333333?style=for-the-badge)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Playbooks-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-Managed%20Nodes-A81D33?style=for-the-badge&logo=debian&logoColor=white)

<br/>

</div>

---

##  Descripció general

Aquest repositori recull el desenvolupament complet del **projecte intermodular del cicle ASIX**, estructurat en tres blocs que cobreixen àrees clau de l'administració de sistemes moderns.

L'objectiu és simular un entorn real on es despleguen serveis, s'orquestren infraestructures i es protegeixen mitjançant sistemes automatitzats de monitorització i seguretat.

> **Enfocament:** Cada bloc és independent a nivell tècnic, però tots formen part del mateix projecte intermodular i permeten demostrar competències complementàries en contenidors, orquestració, automatització i ciberseguretat.

---

##  Objectius principals

- 🐳 Dominar el cicle complet de contenització i orquestració
- ☸️ Desplegar arquitectures cloud-native amb Kubernetes
- 🎛️ Gestionar infraestructures complexes amb Helm i Istio
- 🤖 Automatitzar desplegaments i configuracions amb Ansible
- 🛡️ Detectar, analitzar i respondre a atacs amb IDS/IPS
- 📊 Monitoritzar serveis i infraestructura en temps real

---

##  Estructura del repositori

```
asix-projecte-intermodular/
│
├── 📁 01-docker-basico/       # Contenització i orquestració base
├── 📁 02-microservices-avanzado/  # Plataforma de microserveis avançada
└── 📁 03-ids-ips-ansible/     # Ciberseguretat i automatització
```

---

##  Projectes inclosos

### 🔹 01 — Docker Bàsic

<details open>
<summary><b>Arquitectura multicapa · Docker Compose → Swarm → Kubernetes</b></summary>

<br/>

Implementació d'una arquitectura multicapa clàssica (web + app + DB) progressant des d'un entorn local fins a una orquestració completa.

**Tecnologies:**

- 🐳 Docker Compose
- 🐝 Docker Swarm
- ☸️ Kubernetes (base)
- 🌐 Nginx + PHP-FPM + MariaDB

**Conceptes treballats:**

- Contenització i xarxes multi-contenidor
- Orquestració distribuïda amb Swarm
- Deployments, Services, Secrets i Ingress a Kubernetes
- Healthchecks i probes de salut
- Seguretat bàsica amb Docker Secrets

> **Objectiu:** Aprendre el cicle complet de contenització i orquestració, des del desenvolupament local fins a un entorn orquestrat.

</details>

---

### 🔹 02 — ShopMicro · Microserveis Avançats

<details>
<summary><b>Plataforma cloud-native · Kubernetes · Helm · Istio · Observabilitat</b></summary>

<br/>

Plataforma completa de microserveis que simula un entorn real de producció, adaptada com a sistema de gestió d'incidències urbanes.

**Tecnologies:**

- ☸️ Kubernetes avançat (HPA, StatefulSets, ConfigMaps)
- 🌍 Ingress Controller amb domini personalitzat
- 🎛️ Helm per a la gestió del cicle de vida
- 🕸️ Istio Service Mesh (timeouts, retries, circuit breaker)
- 📊 Prometheus + Grafana per a observabilitat
- 🔭 Kiali per a visualització del graf de serveis

**Microserveis desplegats:**

| Servei | Rol |
|---|---|
| **product-service** | Gestió de productes / incidències |
| **order-service** | Gestió de comandes / assignacions |
| **user-service** | Gestió d'usuaris i autenticació |
| **MySQL** | Persistència de dades (StatefulSet) |
| **Redis** | Cache distribuïda |
| **RabbitMQ** | Missatgeria asíncrona |

> **Objectiu:** Simular un entorn real de producció cloud-native amb escalat automàtic, control de trànsit i observabilitat completa.

</details>

---

### 🔹 03 — IDS/IPS + Ansible · Ciberseguretat i Automatització

<details>
<summary><b>Detecció d'intrusions · Resposta activa · Desplegament automatitzat</b></summary>

<br/>

Projecte de ciberseguretat que implementa un sistema de detecció i prevenció d'intrusions sobre la infraestructura desplegada, amb automatització completa via Ansible.

**Tecnologies:**

- 🤖 Ansible (desplegament i configuració automatitzada)
- 🐳 Docker (infraestructura de serveis)
- 🛡️ Suricata IDS/IPS (detecció i prevenció)
- 📦 Elastic Stack — Elasticsearch + Kibana (anàlisi i visualització)
- 🔥 iptables (resposta activa i bloqueig)

**Funcionalitats implementades:**

- Desplegament automatitzat de tota la infraestructura
- Detecció de trànsit maliciós en temps real
- Anàlisi d'alertes i correlació d'events
- Resposta activa automàtica amb bloqueig d'IPs
- Dashboards de seguretat a Kibana

> **Objectiu:** Detectar, analitzar i respondre a atacs dins una infraestructura real de forma automatitzada.

</details>

---

##  Relació entre projectes

Els tres blocs del repositori formen part del mateix **projecte intermodular d’ASIX**, però no representen una única infraestructura connectada tècnicament entre si.

Cada bloc treballa una àrea diferent de l’administració de sistemes i té el seu propi entorn, objectius, tecnologies i validacions. La relació entre ells és principalment **acadèmica i competencial**, ja que tots contribueixen a demostrar coneixements relacionats amb contenidors, orquestració, automatització, monitorització i ciberseguretat.

```
┌─────────────────────────────────────────────────────────────────────┐
│                  PROJECTE INTERMODULAR ASIX                         │
├──────────────────────┬──────────────────────┬───────────────────────┤
│  01 · DOCKER BÀSIC   │  02 · SHOPMICRO      │  03 · IDS/IPS +       │
│                      │                      │       ANSIBLE         │
│  Contenització       │  Microserveis        │  Ciberseguretat       │
│  Docker Compose      │  Kubernetes avançat  │  Automatització       │
│  Swarm · K8s base    │  Helm · Istio        │  Suricata · Elastic   │
└──────────────────────┴──────────────────────┴───────────────────────┘
```

### Enfocament de cada bloc

| Bloc | Àrea principal | Finalitat |
|---|---|---|
| **01 · Docker Bàsic** | Contenització i orquestració inicial | Aprendre a desplegar serveis amb Docker Compose, Docker Swarm i Kubernetes bàsic |
| **02 · ShopMicro** | Microserveis i cloud-native | Implementar una arquitectura avançada amb Kubernetes, Helm, Istio, HPA i observabilitat |
| **03 · IDS/IPS + Ansible** | Automatització i ciberseguretat | Automatitzar una infraestructura amb Ansible i protegir-la amb Suricata, Elastic Stack i iptables |

### Relació global

Tot i que els projectes no depenen directament els uns dels altres, segueixen una evolució lògica dins del cicle:

```
Contenització → Orquestració avançada → Automatització i seguretat
      01                  02                      03
```

Aquesta organització permet demostrar una visió completa de l’administració de sistemes moderns:

- desplegament de serveis amb contenidors;
- gestió d’infraestructures orquestrades;
- automatització de configuracions;
- monitorització i anàlisi d’esdeveniments;
- detecció i resposta davant incidents de seguretat.

Per tant, la connexió entre els blocs no és una connexió tècnica directa, sinó una connexió formativa: cada projecte cobreix una part diferent de les competències treballades durant el projecte intermodular.

---

##  Stack tecnològic complet

| Àrea | Tecnologies |
|---|---|
| **Contenidors** | Docker · Docker Compose · Docker Swarm |
| **Orquestració** | Kubernetes · Minikube · kubectl |
| **Packaging** | Helm |
| **Service Mesh** | Istio · Envoy · Kiali |
| **Automatització** | Ansible |
| **Seguretat** | Suricata IDS/IPS · iptables |
| **Anàlisi** | Elasticsearch · Kibana |
| **Observabilitat** | Prometheus · Grafana |
| **Sistema** | Linux · Bash |

---

## Conclusions

Aquest projecte intermodular integra les àrees fonamentals de l'administració de sistemes moderns en un entorn coherent i progressiu:

- **Contenització i orquestració** com a base de qualsevol infraestructura actual
- **Arquitectura de microserveis** com a estàndard dels entorns de producció cloud-native
- **Automatització** per eliminar errors humans i garantir la reproductibilitat
- **Ciberseguretat activa** com a capa imprescindible en qualsevol desplegament real

El resultat és un entorn complet que cobreix el cicle de vida sencer d'una infraestructura: des del desplegament fins a la protecció i monitorització activa.

---

<div align="center">

*Projecte intermodular desenvolupat dins del cicle formatiu*
*Administració de Sistemes Informàtics en Xarxa — ASIX*

**Infraestructura → Microserveis → Seguretat**

</div>
