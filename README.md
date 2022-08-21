# Project WebGIS
- MTA
- Django + Vuejs + PostgresSQL + Nginx

# Directory Structure
    .
    ├── backend
    │   ├── backend // root (base url, settings, ...)
    │   ├── biengioidiagioi                         │
    │   ├── cosododac                               │
    │   ├── dancu                                   │
    │   ├── diahinh                                 │   
    │   ├── giaothong                               │   // apps
    │   ├── phubemat                                │
    │   ├── thuyvan                                 │
    │   ├── nendialy                                │
    │   ├── myauth                                  │
    │   ├── stattic
    │   ├── templates
    │   ├── media
    │   ├── .env
    │   ├── docker-compose.backend.yml 
    │   ├── Dockerfile              
    │   ├── README.md    
    │   ├── requirements.txt   
    │   └── manage.py
    ├── frontend
    │   ├── public
    │   └── src
    │       ├── api
    │       ├── assets
    │       ├── components
    │       ├── constants
    │       ├── factory 
    │       ├── mixins
    │       ├── plugins
    │       ├── router
    │       ├── store
    │       ├── style
    │       ├── utils
    │       └── views
    │   ├── Dockerfile  
    │   ├── nginx.conf
    │   ├── .env
        ├── docker-compose.prod.yml    
        ├── ...       

# Run project (use docker-compose)
- 
    ```
    docker-compose -f ./backend/docker-compose.backend.yml -f ./frontend/docker-compose.frontend.yml up -d
    ```