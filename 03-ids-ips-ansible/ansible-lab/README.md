<div align="center">

<br/>

```
 █████╗ ███╗   ██╗███████╗██╗██████╗ ██╗     ███████╗
██╔══██╗████╗  ██║██╔════╝██║██╔══██╗██║     ██╔════╝
███████║██╔██╗ ██║███████╗██║██████╔╝██║     █████╗  
██╔══██║██║╚██╗██║╚════██║██║██╔══██╗██║     ██╔══╝  
██║  ██║██║ ╚████║███████║██║██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═════╝ ╚══════╝╚══════╝

        I n f r a e s t r u c t u r a   d ’ A u t o m a t i t z a c i ó
                    A n s i b l e   →   S S H   →   D o c k e r
```

### Infraestructura d’Automatització (Ansible)

*Node de control · Nodes gestionats · Playbooks · SSH · Docker · Nginx*

<br/>

![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Lab%20Containers-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SSH](https://img.shields.io/badge/SSH-Remote%20Management-333333?style=for-the-badge)
![YAML](https://img.shields.io/badge/YAML-Playbooks-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Web%20Server-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Git](https://img.shields.io/badge/Git-Code%20Deployment-F05032?style=for-the-badge&logo=git&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-Managed%20Nodes-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-System%20Administration-FCC624?style=for-the-badge&logo=linux&logoColor=black)

<br/>

</div>

La infraestructura d'automatització es basa en **Ansible**, que permet gestionar i configurar diversos servidors de forma centralitzada.

Ansible s'executa dins un **contenidor Docker que actua com a node de control**, mentre que els servidors gestionats també s'executen com a contenidors Debian.

Aquesta configuració permet crear un laboratori fàcilment reproduïble i modular.

---

# Node de Control

El node de control Ansible s'executa dins un contenidor Docker basat en **Debian 12**.

Aquest node és responsable d'automatitzar la configuració dels servidors utilitzant **playbooks d’Ansible**.

Les seves funcions principals són:

- executar playbooks
- gestionar inventaris de hosts
- establir connexions SSH amb els nodes gestionats
- garantir que els sistemes mantinguin l'estat desitjat

L'ús de Docker permet:

- desplegament ràpid
- reproduïbilitat del laboratori
- separació del sistema host
- flexibilitat per modificar la infraestructura

---

# Nodes Gestionats

Els nodes gestionats representen servidors dins la infraestructura.

Cada node s'executa com un **contenidor Docker basat en Debian 12** i disposa d'un servidor **SSH** que permet la seva gestió des d'Ansible.

Els nodes gestionats permeten demostrar:

- instal·lació de paquets
- configuració automatitzada de serveis
- desplegament d'aplicacions web
- gestió d'usuaris i permisos
- aplicació de configuracions de sistema

---

# Inventari

Els nodes gestionats es defineixen dins del fitxer:

```
inventory/hosts
```

Exemple d'inventari utilitzat en el laboratori:

```
[clients]
managed-node-01 ansible_host=managed-node-01 ansible_user=ansible ansible_password=ansible ansible_become_password=ansible
managed-node-02 ansible_host=managed-node-02 ansible_user=ansible ansible_password=ansible ansible_become_password=ansible
```

Aquest inventari permet que Ansible gestioni múltiples nodes de forma centralitzada.

---

# Execució del Playbook

La configuració dels servidors es realitza executant el següent comandament des del node de control:

```
ansible-playbook -i /inventory/hosts /ansible/setup_web.yml
```

Aquest playbook aplica la configuració sobre tots els nodes definits al grup **clients**.

---

# Tasques Automatitzades

El playbook implementa diverses tasques que permeten demostrar diferents aspectes d'automatització.

---

## Aprovisionament

El sistema realitza automàticament les següents tasques d'aprovisionament:

- instal·lació de paquets base (`git`, `vim`, `curl`, `cron`)
- creació del grup `devops`
- creació de l'usuari `deploy`
- creació del directori `/opt/webapp`

Exemple de tasca Ansible:

```
- name: Crear grup devops
  group:
    name: devops
    state: present
```

---

## Desplegament d’Aplicacions

El laboratori desplega una aplicació web utilitzant **Nginx**.

Tasques realitzades:

- instal·lació del servidor web Nginx
- activació del servei
- desplegament d'una pàgina web personalitzada
- clonació d'un repositori Git amb contingut d'exemple

Exemple de tasca:

```
- name: Instal·lar nginx
  apt:
    name: nginx
    state: present
```

També es realitza la clonació d'un repositori Git dins del directori de treball.

```
- name: Clonar aplicació web des de Git
  git:
    repo: https://github.com/docker/awesome-compose.git
    dest: /opt/webapp/repo
```

---

## Gestió de Configuració

Ansible permet garantir que els sistemes mantinguin una configuració consistent.

Entre les tasques realitzades es troben:

- assegurar que el servei nginx està actiu
- desplegar fitxers de configuració
- mantenir l'estat dels serveis
- crear tasques programades de manteniment

Exemple de configuració de servei:

```
- name: Assegurar que nginx està actiu
  service:
    name: nginx
    state: started
    enabled: yes
```

---

## Seguretat Bàsica

El playbook també aplica configuracions bàsiques de seguretat.

Entre aquestes mesures es troben:

- desactivar el login SSH del root
- crear fitxers amb permisos segurs
- limitar l'accés administratiu

Exemple de configuració:

```
- name: Desactivar login root per SSH
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^PermitRootLogin'
    line: 'PermitRootLogin no'
```
---

# Execució Ràpida del Laboratori

Per iniciar la infraestructura Docker del laboratori:

```bash
docker compose up -d
```

Accedir al contenidor del node de control d’Ansible:

```bash
sudo docker exec -it ansible-control bash
```

Executar el playbook d'automatització:

```bash
ansible-playbook -i /inventory/hosts /ansible/setup_web.yml
```

Després de l'execució del playbook:

- els nodes gestionats disposaran d’un **servidor web Nginx instal·lat i actiu**
- es desplegarà una **pàgina web personalitzada**
- es configuraran **usuaris, directoris i serveis**
- s’aplicaran **configuracions bàsiques de seguretat**

Això demostra com Ansible pot automatitzar la configuració d’una infraestructura completa.

---

# Conclusions

Aquest projecte m’ha permès introduir-me de manera pràctica en el món de l’automatització de sistemes utilitzant Ansible. Més enllà de la teoria, he pogut veure com realment es poden gestionar diversos servidors de forma centralitzada, simulant una infraestructura real mitjançant contenidors Docker.

Al principi, entendre com funcionaven els playbooks, l’inventari o la connexió entre nodes no ha estat del tot senzill, però a mesura que avançava he anat guanyant confiança i entenent millor el funcionament de l’automatització. Especialment, m’ha resultat interessant veure com una mateixa configuració es pot aplicar a múltiples màquines de manera ràpida i consistent.

Durant el projecte he pogut automatitzar tasques que habitualment es farien manualment, com la instal·lació de paquets, la configuració de serveis web o la creació d’usuaris. Això m’ha fet adonar de la importància de l’automatització en entorns reals, ja que redueix errors humans i estalvia molt temps en la gestió de sistemes.

També considero molt interessant la integració amb el projecte d’IDS, ja que m’ha permès entendre com es poden combinar diferents tecnologies per construir un entorn més complet, no només centrat en la configuració sinó també en la seguretat.

En general, aquest projecte m’ha ajudat a entendre millor com funcionen les infraestructures modernes i m’ha donat una base sòlida per continuar aprenent sobre automatització i DevOps en el futur.
