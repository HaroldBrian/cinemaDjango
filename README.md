# Projet Cinema

_Version_ : 1.0
_Last update_ : 19 Mai 2025
_By_ : FOTSEU CHEDJOU HAROLD BRIAN

---

# Cinema Project

This project is a Django REST API for managing authors and movies, with interactive documentation via Swagger.

## Launch Instructions

1. **Clone the repository and install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Install documentation-specific dependencies**

   ```bash
   pip install drf-yasg[swagger-ui]
   ```

3. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start the server**

   ```bash
   python manage.py runserver
   ```

5. **Access the API and documentation**
   - API: [http://localhost:8000/api/](http://localhost:8000/api/)
   - Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
   - Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
   - Token authentication: [http://localhost:8000/api-token-auth/](http://localhost:8000/api-token-auth/)

## Available Endpoints

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| GET    | /api/authors/      | List all authors               |
| POST   | /api/authors/      | Create an author               |
| GET    | /api/authors/{id}/ | Get details of an author       |
| PUT    | /api/authors/{id}/ | Update an author               |
| DELETE | /api/authors/{id}/ | Delete an author               |
| GET    | /api/movies/       | List all movies                |
| POST   | /api/movies/       | Create a movie                 |
| GET    | /api/movies/{id}/  | Get details of a movie         |
| PUT    | /api/movies/{id}/  | Update a movie                 |
| DELETE | /api/movies/{id}/  | Delete a movie                 |
| POST   | /api-token-auth/   | Obtain an authentication token |

**Note:**  
The complete and interactive documentation of the endpoints is available at `/swagger/` and `/redoc/`.

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

5. **Accéder à l’api/v1 et à la documentation**
   - api/v1 : [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
   - Swagger : [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
   - Redoc : [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
   - Authentification token : [http://localhost:8000/token/](http://localhost:8000/token/)

## Endpoints disponibles

| Méthode | Endpoint              | Description                         |
| ------- | --------------------- | ----------------------------------- |
| GET     | /api/v1/authors/      | Liste des auteurs                   |
| POST    | /api/v1/authors/      | Créer un auteur                     |
| GET     | /api/v1/authors/{id}/ | Détail d’un auteur                  |
| PUT     | /api/v1/authors/{id}/ | Modifier un auteur                  |
| DELETE  | /api/v1/authors/{id}/ | Supprimer un auteur                 |
| GET     | /api/v1/movies/       | Liste des films                     |
| POST    | /api/v1/movies/       | Créer un film                       |
| GET     | /api/v1/movies/{id}/  | Détail d’un film                    |
| PUT     | /api/v1/movies/{id}/  | Modifier un film                    |
| DELETE  | /api/v1/movies/{id}/  | Supprimer un film                   |
| POST    | /token/               | Obtenir un token d’authentification |

**Remarque :**  
La documentation complète et interactive des endpoints est disponible sur `/swagger/` et `/redoc/`.
