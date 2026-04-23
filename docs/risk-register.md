# Risk Register

**Scoring Guide:**
* **Likelihood (1-5):** 1 = Very Unlikely, 5 = Highly Likely
* **Impact (1-5):** 1 = Minimal, 5 = Critical
* **Risk Score:** Likelihood × Impact (Higher score = higher priority)

| ID | Risk Description | Likelihood | Impact | Score | Mitigation Plan | Risk Owner |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **R01** | **Scope Creep:** Adding too many features beyond the GWA calculation delays Sprint 1. | 4 | 4 | **16** | Strictly enforce the backlog. Push non-essential features to Sprint 2. | Lorenz |
| **R02** | **Merge Conflicts:** Multiple members editing the same files cause deployment blocks. | 5 | 3 | **15** | Require members to pull the latest `dev` branch before starting work and communicate before merges. | James |
| **R03** | **Database Data Loss:** Accidental deletion or corruption of the SQL grade database. | 2 | 5 | **10** | Implement regular database backups and use soft deletes for records. | James |
| **R04** | **Uncaught Bugs:** Math logic for the GWA calculation is inaccurate. | 2 | 4 | **8** | Implement Test-Driven Development (TDD) and require passing unit tests before PR approvals. | Lorenz |
| **R05** | **Team Member Absence:** Illness or schedule conflicts stall progress. | 3 | 3 | **9** | Ensure code is pushed daily so others can pick up the work. Keep docs updated. | Nash |
| **R06** | **UI Incompatibility:** React Native frontend breaks on different screen sizes. | 3 | 3 | **9** | Use flexbox for responsive design and test on multiple device emulators early. | Kyle |
| **R07** | **Environment Issues:** Python/React versions differ across members' machines causing "works on my machine" errors. | 4 | 2 | **8** | Standardize versions in a `requirements.txt` and `package.json` file. | James |
| **R08** | **Failed Authentication:** Security flaws in the login system expose student data. | 1 | 5 | **5** | Use established, tested authentication libraries instead of writing custom auth logic. | Lorenz |
