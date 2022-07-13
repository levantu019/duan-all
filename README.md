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
    │   ├── Dockerfile  // Dockerfile frontend
    │   ├── nginx.conf
    │   ├── ...
    ├── .env
    ├── docker-compose.base.yml // docker-compose backend
    ├── docker-compose.prod.yml // docker-compose frontend
    ├── Dockerfile              // Dockerfile backend
    ├── README.md    
    └── requirements.txt        // python          

# Run project (use docker-compose)
    ```
    docker-compose -f docker-compose.base.yml -f docker-compose.prod.yml up -d
    ```
