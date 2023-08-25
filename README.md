# Automated Unit Testing Demo

[![Unit Tests](https://github.com/VirtualBrainLab/automated-unit-testing-demo/actions/workflows/test.yml/badge.svg)](https://github.com/VirtualBrainLab/automated-unit-testing-demo/actions/workflows/test.yml)

Demo repo for automated unit testing in Python. Use this as a reference for how to perform unit tests in Python and have
GitHub Actions run them.

## Install and run the demo code

1. Clone this repo: `git clone https://github.com/VirtualBrainLab/automated-unit-testing-demo.git`
2. (Optional) create a virtual environment: `python -m venv venv`
3. Install the package: `pip install -e .`
4. Run the demo script: `demo`
5. Run the unit tests: `python -m unittest discover -s tests`

## Work through writing tests

This repo has branches labeled `0-...` through `5-...` which highlight steps in the process of writing code and unit
tests. They can be visited (in no particular order) with `git checkout` or `git switch` to experiment wth writing tests
and see the code at different states. On the `main` branch you can see the finished product including GitHub Actions
workflow and branch protection.

| Branch           | Description                                                                  | Activity                                          |
|------------------|------------------------------------------------------------------------------|---------------------------------------------------|
| `0-start`        | Demo class code with no unit tests.                                          | Write tests for `DemoClass` from scratch.         |
| `1-weak-tests`   | Basic unit test. Demonstrates the `TestCase` class structure.                | Improve the tests given.                          |
| `2-code-change`  | `DemoClass`'s code got changed! Does the unit tests catch the bugs (if any)? | Write tests to catch the bugs introduced.         |
| `3-better-tests` | Improved unit tests to expose the bugs.                                      | Fix the bugs introduced in `DemoClass`            |
| `4-fixed-code`   | Fixed the bugs introduced earlier.                                           | Think of inputs that can trigger uncaught errors. |
| `5-error-tests`  | Added tests that check for bad inputs.                                       | Write a GitHub Action workflow from scratch.      |