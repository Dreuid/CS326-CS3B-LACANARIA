# Deployment Plan

**Project:** GWA Calculator & Academic Tracker
**DevOps Lead:** James Henry Emorricha
**Target Platform:** Replit / Streamlit Cloud (PaaS)

## 1. Deployment Strategy
For Sprint 1, we are using a **Rolling Deployment** strategy via a Platform as a Service (PaaS). We will deploy our core Python backend logic to an online container so it can be accessed remotely. Future sprints will integrate the React Native frontend via Vercel.

## 2. Deployment Steps
1. Ensure all tests pass on the `dev` branch.
2. Merge `dev` into `main` and tag the release (e.g., v0.5).
3. Pull the `main` branch into the production environment.
4. Run the application startup script.

## 3. Rollback Steps
If the deployed system crashes or exhibits critical bugs:
1. Immediately log into the hosting dashboard.
2. Revert the repository pointer back to the previous stable release tag (e.g., `git checkout v0.4`).
3. Restart the server environment.
4. Log the incident in the `docs/defect-log.md` for investigation.
