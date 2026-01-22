# API Automation Testing Project
![Python API Tests](https://github.com/oleg-pyshenkin/api-automation-practice/actions/workflows/python-tests.yml/badge.svg)

This project is a professional automation framework designed to validate REST API endpoints. It features **Test Isolation**, **Data-Driven Testing**, and **Contract Validation**.

This project contains automated tests for the JSONPlaceholder API.

## Key Features
- **Contract Testing:** Automated JSON Schema validation for all responses.
- **Negative Testing:** Robust error handling verification (404, etc.).
- **CI/CD Integration:** Automated test execution via GitHub Actions.
- **Detailed Reporting:** Full test execution history and screenshots via Allure.

## Tech Stack
- **Language:** Python 3.13
- **Framework:** Pytest
- **Reporting:** Allure
- **Library:** Requests, JSONSchema

## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `pytest --alluredir=allure-results`
3. See report: `allure serve allure-results`