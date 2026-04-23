# Product Backlog

## Epic: Student GWA Calculator App

**1. User Authentication**
* **Priority:** High | **Story Points:** 5
* **Acceptance Criteria:** User can register with an email/password. System displays an error for invalid credentials. User stays logged in across sessions.

**2. Add a Course & Grade**
* **Priority:** High | **Story Points:** 3
* **Acceptance Criteria:** Form accepts text for course name and numbers for units/grades. Input is saved to the SQL database.

**3. Calculate Overall GWA**
* **Priority:** High | **Story Points:** 5
* **Acceptance Criteria:** The app multiplies grades by units, divides by total units, and displays the GWA accurately to two decimal places. 

**4. Edit Course Details**
* **Priority:** Medium | **Story Points:** 2
* **Acceptance Criteria:** Clicking a saved course opens an edit modal. Changes are reflected immediately in the database and the GWA recalculates.

**5. Delete a Course**
* **Priority:** Medium | **Story Points:** 2
* **Acceptance Criteria:** User is prompted with a confirmation before deletion. Once deleted, it is removed from the UI and GWA calculation.

**6. Sort by Semester**
* **Priority:** Medium | **Story Points:** 3
* **Acceptance Criteria:** UI includes a dropdown to filter by "1st Semester", "2nd Semester", or "All Time".

**7. Target Grade Predictor**
* **Priority:** Low | **Story Points:** 8
* **Acceptance Criteria:** Requires input for "Target GWA" and "Remaining Units". Outputs the required average grade needed. 

**8. Dark Mode Toggle**
* **Priority:** Low | **Story Points:** 2
* **Acceptance Criteria:** A toggle switch in settings changes the global React Native theme from light to dark. 

**9. Export GWA Report**
* **Priority:** Low | **Story Points:** 5
* **Acceptance Criteria:** Generates a formatted PDF containing the student's name, list of courses, units, grades, and final GWA. 

**10. Offline Mode**
* **Priority:** Low | **Story Points:** 8
* **Acceptance Criteria:** App caches the latest database fetch locally. Displays a "You are offline" banner when disconnected.