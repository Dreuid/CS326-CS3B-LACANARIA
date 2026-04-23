# Technical Debt Register

**Project:** GWA Calculator & Academic Tracker
**Lead Developer:** Nash Andrew Bondoc

## Identified Technical Debts (5)
1. **Inefficient List Iteration:** The `calculate_gwa` function loops through the courses list twice (once for total units, once for weighted points), doubling the processing time ($O(2N)$ complexity).
2. **Missing Type Hinting:** The Python backend lacks type annotations, making it harder for developers to know what data structures are expected, which can lead to bugs.
3. **Hardcoded Database Strings:** Database connection credentials (if implemented) would currently be hardcoded instead of using secure environment variables (`.env`).
4. **No Frontend State Management:** The React Native UI (hypothetical) relies on prop-drilling instead of a centralized state manager like Redux or Context API.
5. **Lack of Input Sanitization:** The current backend logic assumes all grade/unit inputs are perfectly formatted floats and doesn't handle malicious string inputs.

## Selected Debt to Fix
We have selected **Debt #1 and #2** to fix for this sprint. We will refactor the `calculate_gwa` algorithm to process all math in a single pass ($O(N)$ complexity) and add strict Python type hinting for better maintainability.
