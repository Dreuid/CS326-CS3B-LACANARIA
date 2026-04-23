# Quality Assurance & Test Plan

**Project:** GWA Calculator & Academic Tracker
**QA Lead:** Lorenz Lacanaria

## 1. Testing Strategy
Our testing approach will focus on ensuring the core logic of the application is mathematically accurate and stable before integrating it with the UI.

## 2. Test Types Defined
* **Unit Testing:** We will test individual Python functions in isolation, specifically the math algorithms that calculate the GWA, to ensure they handle standard inputs, edge cases (like 0 units), and rounding correctly.
* **Integration Testing:** Once the UI and Backend are connected, we will test the data flow to ensure that when a user adds a course in the React Native frontend, it successfully writes to the SQL database.

## 3. Tools Used
* **Backend Testing:** `pytest` (Python framework)
* **Frontend/UI Testing:** `Jest` (React Native framework)
