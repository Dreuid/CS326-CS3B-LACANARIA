# Key Performance Indicators (KPIs)

**Project:** GWA Calculator & Academic Tracker
**Documentation Lead:** Lorenz Lacanaria

## Defined KPIs (5)
To ensure our application is performant, reliable, and user-friendly, we track the following metrics:

1. **Calculation Execution Time (Backend Performance):** The time it takes for the backend to process the math logic once grades are submitted. Target: `< 5ms`.
2. **System Error Rate (Reliability):** The percentage of calculations that result in a zero-division warning or unhandled exception. Target: `0%`.
3. **Test Pass Rate (Quality Assurance):** The percentage of core calculation logic covered by passing automated unit tests. Target: `100%`.
4. **Memory Usage per Transaction (Resource Efficiency):** The amount of RAM consumed during a single `calculate_gwa` execution. Target: Minimal footprint.
5. **User Input Time (Usability):** The average time it takes for a student to manually input a standard 5-course semester into the UI. Target: `< 30 seconds`.
