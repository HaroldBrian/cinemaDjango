# Projet Cinema

Ce projet est une API Django REST permettant de gérer des auteurs et des films, avec documentation interactive via Swagger.

## Instructions de lancement

1. **Cloner le dépôt et installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

2. **Installer les dépendances spécifiques à la documentation**

   ```bash
   pip install drf-yasg[swagger-ui]
   ```

3. **Appliquer les migrations**

   ```bash
   python manage.py migrate
   ```

4. **Lancer le serveur**

   ```bash
   python manage.py runserver
   ```

5. **Accéder à l’API et à la documentation**
   - API : [http://localhost:8000/api/](http://localhost:8000/api/)
   - Swagger : [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
   - Redoc : [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
   - Authentification token : [http://localhost:8000/api-token-auth/](http://localhost:8000/api-token-auth/)

## Endpoints disponibles

| Méthode | Endpoint           | Description                         |
| ------- | ------------------ | ----------------------------------- |
| GET     | /api/authors/      | Liste des auteurs                   |
| POST    | /api/authors/      | Créer un auteur                     |
| GET     | /api/authors/{id}/ | Détail d’un auteur                  |
| PUT     | /api/authors/{id}/ | Modifier un auteur                  |
| DELETE  | /api/authors/{id}/ | Supprimer un auteur                 |
| GET     | /api/movies/       | Liste des films                     |
| POST    | /api/movies/       | Créer un film                       |
| GET     | /api/movies/{id}/  | Détail d’un film                    |
| PUT     | /api/movies/{id}/  | Modifier un film                    |
| DELETE  | /api/movies/{id}/  | Supprimer un film                   |
| POST    | /api-token-auth/   | Obtenir un token d’authentification |

**Remarque :**  
La documentation complète et interactive des endpoints est disponible sur `/swagger/` et `/redoc/`.
