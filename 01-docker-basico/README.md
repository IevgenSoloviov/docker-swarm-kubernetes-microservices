<div align="center">

<br/>

```
██████╗  ██████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║  ██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

     B À S I C  ·  D o c k e r   →   K u b e r n e t e s
```

### Desenvolupament i Desplegament de Microserveis en Entorns Cloud

*Docker Compose · Docker Swarm · Kubernetes · Arquitectura LAMP*

<br/>

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Swarm](https://img.shields.io/badge/Docker_Swarm-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

<br/>

</div>

---

## 📋 Descripció del projecte

Aquest projecte implementa el desplegament d'una aplicació contenitzada utilitzant **Docker Compose**, **Docker Swarm** i **Kubernetes**.

L'objectiu és comprendre el procés complet d'evolució d'una arquitectura local basada en contenidors cap a un entorn orquestrat i més proper a producció.

El projecte parteix d'una arquitectura multicapa tipus **LAMP**, formada per una capa web, una capa d'aplicació i una base de dades. Posteriorment, aquesta base serveix com a preparació per a la part avançada del projecte, on es treballa amb una plataforma de microserveis més completa.

---

## 🎯 Objectius principals

- 🐳 Crear un entorn multi-contenidor amb Docker Compose
- 🔄 Migrar el desplegament a Docker Swarm
- ⚙️ Aplicar conceptes bàsics d'orquestració
- 🔐 Implementar mesures bàsiques de seguretat
- ☸️ Migrar el projecte a Kubernetes
- 📦 Crear Deployments, Services, Secrets, ConfigMaps i Ingress
- 📈 Validar escalat i autorecuperació de serveis

---

## 🏗️ Arquitectura general

L'arquitectura del projecte es basa en tres capes principals:

```
┌─────────────────────────────────┐
│       CLIENT / NAVEGADOR        │
└────────────────┬────────────────┘
                 │  HTTP
┌────────────────▼────────────────┐
│             NGINX               │
│         Servidor web            │
└────────────────┬────────────────┘
                 │  FastCGI
┌────────────────▼────────────────┐
│            PHP-FPM              │
│        Capa d'aplicació         │
└────────────────┬────────────────┘
                 │  SQL
┌────────────────▼────────────────┐
│            MariaDB              │
│         Base de dades           │
└─────────────────────────────────┘
```

| Entorn | Comportament |
|---|---|
| 🐳 **Docker Compose** | Serveis en un únic host |
| 🐝 **Docker Swarm** | Serveis orquestrats amb escalat i xarxes overlay |
| ☸️ **Kubernetes** | Objectes declaratius: Pods, Deployments, Services, Secrets, Ingress |

---

## 🚀 Fases del projecte

### Fase 1 — Docker Compose

<details open>
<summary><b>Entorn multi-contenidor local</b></summary>

<br/>

**Components desplegats:**

- 🌐 Nginx com a servidor web
- ⚙️ PHP-FPM com a capa d'aplicació
- 🗄️ MariaDB com a base de dades
- 🔀 Xarxes separades `frontend` i `backend`
- 💾 Volum persistent per a la base de dades
- 📄 Fitxer `.env` per centralitzar la configuració

**Comandes principals:**
```bash
docker compose up -d --build
docker ps
docker compose logs
docker compose down
```

**Docker Compose en funcionament:**

![Docker Compose up](images/docker-compose-up.png)

**Contenidors en execució:**

![Docker PS](images/docker-ps.png)

**Aplicació web accessible:**

![Aplicació web](images/Aplicacio-web.png)

</details>

---

### Fase 2 — Docker Swarm

<details>
<summary><b>Orquestració bàsica distribuïda</b></summary>

<br/>

**Conceptes treballats:**

- 🔧 Inicialització del clúster
- 📦 Desplegament amb `docker stack deploy`
- 🔁 Serveis replicables
- 🌐 Xarxes overlay
- 📈 Escalat manual
- ⚖️ Load balancing intern
- 🔑 Docker Secrets
- 🔄 Polítiques de reinici

**Comandes principals:**
```bash
docker swarm init
docker node ls
docker stack deploy -c docker-stack.yml mystack
docker service ls
docker service scale mystack_app=3
docker service logs mystack_app
```

**Swarm inicialitzat:**

![Docker Swarm Init](images/docker-swarm-init.png)

**Serveis desplegats:**

![Docker Service LS](images/docker-service-ls.png)

**Escalat de rèpliques:**

![Docker Service Scale](images/docker-service-scale.png)

</details>

---

### Fase 3 — Seguretat a Docker Swarm

<details>
<summary><b>Reducció de la superfície d'atac</b></summary>

<br/>

| Mesura | Descripció |
|---|---|
| 🔑 Docker Secrets | Gestió segura de credencials |
| 🌐 Xarxes internes | Aïllament de components |
| 🚫 BD no exposada | La base de dades no és accessible externament |
| 👤 Usuari no privilegiat | Execució sense permisos root |
| 📁 Read-only filesystem | Sistema de fitxers en mode lectura |
| 🔒 TLS automàtic | Comunicació xifrada entre nodes Swarm |

Aquestes mesures permeten apropar el desplegament a un entorn més segur i controlat.

</details>

---

### Fase 4 — Kubernetes

<details>
<summary><b>Desplegament professional amb Minikube</b></summary>

<br/>

**Objectes implementats:**

- 📦 Deployments
- 🔌 Services
- 🔑 Secrets
- ⚙️ ConfigMaps
- 🌍 Ingress
- 📈 Escalat de rèpliques
- 💓 Probes de salut
- 📊 Gestió de recursos amb `requests` i `limits`
- 🔍 Validació amb port-forward i Ingress

**Comandes principals:**
```bash
minikube start
kubectl get nodes
kubectl apply -f kubernetes/
kubectl get pods
kubectl get svc
kubectl scale deployment app-deployment --replicas=3
kubectl port-forward svc/nginx-service 8081:80
```

**Pods en estat Running:**

![Kubectl Get Pods](images/kubectl-get-pods.png)

**Services creats:**

![Kubectl Get SVC](images/kubectl-get-svc.png)

</details>

---

## 🖥️ Accés a l'aplicació

### 🐳 Docker Compose

```bash
docker compose up -d --build
```

> 🌐 **http://localhost:8080/**

---

### ☸️ Kubernetes amb port-forward

```bash
kubectl port-forward svc/nginx-service 8081:80
```

> 🌐 **http://127.0.0.1:8081/**

![Port Forward](images/port-forward.png)

---

### 🌍 Kubernetes amb Ingress

Domini: `microservices.local`

```bash
# Activar l'Ingress Controller
minikube addons enable ingress
minikube tunnel

# Afegir el domini a /etc/hosts
echo "$(minikube ip) microservices.local" | sudo tee -a /etc/hosts
```

> 🌐 **http://microservices.local/**

![Ingress](images/Ingress.png)

---

## 📁 Estructura del repositori

```
01-docker-basico/
│
├── 📁 compose/
│   ├── docker-compose.yml
│   ├── app/
│   └── nginx/
│
├── 📁 swarm/
│   └── docker-stack.yml
│
├── 📁 kubernetes/
│   ├── app-deployment.yaml
│   ├── nginx-deployment.yaml
│   ├── db-deployment.yaml
│   ├── services.yaml
│   ├── ingress.yaml
│   └── secrets.yaml
│
├── 📁 docs/
│   └── annex-projecte-basic.md
│
├── 📁 images/
│
├── .env.example
└── README.md
```

---

## 🔧 Problemes detectats i solucions

<details>
<summary><b>❌ ImagePullBackOff en Kubernetes</b></summary>

<br/>

**Causa:** La imatge no estava disponible dins de Minikube.

**Solució:**
```bash
minikube image load microservices-app:1.0
```

</details>

<details>
<summary><b>❌ NodePort no accessible</b></summary>

<br/>

**Causa:** Limitació de Minikube amb driver Docker.

**Solució:**
```bash
kubectl port-forward svc/nginx-service 8081:80
```

</details>

<details>
<summary><b>❌ Problemes amb hostPath</b></summary>

<br/>

**Causa:** Ruta no accessible dins de Minikube.

**Solució:** Substituir per `ConfigMap` o volum gestionat.

</details>

---

## 📊 Comparativa de tecnologies

| Tecnologia | ✅ Avantatges | ⚠️ Limitacions |
|---|---|---|
| 🐳 **Docker Compose** | Simple, ràpid i útil per desenvolupament local | No és distribuït ni escalable |
| 🐝 **Docker Swarm** | Orquestració senzilla, rèpliques i load balancing | Menys flexible que Kubernetes |
| ☸️ **Kubernetes** | Escalable, robust i molt utilitzat en producció | Més complex de configurar |

---

## 🏁 Conclusions

Aquest projecte ha permès validar el cicle complet de desplegament d'una aplicació contenitzada.

Primer s'ha treballat amb **Docker Compose** per crear un entorn local reproduïble. Després s'ha migrat a **Docker Swarm** per introduir orquestració, escalat i seguretat bàsica. Finalment, s'ha desplegat el projecte a **Kubernetes**, aplicant un model més professional basat en Deployments, Services, Secrets, ConfigMaps i Ingress.

El resultat és una base sòlida per entendre la diferència entre contenidors locals i orquestració en entorns cloud-native.

---

<div align="center">

*Projecte realitzat com a pràctica d'orquestració de contenidors amb Docker Swarm i Kubernetes*

**Docker Compose → Docker Swarm → Kubernetes**

</div>
