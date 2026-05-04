# Docker Swarm i Kubernetes: Desenvolupament i Desplegament de Microserveis en Entorns Cloud

## Descripció del projecte

Aquest projecte implementa el desplegament d'una aplicació contenitzada utilitzant Docker Compose, Docker Swarm i Kubernetes.

L'objectiu és comprendre el procés complet d'evolució d'una arquitectura local basada en contenidors cap a un entorn orquestrat i més proper a producció.

El projecte parteix d'una arquitectura multicapa tipus LAMP, formada per una capa web, una capa d'aplicació i una base de dades. Posteriorment, aquesta base serveix com a preparació per a la part avançada del projecte, on es treballa amb una plataforma de microserveis més completa.

---

## Tecnologies utilitzades

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat&logo=mariadb&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)

- Docker
- Docker Compose
- Docker Swarm
- Kubernetes
- Minikube
- Nginx
- PHP-FPM
- MariaDB
- YAML
- Linux / WSL2

---

## Objectius principals

- Crear un entorn multi-contenidor amb Docker Compose.
- Migrar el desplegament a Docker Swarm.
- Aplicar conceptes bàsics d'orquestració.
- Implementar mesures bàsiques de seguretat.
- Migrar el projecte a Kubernetes.
- Crear Deployments, Services, Secrets, ConfigMaps i Ingress.
- Validar escalat i autorecuperació de serveis.

---

## Arquitectura general

L'arquitectura del projecte es basa en tres capes principals:

```
Client / Navegador
        |
        v
      Nginx
        |
        v
    PHP-FPM
        |
        v
    MariaDB
```

- En **Docker Compose**, els serveis s'executen en un únic host.
- En **Docker Swarm**, els serveis passen a gestionar-se com a serveis orquestrats, amb possibilitat d'escalat i xarxes overlay.
- En **Kubernetes**, l'aplicació es desplega mitjançant objectes declaratius com Pods, Deployments, Services, Secrets i Ingress.

---

## Fases del projecte

### Fase 1 — Docker Compose

En aquesta fase s'ha creat un entorn multi-contenidor amb:

- Nginx com a servidor web.
- PHP-FPM com a capa d'aplicació.
- MariaDB com a base de dades.
- Xarxes separades frontend i backend.
- Volum persistent per a la base de dades.
- Fitxer `.env` per centralitzar la configuració.

**Comandes principals:**
```bash
docker compose up -d --build
docker ps
docker compose logs
docker compose down
```

---

### Fase 2 — Docker Swarm

En aquesta fase s'ha migrat el projecte a Docker Swarm per introduir orquestració bàsica.

S'han treballat els següents conceptes:

- Inicialització del clúster.
- Desplegament amb `docker stack deploy`.
- Serveis replicables.
- Xarxes overlay.
- Escalat manual.
- Load balancing intern.
- Docker Secrets.
- Polítiques de reinici.

**Comandes principals:**
```bash
docker swarm init
docker node ls
docker stack deploy -c docker-stack.yml mystack
docker service ls
docker service scale mystack_app=3
docker service logs mystack_app
```

---

### Fase 3 — Seguretat a Docker Swarm

S'han aplicat mesures bàsiques de seguretat per reduir la superfície d'atac:

- Ús de Docker Secrets.
- Xarxes internes.
- No exposició directa de la base de dades.
- Execució amb usuari no privilegiat.
- Sistema de fitxers en mode read-only.
- Comunicació TLS automàtica entre nodes Swarm.

Aquestes mesures permeten apropar el desplegament a un entorn més segur i controlat.

---

### Fase 4 — Kubernetes

En aquesta fase s'ha migrat l'entorn a Kubernetes utilitzant Minikube.

S'han implementat:

- Deployments.
- Services.
- Secrets.
- ConfigMaps.
- Ingress.
- Escalat de rèpliques.
- Probes de salut.
- Gestió de recursos amb requests i limits.
- Validació amb port-forward i Ingress.

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

---

## Accés a l'aplicació

### Docker Compose
```bash
docker compose up -d --build
```
Accés: [http://localhost:8080/](http://localhost:8080/)

---

### Kubernetes amb port-forward
```bash
kubectl port-forward svc/nginx-service 8081:80
```
Accés: [http://127.0.0.1:8081/](http://127.0.0.1:8081/)

---

### Kubernetes amb Ingress

Domini utilitzat: `microservices.local`

Cal afegir el domini al fitxer `/etc/hosts` i tenir actiu l'Ingress Controller de Minikube.

```bash
minikube addons enable ingress
minikube tunnel
```

---

## Estructura del repositori

```
.
├── compose/
│   ├── docker-compose.yml
│   ├── app/
│   └── nginx/
│
├── swarm/
│   └── docker-stack.yml
│
├── kubernetes/
│   ├── app-deployment.yaml
│   ├── nginx-deployment.yaml
│   ├── db-deployment.yaml
│   ├── services.yaml
│   ├── ingress.yaml
│   └── secrets.yaml
│
├── docs/
│   └── annex-projecte-basic.md
│
├── images/
│
├── .env.example
├── .gitignore
└── README.md
```

---

## Evidències recomanades

Les captures es poden afegir dins la carpeta `images/`.

Captures recomanades:

- Docker Compose funcionant.
- Sortida de `docker ps`.
- Aplicació web accessible.
- Docker Swarm inicialitzat.
- Serveis Swarm desplegats.
- Escalat de rèpliques.
- Kubernetes pods en estat Running.
- Services creats.
- Accés amb port-forward.
- Accés amb Ingress.

Exemple d'inserció d'una captura:

```markdown
![Docker Compose funcionant](images/compose-web.png)
```

---

## Problemes detectats i solucions

### ImagePullBackOff en Kubernetes

**Causa:** la imatge no estava disponible dins de Minikube.

**Solució:**
```bash
minikube image load microservices-app:1.0
```

---

### NodePort no accessible

**Causa:** limitació de Minikube amb driver Docker.

**Solució:**
```bash
kubectl port-forward svc/nginx-service 8081:80
```

---

### Problemes amb hostPath

**Causa:** ruta no accessible dins de Minikube.

**Solució:** substituir per ConfigMap o volum gestionat.

---

## Comparativa de tecnologies

| Tecnologia | Avantatges | Limitacions |
|---|---|---|
| Docker Compose | Simple, ràpid i útil per desenvolupament local | No és distribuït ni escalable |
| Docker Swarm | Orquestració senzilla, rèpliques i load balancing | Menys flexible que Kubernetes |
| Kubernetes | Escalable, robust i molt utilitzat en producció | Més complex de configurar |

---

## Conclusions

Aquest projecte ha permès validar el cicle complet de desplegament d'una aplicació contenitzada.

Primer s'ha treballat amb Docker Compose per crear un entorn local reproduïble. Després s'ha migrat a Docker Swarm per introduir orquestració, escalat i seguretat bàsica. Finalment, s'ha desplegat el projecte a Kubernetes, aplicant un model més professional basat en Deployments, Services, Secrets, ConfigMaps i Ingress.

El resultat és una base sòlida per entendre la diferència entre contenidors locals i orquestració en entorns cloud-native.

---

## Autor

Projecte realitzat com a pràctica d'orquestració de contenidors amb Docker Swarm i Kubernetes.


.idea/
```
