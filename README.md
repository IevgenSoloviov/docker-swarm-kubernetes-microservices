# Docker Swarm i Kubernetes: Desenvolupament i Desplegament de Microserveis en Entorns Cloud

## Informació del projecte

Aquest repositori recull el desenvolupament complet del projecte **Docker Swarm i Kubernetes: Desenvolupament i Desplegament de Microserveis en Entorns Cloud**, realitzat dins del marc del cicle formatiu **ASIX2**.

El projecte mostra l'evolució d'una arquitectura multicapa des d'un entorn local amb **Docker Compose**, passant per una orquestració amb **Docker Swarm**, fins a una migració final a **Kubernetes** amb **Minikube**.

## Repositori GitHub

Segons els requisits del projecte, s'ha utilitzat un compte de GitHub per centralitzar tota la documentació tècnica, configuracions, captures, demostracions i fitxers del projecte.

Cal que el repositori tingui com a col·laborador obligatori el compte del professorat: `projectesasixsapalomera`

La URL del repositori s'ha d'indicar també a la portada, annex o apartat corresponent de la memòria final.

**URL del repositori:** `https://github.com/IevgenSoloviov/docker-swarm-kubernetes-microservices`

---

## Índex

1. [Fase 1 — Configuracions i desplegament amb Docker Compose](#fase-1--configuracions-i-desplegament-amb-docker-compose)
2. [Fase 2 — Orquestració i desplegament amb Docker Swarm](#fase-2--orquestració-i-desplegament-amb-docker-swarm)
3. [Fase 3 — Seguretat a Docker Swarm](#fase-3--seguretat-a-docker-swarm)
4. [Fase 4 — Orquestració amb Kubernetes](#fase-4--orquestració-amb-kubernetes)
5. [Estructura del repositori](#estructura-del-repositori)
6. [Tecnologies utilitzades](#tecnologies-utilitzades)
7. [Conclusions finals](#conclusions-finals)

---

## Fase 1 — Configuracions i desplegament amb Docker Compose

### 1. Objectiu de la fase

L'objectiu d'aquesta fase és crear un entorn multi-contenidor amb Docker Compose que simuli una arquitectura multicapa tipus LAMP, formada per capa web, capa d'aplicació i base de dades, de forma repetible i preparada per a futures migracions a Docker Swarm i Kubernetes.

### 2. Introducció a Docker Compose

Docker Compose permet definir i desplegar múltiples serveis Docker mitjançant un únic fitxer `docker-compose.yml`. Aquesta eina facilita la gestió de dependències, xarxes i volums, i garanteix que l'entorn es pugui recrear de forma consistent en qualsevol sistema.

#### Avantatges de Docker Compose

- Permet definir múltiples serveis en un únic fitxer declaratiu.
- Facilita la gestió de dependències entre serveis.
- Simplifica la recreació d'entorns.
- Permet versionar la infraestructura com a codi.
- Redueix errors humans en la configuració manual.

#### Inconvenients

- No està pensat per a entorns distribuïts.
- No gestiona alta disponibilitat.
- No distribueix càrrega entre múltiples nodes.
- No implementa estratègies avançades d'actualització.

### 3. Disseny de l'entorn multi-nivell

S'ha implementat una arquitectura de tres capes formada per:

- **Nginx** com a servidor web i reverse proxy.
- **PHP-FPM** com a capa d'aplicació.
- **MariaDB** com a capa de dades i persistència.

Per millorar la seguretat i l'organització del desplegament:

- S'han creat dues xarxes: `frontend` i `backend`.
- La xarxa `backend` s'ha configurat com a interna (`internal: true`) per evitar exposar la base de dades a l'exterior.
- S'ha utilitzat un volum `db_data` per garantir la persistència de dades.

### 4. Configuració realitzada

#### Fitxers principals del projecte

- `.env`: paràmetres configurables com ports i credencials.
- `docker-compose.yml`: definició dels serveis, xarxes i volums.
- `app/Dockerfile`: imatge personalitzada per al servei PHP-FPM.
- `nginx/conf.d/default.conf`: configuració del servidor web.
- `app/src/index.php`: pàgina de prova basada en `phpinfo()`.

### 5. Desplegament

#### Comandes executades

```bash
docker compose up -d --build
docker ps
```

#### Validació

La validació funcional s'ha realitzat accedint a `http://localhost:8080`. La pàgina `phpinfo()` s'ha mostrat correctament, confirmant el funcionament dels serveis i la comunicació entre les diferents capes.

### 6. Mesures bàsiques de seguretat aplicades

S'han aplicat diverses bones pràctiques bàsiques de seguretat:

- Xarxa backend interna per limitar l'exposició de la base de dades.
- Configuració `read_only` i `tmpfs` al servei Nginx per reduir la superfície d'atac.
- Variables centralitzades a `.env` i `.env.example` per evitar credencials hardcodejades.

Tot i que Docker Compose no està orientat a entorns productius distribuïts, aquestes mesures permeten construir un entorn local més ordenat i segur. La dependència entre serveis es resol mitjançant el sistema DNS intern de Docker.

#### 6.1 Implementació de healthchecks en Docker Compose

S'han configurat comprovacions d'estat per a:

- MariaDB
- PHP-FPM
- Nginx

Això permet verificar que els serveis es troben en estat `healthy` i facilita la detecció de problemes durant l'inici o el funcionament.

### 7. Evidències

**Evidència A — Versions Docker i Compose**

S'ha validat l'entorn executant:

```bash
docker --version
docker compose version
```

S'ha utilitzat Docker Desktop amb WSL2 (Ubuntu) per disposar d'un entorn Linux integrat.

**Evidència B — Estructura del projecte**

Captura de l'estructura general del projecte amb els fitxers més importants.

**Evidències C, D, E, F i G — Fitxers clau**

Creació dels fitxers principals: `.env`, `app/src/index.php`, `nginx/conf.d/default.conf`, `app/Dockerfile`, `docker-compose.yml`.

**Evidència H — Contenidors en execució**

```bash
docker ps
```

**Evidència I — Validació web**

Accés a `http://localhost:8080`.

**Evidència J — Logs dels serveis**

Validació de l'arrencada i funcionament dels contenidors mitjançant els logs.

**Fitxers complementaris:** `.gitignore`, `.env.example` amb credencials fictícies.

### 8. Resultat de la fase

Aquesta fase ha permès crear una arquitectura multicapa funcional i reproduïble mitjançant infraestructura declarativa. Docker Compose és adequat per al desenvolupament local, però presenta limitacions en entorns distribuïts, fet que justifica la seva evolució posterior cap a Docker Swarm.

---

## Fase 2 — Orquestració i desplegament amb Docker Swarm

### 1. Objectiu de la fase

L'objectiu d'aquesta fase és transformar l'entorn multi-contenidor creat amb Docker Compose en una infraestructura orquestrada amb Docker Swarm.

Aquesta fase introdueix:

- Arquitectura basada en serveis.
- Escalat manual de rèpliques.
- Xarxes overlay distribuïdes.
- Gestió declarativa de serveis.
- Actualitzacions controlades i reinici automàtic.

### 2. Principis de Docker Swarm

Docker Swarm és l'orquestrador natiu de Docker. Permet agrupar diversos nodes en un clúster lògic administrat per un o més nodes manager.

#### Components principals

- **Node Manager**: coordina el clúster i distribueix les tasques.
- **Node Worker**: executa serveis.
- **Service**: definició declarativa d'un contenidor replicable.
- **Task**: instància individual assignada a un node.
- **Overlay Network**: xarxa distribuïda entre nodes.
- **Replicas**: nombre d'instàncies actives d'un servei.

#### Diferències entre Docker Compose i Docker Swarm

| Docker Compose | Docker Swarm |
|----------------|--------------|
| Entorn local | Entorn orquestrat |
| `docker compose up` | `docker stack deploy` |
| Xarxa bridge | Xarxa overlay |
| No gestiona alta disponibilitat | Permet rèpliques |
| No distribueix càrrega | Load balancing intern |

#### Avantatges de Docker Swarm

- Integració nativa amb Docker Engine.
- Simplicitat d'implementació.
- Escalat ràpid amb comandes senzilles.
- Load balancing intern automàtic.
- Suport per actualitzacions controlades i rollback.

#### Inconvenients

- Menor flexibilitat que Kubernetes.
- Comunitat més reduïda.
- Funcionalitats avançades més limitades.

### 3. Configuració del clúster

Per inicialitzar el clúster:

```bash
docker swarm init
```

#### Validació de l'estat del clúster

```bash
docker node ls
```

En aquesta implementació s'ha treballat amb un clúster d'un únic node manager, suficient per validar funcionalitats bàsiques d'orquestració.

#### Afegir nodes al clúster

```bash
docker swarm join-token worker
```

Swarm activa automàticament comunicació xifrada mitjançant TLS entre nodes.

### 4. Conceptes de desplegament i escalat en Swarm

En Docker Swarm, els serveis es defineixen en un fitxer `docker-stack.yml`. A diferència de Docker Compose, s'utilitzen conceptes com `deploy`, `replicas`, xarxes overlay i estratègies d'actualització.

L'escalat es realitza amb:

```bash
docker service scale
```

### 5. Migració del projecte de Compose a Swarm

La migració ha implicat:

- Adaptació de `docker-compose.yml` a `docker-stack.yml`
- Eliminació de paràmetres no compatibles
- Incorporació de la secció `deploy`
- Substitució de xarxes bridge per xarxes overlay
- Construcció manual prèvia de la imatge personalitzada

#### Desplegament del stack

```bash
docker stack deploy -c docker-stack.yml mystack
```

#### Verificació de serveis

```bash
docker service ls
```

#### 5.1 Diferències tècniques detectades durant la migració

- En Swarm, `docker stack deploy` no construeix imatges automàticament; la imatge s'ha de construir abans.
- Les xarxes bridge s'han substituït per overlay.
- S'ha afegit la secció `deploy` per definir rèpliques, estratègies de reinici i actualització.
- L'escalat es realitza amb `docker service scale`.
- Swarm aplica balanceig intern entre rèpliques del servei.

### 6. Escalat de serveis

S'ha realitzat una prova d'escalat del servei d'aplicació:

```bash
docker service scale mystack_app=3
```

#### 6.1 Validació d'estat i reinici automàtic en Swarm

```yaml
deploy:
  restart_policy:
    condition: on-failure
```

#### 6.2 Limitació de recursos en Docker Swarm

| Paràmetre | Funció |
|-----------|--------|
| `limits` | límit màxim de recursos que pot consumir |
| `reservations` | recursos mínims reservats pel scheduler |

### 7. Validació funcional

S'ha comprovat: accés web correcte, funcionament amb múltiples rèpliques, comunicació entre serveis i persistència de dades.

### 8. Evidències

- **Evidència A** — Inicialització del clúster Docker Swarm (`docker swarm init`)
- **Evidència B** — Estat dels nodes (`docker node ls`)
- **Evidència D** — Fitxer `docker-stack.yml`
- **Evidència E** — Desplegament del stack (`docker service ls`)
- **Evidència F** — Validació web en entorn Swarm
- **Evidència G** — Escalat del servei
- **Evidència H** — Logs del servei desplegat
- **Evidència I** — Incorporació de nodes al clúster

### 9. Resultat de la fase

Aquesta fase ha permès transformar un entorn local basat en Docker Compose en una arquitectura orquestrada amb Swarm, introduint serveis declaratius, escalabilitat i gestió distribuïda bàsica.

---

## Fase 3 — Seguretat a Docker Swarm

### 1. Objectiu de la fase

L'objectiu d'aquesta fase és reforçar la seguretat del clúster Docker Swarm desplegat a la fase anterior, aplicant bones pràctiques relacionades amb:

- Protecció de la comunicació interna del clúster
- Gestió segura de credencials
- Reducció de la superfície d'atac
- Aïllament de serveis
- Controls d'accés i autenticació

### 2. Tècniques de seguretat a Docker Swarm

#### 2.1 Seguretat del clúster

- Comunicació interna xifrada mitjançant TLS automàtic
- Autenticació de nodes amb certificats digitals
- Tokens de unió per controlar l'entrada de nous nodes
- Separació de rols entre manager i worker
- Possibilitat de rotació de certificats

#### 2.2 Seguretat de serveis

- Execució de serveis amb usuari no root
- Polítiques de reinici controlades
- Sistema de fitxers en mode `read_only` quan és possible
- Definició explícita de rèpliques

#### 2.3 Seguretat de xarxa

- Ús de xarxes overlay internes
- No exposició de serveis interns com la base de dades
- Publicació mínima dels ports necessaris
- Separació entre xarxa frontend i backend

#### 2.4 Gestió segura de credencials amb Docker Secrets

Docker Secrets permet:

- Emmagatzemar credencials de forma xifrada
- Limitar l'accés als serveis autoritzats
- Evitar exposició en variables d'entorn o configuracions visibles

### 3. Anàlisi de problemàtiques i solucions aplicades

| Problemàtica detectada | Impacte potencial | Solució aplicada |
|------------------------|-------------------|------------------|
| Password en text pla al stack | Compromís de la base de dades | Implementació de Docker Secrets |
| Execució de contenidors com root | Escalada de privilegis | Execució amb usuari no privilegiat |
| Base de dades accessible des de frontend | Accés no autoritzat | Xarxa backend interna |
| Ports oberts innecessaris | Major superfície d'atac | Exposició exclusiva de Nginx |
| Comunicació no xifrada entre nodes | Intercepció de tràfic | TLS automàtic de Swarm |

### 4. Aplicació de millores de seguretat al clúster

#### 4.1 Implementació de Docker Secrets

S'han creat secrets per gestionar les credencials de la base de dades. Els secrets només són accessibles pels serveis que els declaren explícitament.

- **Evidència B** — Creació del secret per les credencials de la base de dades
- **Evidència C** — Adaptació del stack per utilitzar Docker Secrets
- **Evidència D** — Redeploy del stack amb credencials protegides

#### 4.2 Restricció de privilegis

```yaml
security_opt:
  - no-new-privileges:true
```

**Evidència E** — Execució del servei amb usuari no privilegiat

#### 4.3 Sistema de fitxers read-only

El servei Nginx s'ha configurat amb `read_only: true` i `tmpfs` per als directoris temporals.

**Evidència F** — Configuració read-only del servei Nginx

#### 4.4 Segmentació de xarxa

- Xarxa `frontend` per a l'accés web
- Xarxa `backend` com a xarxa interna
- Base de dades no exposada externament

**Evidència G** — Exposició mínima de ports al clúster

#### 4.5 Validació del xifrat TLS

Docker Swarm utilitza TLS per defecte en la comunicació interna entre nodes, garantint autenticació de nodes, xifrat del tràfic intern i integritat de les comunicacions.

**Evidència A** — Clúster Swarm actiu amb comunicació segura TLS

### 5. Resultat de la fase

Després de l'aplicació de les millores de seguretat:

- La superfície d'atac del clúster s'ha reduït
- Les credencials ja no es troben en text pla
- Els serveis interns no estan exposats
- Els contenidors tenen privilegis limitats
- La comunicació entre nodes està xifrada

En entorns productius reals seria recomanable complementar aquesta protecció amb firewall extern, reverse proxy amb HTTPS i monitorització activa de logs.

---

## Fase 4 — Orquestració amb Kubernetes

### 1. Objectiu de la fase

L'objectiu d'aquesta fase és migrar el desplegament orquestrat amb Docker Swarm a una arquitectura basada en Kubernetes, utilitzant els seus mecanismes natius de gestió de contenidors, escalabilitat i serveis.

La implementació s'ha realitzat amb **Minikube** en entorn local.

### 2. Principis de Kubernetes

Kubernetes és una plataforma d'orquestració de contenidors que treballa sota el model declaratiu d'estat desitjat.

#### 2.1 Arquitectura bàsica

**Control Plane:**

- **API Server**: punt d'entrada del clúster
- **etcd**: base de dades distribuïda amb l'estat del clúster
- **Scheduler**: assigna Pods als nodes
- **Controller Manager**: manté l'estat desitjat del sistema

**Worker Nodes:**

- **kubelet**: gestiona els contenidors del node
- **kube-proxy**: gestiona la xarxa
- **Container Runtime**: executa els contenidors

#### 2.2 Conceptes bàsics

- **Pod**: unitat mínima desplegable
- **Deployment**: defineix rèpliques i actualitzacions
- **Service**: exposa Pods a la xarxa
- **ConfigMap**: configuració no sensible
- **Secret**: gestió segura de credencials
- **Namespace**: aïllament lògic

```bash
kubectl apply -f fitxer.yaml
```

### 3. Diferències entre Kubernetes i Docker Swarm

#### 3.1 Comparació arquitectònica

| Característica | Docker Swarm | Kubernetes |
|----------------|--------------|------------|
| Arquitectura | Integrada a Docker | Plataforma independent |
| Fitxers | `docker-stack.yml` | YAML separats |
| Escalat | `docker service scale` | `replicas` en Deployment |
| Xarxa | Overlay | CNI |
| Secrets | Docker Secrets | Kubernetes Secrets |
| Complexitat | Baixa | Alta |
| Popularitat | Mitjana | Molt alta |

#### 3.2 Diferències clau

- Kubernetes utilitza objectes declaratius separats
- Té autorecuperació més avançada
- Permet rolling updates automàtiques
- Disposa d'un ecosistema molt més ampli
- Té una adopció professional superior
- A Minikube s'ha necessitat carregar la imatge manualment amb `minikube image load`

### 4. Creació i gestió de Pods i Services

#### 4.1 Preparació de l'entorn

```bash
minikube start
kubectl get nodes
```

**Evidència A** — Clúster Kubernetes actiu

#### 4.2 Arquitectura adoptada

- `app-deployment` → PHP-FPM (port 9000)
- `nginx-deployment` → servidor web (port 80)
- `db-deployment` → MariaDB

#### 4.3 Deployment de l'aplicació (PHP-FPM)

```bash
kubectl apply -f app-deployment.yaml
kubectl get pods
```

**Evidència B** — Deployment de l'aplicació creat

#### 4.4 Service intern de l'aplicació

L'aplicació no s'exposa directament. S'ha creat un Service intern tipus `ClusterIP` que permet que Nginx accedeixi a `app-service:9000`.

**Evidència C** — Service intern de l'aplicació

#### 4.5 Deployment de Nginx

Nginx actua com a frontend i reenvia les peticions PHP cap a `fastcgi_pass app-service:9000`. La seva configuració s'ha gestionat amb un ConfigMap.

**Evidència D** — ConfigMap de Nginx

#### 4.6 Service extern de Nginx

```yaml
kind: Service
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

**Evidència E** — Service Nginx exposat

#### 4.7 Escalat

```bash
kubectl scale deployment app-deployment --replicas=3
kubectl get pods
```

**Evidència F** — Escalat de Pods

#### 4.8 Gestió i diagnòstic amb kubectl

```bash
kubectl get pods -o wide
kubectl describe pod 
kubectl logs 
```

S'ha validat el mecanisme d'autorecuperació eliminant manualment un Pod i comprovant que el Deployment crea automàticament una nova rèplica.

#### 4.9 Probes de salut en Kubernetes

**Exemple per a l'aplicació:**

```yaml
livenessProbe:
  tcpSocket:
    port: 9000
  initialDelaySeconds: 10
  periodSeconds: 10

readinessProbe:
  tcpSocket:
    port: 9000
  initialDelaySeconds: 5
  periodSeconds: 5
```

**Exemple per a Nginx:**

```yaml
livenessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 10
  periodSeconds: 10
```

#### 4.10 Gestió de recursos en Kubernetes

| Paràmetre | Funció |
|-----------|--------|
| `requests` | recursos mínims reservats pel scheduler |
| `limits` | màxim de recursos que pot consumir |

### 5. Base de dades i Secrets

#### 5.1 Deployment de MariaDB

```bash
kubectl apply -f db-deployment.yaml
```

**Evidència G** — Base de dades desplegada

#### 5.2 Implementació de Secrets

```bash
kubectl create secret generic db-secret \
  --from-literal=MARIADB_ROOT_PASSWORD=root_password
```

**Evidència H** — Secret creat

### 6. Validació funcional

Amb Minikube en Linux i driver Docker, la validació inicial s'ha realitzat amb:

```bash
kubectl port-forward svc/nginx-service 8081:80
```

Accés via navegador: `http://127.0.0.1:8081`

**Evidència I** — Validació funcional final

#### 6.1 Accés extern mitjançant Ingress

Per acostar el projecte a un escenari més real, s'ha implementat accés mitjançant Ingress amb el domini `microservices.local`.

##### 6.1.1 Activació del controlador Ingress

```bash
minikube addons enable ingress
```

**Evidència J** — Controlador Ingress actiu

##### 6.1.2 Configuració del recurs Ingress

S'ha creat un fitxer `ingress.yaml` que defineix domini d'accés (`microservices.local`), ruta (`/`) i servei backend (`nginx-service`, port 80).

##### 6.1.3 Resolució DNS local

```
127.0.0.1 microservices.local
```

##### 6.1.4 Ús de Minikube Tunnel

```bash
minikube tunnel
```

##### 6.1.5 Validació de l'accés amb Ingress

Accés final: `http://microservices.local`

La cadena completa funciona correctament: **Ingress → Service → Pod**

**Evidència K** — Accés a l'aplicació mitjançant Ingress

### 7. Incidències i resolució

**Problema 1 — ImagePullBackOff**

Causa: la imatge no estava disponible dins Minikube.

```bash
minikube image load microservices-app:1.0
```

**Problema 2 — Error amb hostPath**

Causa: ús d'una ruta no accessible dins Minikube. Solució: substitució per ConfigMap.

**Problema 3 — NodePort no accessible**

Causa: limitacions del driver Docker de Minikube en Linux. Solució: ús de `kubectl port-forward`.

### 8. Resultat de la fase

Després de la migració, el projecte funciona correctament en Kubernetes amb Pods creats adequadament, escalat funcional, Nginx i PHP-FPM separats, configuració declarativa i credencials gestionades amb Secrets.

**Comparació pràctica entre Swarm i Kubernetes:**

- Docker Swarm és més ràpid d'implementar.
- Kubernetes requereix més configuració inicial.
- Kubernetes ofereix millor separació de responsabilitats.
- La gestió declarativa és més granular.
- El model Service + Deployment aporta més control.

A nivell professional, Kubernetes és l'opció més robusta i escalable, especialment en entorns multi-node i cloud-native.

---

## Estructura del repositori

```
microservices/
├── compose/
│   ├── .env.example
│   ├── .gitignore
│   ├── docker-compose.yml
│   ├── docker-stack.yml
│   ├── app/
│   │   ├── Dockerfile
│   │   └── src/
│   │       └── index.php
│   └── nginx/
│       ├── nginx.conf
│       └── conf.d/
│           └── default.conf
└── k8s/
    ├── app-deployment.yaml
    ├── app-service.yaml
    ├── db-deployment.yaml
    ├── ingress.yaml
    ├── nginx-configmap.yaml
    ├── nginx-deployment.yaml
    ├── nginx-service.yaml
    └── web-configmap.yaml
```

---

## Tecnologies utilitzades

- Docker
- Docker Compose
- Docker Swarm
- Kubernetes
- Minikube
- kubectl
- Nginx
- PHP-FPM
- MariaDB
- Git i GitHub

---

## Conclusions finals

Aquest projecte ha permès desenvolupar una arquitectura de microserveis a través de diferents nivells de maduresa tecnològica.

En una primera fase, Docker Compose ha estat útil per construir i validar ràpidament un entorn local declaratiu. Posteriorment, Docker Swarm ha aportat conceptes d'orquestració, escalabilitat i serveis distribuïts, juntament amb millores específiques de seguretat. Finalment, Kubernetes ha permès migrar el projecte a una plataforma més avançada i propera als estàndards professionals actuals.

A nivell tècnic, el projecte ha servit per consolidar coneixements sobre:

- contenidors i desplegament multi-servei
- segmentació de xarxa
- persistència de dades
- gestió segura de credencials
- alta disponibilitat bàsica
- escalat
- probes de salut
- serveis, deployments i ingressos en Kubernetes

La comparació entre Docker Swarm i Kubernetes ha permès entendre les diferències entre una solució més simple i integrada, i una altra més completa, modular i escalable. En conjunt, el projecte reprodueix de manera pràctica una evolució realista des d'un entorn de desenvolupament local fins a una arquitectura cloud-native més robusta.

---

## Autor

ASIX2 — Administració de Sistemes Informàtics en Xarxa  
Projecte desenvolupat dins del mòdul Projecte Intermodular (M0379)
