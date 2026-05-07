# System Architecture

**Project:** GWA Calculator & Academic Tracker

## 1. High-Level Architecture
The system follows a standard client-server model, separating the user interface from the calculation logic and data storage.

## 2. Component Breakdown
* **Frontend (Client):** Developed using React Native. Responsible for rendering the UI, capturing user input (courses, units, grades), and displaying the calculated GWA.
* **Backend (Server/Logic):** Developed in Python. Contains the core algorithm optimized for O(N) time complexity to process grade weights and handle edge cases (e.g., zero-division errors).
* **Database:** A relational SQL database designed to store user profiles, course histories, and authentication credentials securely.

## 3. Data Flow
1. User inputs grades via the React Native UI.
2. Data is formatted as a JSON payload and sent to the Python backend via API.
3. The backend validates the payload, runs the GWA algorithm, and logs the transaction.
4. Results are returned to the client and saved to the SQL database for persistence.
