from flaskr import create_app

app = create_app()

#Démarre le serveur Flask sur toutes les interfaces (0.0.0.0) sur le port 5000
# Permet l'accès depuis d'autres conteneurs Docker via le réseau interne
# S'assure que la configuration est chargée avant toute connexion à MySQL
if __name__ == '__main__':
    with app.app_context():
        from flaskr.db import db
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

