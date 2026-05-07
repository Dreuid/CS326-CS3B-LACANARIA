# Software Security Checklist

**Project:** GWA Calculator & Academic Tracker

## Implemented Security Measures
* **[x] Input Validation (2 Places):** Added bounds checking in `calculator.py` to ensure course units remain between 0-10 and grades strictly fall within the 1.0 - 5.0 scale, preventing injection of malicious float values.
* **[x] Basic Authentication:** Implemented a token-based authentication wrapper (`authenticate()`) that must pass before the calculation logic executes.
* **[x] Protected Sensitive Values:** Removed hardcoded API keys from the source code. The system now securely fetches the `GWA_API_KEY` using Python's `os.getenv()` method.
* **[x] Dependency Audit:** Ran a vulnerability scan on all Python packages used in the environment.
