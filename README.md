<div align="center">

<br/>

```
██╗  ██╗ █████╗ ██████╗ ███████╗    ██████╗ ███████╗██╗   ██╗ ██████╗ ██████╗ ███████╗
██║ ██╔╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔════╝██║   ██║██╔═══██╗██╔══██╗██╔════╝
█████╔╝ ╚█████╔╝██████╔╝███████╗    ██║  ██║█████╗  ╚██╗ ██╔╝██║   ██║██████╔╝███████╗
██╔═██╗ ██╔══██╗██╔══██╗╚════██║    ██║  ██║██╔══╝   ╚████╔╝ ██║   ██║██╔═══╝ ╚════██║
██║  ██╗╚█████╔╝██║  ██║███████║    ██████╔╝███████╗  ╚██╔╝  ╚██████╔╝██║     ███████║
╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚══════╝

                    P  O  R  T  F  O  L  I  O
```

### Del contenidor local a la producció cloud-native

*Docker · Swarm · Kubernetes · Helm · Istio · Prometheus · Grafana*

<br/>

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)
![Istio](https://img.shields.io/badge/Istio-466BB0?style=for-the-badge&logo=istio&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

<br/>

</div>

---

## 👋 Sobre aquest repositori

Aquest repositori recull el cicle complet d'aprenentatge en **orquestració de contenidors**, des d'un entorn local amb Docker Compose fins a una arquitectura de microserveis professional amb Kubernetes, Helm i Istio.

Els dos projectes estan estructurats de forma progressiva: el primer estableix les bases, el segon aplica conceptes avançats d'un entorn real de producció.

---

## 📂 Estructura del repositori

```
kubernetes-devops-portfolio/
│
├── 📁 01-docker-basico/         ← Projecte base: Docker Compose → Swarm → Kubernetes
│   ├── README.md
│   ├── compose/
│   ├── swarm/
│   ├── kubernetes/
│   ├── docs/
│   └── images/
│
├── 📁 02-microservices-avanzado/ ← Projecte avançat: ShopMicro + Helm + Istio
│   ├── README.md
│   ├── compose/
│   ├── swarm/
│   ├── k8s/
│   ├── helm/
│   ├── istio/
│   ├── docs/
│   └── images/
│
├── .gitignore
└── README.md                    ← Estàs aquí
```

---

## 🗺️ Roadmap d'aprenentatge

```
[1] Docker Compose        →   Entorn local multi-contenidor
        ↓
[2] Docker Swarm          →   Orquestració bàsica + seguretat
        ↓
[3] Kubernetes            →   Deployments, Services, Ingress, Secrets
        ↓
[4] Kubernetes Avançat    →   HPA, StatefulSets, Probes, Helm
        ↓
[5] Istio Service Mesh    →   Circuit breaker, retries, observabilitat
        ↓
[6] Monitorització        →   Prometheus + Grafana + Kiali
```

---

## 📦 Projecte 01 — Docker Bàsic

> **Arquitectura multicapa LAMP contenitzada i orquestrada**

```
Nginx  →  PHP-FPM  →  MariaDB
```

| Fase | Tecnologia | Conceptes |
|---|---|---|
| 1 | Docker Compose | Multi-contenidor, xarxes, volums |
| 2 | Docker Swarm | Orquestració, escalat, overlay |
| 3 | Seguretat | Secrets, read-only, usuari no privilegiat |
| 4 | Kubernetes | Deployments, Ingress, ConfigMaps, HPA |

📁 **[Veure projecte →](./01-docker-basico/README.md)**

---

## 🚀 Projecte 02 — ShopMicro (Avançat)

> **Plataforma de microserveis cloud-native amb Service Mesh i monitorització**

```
Ingress  →  API Gateway  →  product / order / user  →  MySQL · Redis · RabbitMQ
```

| Fase | Tecnologia | Conceptes |
|---|---|---|
| 1 | Kubernetes | StatefulSets, HPA, probes |
| 2 | Helm | Packaging, upgrades, historial |
| 3 | Istio | Service Mesh, circuit breaker, retries |
| 4 | Observabilitat | Prometheus, Grafana, Kiali |

📁 **[Veure projecte →](./02-microservices-avanzado/README.md)**

---

## 🛠️ Tecnologies utilitzades

<div align="center">

| Capa | Eines |
|---|---|
| **Contenidors** | Docker, Docker Compose |
| **Orquestració bàsica** | Docker Swarm |
| **Orquestració avançada** | Kubernetes, Minikube |
| **Packaging** | Helm |
| **Service Mesh** | Istio, Envoy |
| **Monitorització** | Prometheus, Grafana, Kiali |
| **Web / App** | Nginx, PHP-FPM |
| **Bases de dades** | MariaDB, MySQL |
| **Cache / Cues** | Redis, RabbitMQ |
| **Infraestructura** | Linux, WSL2, YAML |

</div>

---

## 🔐 .gitignore

Un sol `.gitignore` a l'arrel cobreix tot el repositori:

```gitignore
.env
*.log
.DS_Store
node_modules/
__pycache__/
.vscode/
.idea/
```

---

<div align="center">

*Projecte d'aprenentatge progressiu en DevOps i orquestració de contenidors*

**Docker → Swarm → Kubernetes → Helm → Istio**

</div>
