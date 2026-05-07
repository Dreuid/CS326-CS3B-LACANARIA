# CI/CD Pipeline Architecture

**Project:** GWA Calculator & Academic Tracker
**DevOps Lead:** James Henry Emorricha

This document outlines our automated Continuous Integration and Continuous Deployment (CI/CD) pipeline.

## Pipeline Flow Diagram
The following diagram illustrates the steps our automation server takes when new code is introduced to the production branch.

```mermaid
graph TD
    A[Code Merged to 'main' branch] -->|Triggers Action| B(Initialize Environment)
    B --> C{Run Python Smoke Tests}
    C -- Tests Fail --> D[Halt Pipeline & Alert Team]
    C -- Tests Pass --> E[Trigger Deployment Webhook]
    E --> F[Deploy to Production Server]
    F --> G((System Live))
