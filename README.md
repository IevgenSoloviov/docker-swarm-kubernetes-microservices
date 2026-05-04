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

<br/>

</div>

---

## 📋 Descripció general

Aquest repositori recull el desenvolupament complet del **projecte intermodular del cicle ASIX**, estructurat en tres blocs que cobreixen àrees clau de l'administració de sistemes moderns.

L'objectiu és simular un entorn real on es despleguen serveis, s'orquestren infraestructures i es protegeixen mitjançant sistemes automatitzats de monitorització i seguretat.

> **Enfocament:** Cada bloc és independent, però tots formen part d'un mateix entorn integrat que evoluciona des del desplegament fins a la protecció activa.

---

## 🎯 Objectius principals

- 🐳 Dominar el cicle complet de contenització i orquestració
- ☸️ Desplegar arquitectures cloud-native amb Kubernetes
- 🎛️ Gestionar infraestructures complexes amb Helm i Istio
- 🤖 Automatitzar desplegaments i configuracions amb Ansible
- 🛡️ Detectar, analitzar i respondre a atacs amb IDS/IPS
- 📊 Monitoritzar serveis i infraestructura en temps real

---

## 📁 Estructura del repositori

```
asix-projecte-intermodular/
│
├── 📁 01-docker-basico/       # Contenització i orquestració base
├── 📁 02-microservices-avanzado/  # Plataforma de microserveis avançada
└── 📁 03-ids-ips-ansible/     # Ciberseguretat i automatització
```

---

## 🗂️ Projectes inclosos

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

## 🔗 Relació entre projectes

Els tres blocs no són independents, sinó que representen **fases d'un mateix entorn integrat**:

```
┌─────────────────────────────────────────────────────────────┐
│                     ENTORN COMPLET ASIX                     │
├──────────────────┬──────────────────┬───────────────────────┤
│  01 · DOCKER     │  02 · SHOPMICRO  │  03 · IDS/IPS         │
│                  │                  │                       │
│  Infraestructura │  Microserveis    │  Seguretat            │
│  Kubernetes      │  Helm · Istio    │  Ansible · Suricata   │
│  Base            │  Avançat         │  Elastic Stack        │
└──────────────────┴──────────────────┴───────────────────────┘
```

**Flux complet de l'entorn:**

```
Infraestructura → Microserveis → Trànsit → IDS → Anàlisi → Resposta
      01               02           02       03      03         03
```

| Fase | Bloc | Descripció |
|---|---|---|
| **1** | Docker Bàsic | Desplegament i orquestració de serveis |
| **2** | ShopMicro | Infraestructura de microserveis en producció |
| **3** | IDS/IPS | Monitorització, detecció i resposta a atacs |

---

## 🛠️ Stack tecnològic complet

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

## 🏁 Conclusions

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
