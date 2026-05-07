# DevOps Practices & CI/CD

**Project:** GWA Calculator & Academic Tracker

## 1. Version Control & Collaboration
* **Git Workflow:** We utilize a feature-branch workflow. All changes are made on isolated branches and merged into `main` via Pull Requests.
* **Conflict Resolution:** Merges require manual review by the DevOps lead to resolve any code conflicts before deployment.

## 2. Continuous Integration (CI)
* **Automated Testing:** We enforce Test-Driven Development (TDD). Our Python test suite (5 core unit tests) must pass 100% before any code is deployed.
* **Quality Assurance:** Code is reviewed for technical debt, performance metrics, and type-hinting accuracy.

## 3. Continuous Deployment (CD)
* **Deployment Strategy:** We use a Rolling Deployment strategy via Cloud PaaS for the backend logic, ensuring zero downtime during updates.
* **Monitoring & Rollback:** The system includes automated logging. In the event of a critical failure, we revert the repository to the previous stable Git tag (e.g., `v0.8`).
