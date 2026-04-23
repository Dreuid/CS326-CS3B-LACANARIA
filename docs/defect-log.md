# Defect Log

| Bug ID | Date Found | Found By | Description | Priority | Status | Fix Implemented |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-001** | Oct 26 | Lorenz | App crashes with a `ZeroDivisionError` when calculating GWA if a user inputs a course with 0 units. | High | **Closed** | Added an `if total_units == 0: return 0.0` check in `calculator.py` to handle the edge case safely. |
