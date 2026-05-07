# Ethical Impact Assessment

**Project:** GWA Calculator & Academic Tracker

## 1. Identified Stakeholders
* **Primary:** University students using the app to track their academic standing.
* **Secondary:** Academic advisors and faculty who may receive exported grade reports from students.
* **Internal:** The development team responsible for maintaining the system.

## 2. Identified Ethical Risks
* **Psychological Stress:** Displaying a failing projected GWA could negatively impact a student's mental health.
    * *Mitigation:* The UI will use neutral language and avoid alarming color schemes (e.g., bright red) when displaying low grades. We will frame the "Target Grade Predictor" as an actionable planning tool rather than a definitive failure notice.
* **Algorithmic Bias:** The math logic assumes standard university grading systems. If a student transfers from a school with a different weight system, the app could miscalculate their standing.
    * *Mitigation:* We have clearly labeled the grading scale parameters in the UI (1.0 - 5.0) to set accurate user expectations.
