# Docker Swarm i Kubernetes: Desenvolupament i Desplegament de Microserveis en Entorns Cloud

## Informació del projecte

Aquest repositori recull el desenvolupament complet del projecte **Docker Swarm i Kubernetes: Desenvolupament i Desplegament de Microserveis en Entorns Cloud**, realitzat dins del marc del cicle formatiu **ASIX2**.

El projecte mostra l’evolució d’una arquitectura multicapa des d’un entorn local amb **Docker Compose**, passant per una orquestració amb **Docker Swarm**, fins a una migració final a **Kubernetes** amb **Minikube**.

## Repositori GitHub

Segons els requisits del projecte, s’ha utilitzat un compte de GitHub per centralitzar tota la documentació tècnica, configuracions, captures, demostracions i fitxers del projecte.

Cal que el repositori tingui com a col·laborador obligatori el compte del professorat:

`projectesasixsapalomera`

La URL del repositori s’ha d’indicar també a la portada, annex o apartat corresponent de la memòria final.

**URL del repositori:**

`https://github.com/IevgenSoloviov/docker-swarm-kubernetes-microservices`

---

# Índex

1. [Fase 1 — Configuracions i desplegament amb Docker Compose](#fase-1--configuracions-i-desplegament-amb-docker-compose)  
2. [Fase 2 — Orquestració i desplegament amb Docker Swarm](#fase-2--orquestració-i-desplegament-amb-docker-swarm)  
3. [Fase 3 — Seguretat a Docker Swarm](#fase-3--seguretat-a-docker-swarm)  
4. [Fase 4 — Orquestració amb Kubernetes](#fase-4--orquestració-amb-kubernetes)  
5. [Estructura del repositori](#estructura-del-repositori)  
6. [Tecnologies utilitzades](#tecnologies-utilitzades)  
7. [Conclusions finals](#conclusions-finals)

---

# Fase 1 — Configuracions i desplegament amb Docker Compose

## 1. Objectiu de la fase

L’objectiu d’aquesta fase és crear un entorn multi-contenidor amb Docker Compose que simuli una arquitectura multicapa tipus LAMP, formada per capa web, capa d’aplicació i base de dades, de forma repetible i preparada per a futures migracions a Docker Swarm i Kubernetes.

## 2. Introducció a Docker Compose

Docker Compose permet definir i desplegar múltiples serveis Docker mitjançant un únic fitxer `docker-compose.yml`. Aquesta eina facilita la gestió de dependències, xarxes i volums, i garanteix que l’entorn es pugui recrear de forma consistent en qualsevol sistema.

### Avantatges de Docker Compose

- Permet definir múltiples serveis en un únic fitxer declaratiu.
- Facilita la gestió de dependències entre serveis.
- Simplifica la recreació d’entorns.
- Permet versionar la infraestructura com a codi.
- Redueix errors humans en la configuració manual.

### Inconvenients

- No està pensat per a entorns distribuïts.
- No gestiona alta disponibilitat.
- No distribueix càrrega entre múltiples nodes.
- No implementa estratègies avançades d’actualització.

## 3. Disseny de l’entorn multi-nivell

S’ha implementat una arquitectura de tres capes formada per:

- **Nginx** com a servidor web i reverse proxy.
- **PHP-FPM** com a capa d’aplicació.
- **MariaDB** com a capa de dades i persistència.

Per millorar la seguretat i l’organització del desplegament:

- S’han creat dues xarxes: `frontend` i `backend`.
- La xarxa `backend` s’ha configurat com a interna (`internal: true`) per evitar exposar la base de dades a l’exterior.
- S’ha utilitzat un volum `db_data` per garantir la persistència de dades.

## 4. Configuració realitzada

### Fitxers principals del projecte

- `.env`: paràmetres configurables com ports i credencials.
- `docker-compose.yml`: definició dels serveis, xarxes i volums.
- `app/Dockerfile`: imatge personalitzada per al servei PHP-FPM.
- `nginx/conf.d/default.conf`: configuració del servidor web.
- `app/src/index.php`: pàgina de prova basada en `phpinfo()`.

## 5. Desplegament

### Comandes executades

```bash
docker compose up -d --build
docker ps
