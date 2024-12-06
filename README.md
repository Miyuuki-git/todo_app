## Todo App - Documentation

## Structure du Projet
  Frontend: Application Angular
  Backend: API Flask
  Base de données: MySQL 5.7
  Reverse Proxy: Nginx
  Outils de monitoring: Prometheus, Grafana, Elasticsearch, Fluentd, cAdvisor

## Points Importants
*Le backend Flask utilise SQLAlchemy pour la connexion à MySQL
*Nginx agit comme reverse proxy sur le port 8086
*La configuration de la base de données est définie dans config.py
*Modification du db.py pour assurer la connection à la base de données
*Les services communiquent via un réseau Docker interne
*Ajout de mysqlclient dans le dockerfile du backend (énoncé dans requirements.txt)
*Creation de nginx.conf, fluent.conf et prometheus.yml pour leur configuration respective
*Fluentd collecte les logs et les envoie vers Elasticsearch
*Prometheus collecte les métriques des conteneurs via cAdvisor (que j'ai ajouté au docker-compose)
*Grafana visualise les données d'Elasticsearch et Prometheus

## Problèmes Résolus / Difficultées
*Installation de mysqlclient pour la connexion Python-MySQL
*Configuration du healthcheck MySQL
*Configuration du reverse proxy Nginx
*Configuration de la connexion à la base de données
*Configuration de Fluentd avec Elasticsearch
*Configuration du healthcheck Elasticsearch pour répondre à la difficulté de Fluentd pour se connecter
*Configuration de Prometheus avec cAdvisor
*Mise en place des dashboards Grafana

## Problèmes non Résolus
*Prometheus n'arrive pas à communiuer avec cAdvisor pour collecter les données

## Accès aux Services
*Application Web: http://localhost:8086
*PHPMyAdmin: http://localhost:8085
*Grafana: http://localhost:3000
*Prometheus: http://localhost:9090
*Elasticsearch: http://localhost:9200

## Notes
Certains services de monitoring (Fluentd) nécessitent des configurations supplémentaires
Les dashboards Grafana doivent être configurés manuellement
