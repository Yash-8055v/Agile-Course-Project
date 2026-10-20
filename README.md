# DevOps Mini Project - CI/CD Pipeline for a Containerized Flask Application

Pipeline: **Developer -> GitHub -> GitHub Actions (lint + test) -> Docker build -> Docker Hub -> Render -> Live app**

## Run locally
```bash
pip install -r requirements.txt
pytest
python app.py                      # http://localhost:5000
```

## Run with Docker
```bash
docker compose up --build -d       # http://localhost:5000
curl http://localhost:5000/health
```

## One-time setup for the pipeline
1. **Docker Hub:** create an access token (Account Settings -> Security -> New Access Token).
2. **Render:** New -> Web Service -> "Existing image" -> `docker.io/<dockerhub-username>/devops-mini-project:latest`
   (free instance). Then open the service -> Settings -> copy the **Deploy Hook** URL.
3. **GitHub:** repo -> Settings -> Secrets and variables -> Actions -> add three secrets:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
   - `RENDER_DEPLOY_HOOK`
4. `git push origin main` - the pipeline builds, tests, pushes the image and redeploys on Render.

## API
| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Health check |
| GET | /api/tasks | List tasks |
| POST | /api/tasks | Add task `{"title": "..."}` |
| PUT | /api/tasks/<id> | Toggle done |
| DELETE | /api/tasks/<id> | Delete task |

## Made by
Yash 
Siddhesh
