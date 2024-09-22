# yijia_ids706_miniProj2

## Python Template

This project is designed to generate descriptive statistics and visualizations from datasets. It includes integrated CI/CD capabilities using GitHub Actions, which automatically generate and commit summary reports in Markdown format as part of the pipeline.

## CI/CD Badge
[![CI](https://github.com/nogibjj/yijia_ids706_miniProj2/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj2/actions/workflows/hello.yml)


## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.
- **`rdu-weather-history.csv`**: Contains weather data for the Durham region, used as the dataset for analysis.
- **`summary_report.md`**: A generated report with summary statistics (mean, median, standard deviation) and visualizations.

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj2.git
```

### 2. Open the Repository in Visual Studio Code

- Reopen in the container using the .devcontainer configuration.
- Rebuild the container if necessary, ensuring Docker is running on your computer.

### 3. Install dependencies
Run the following command to install all required dependencies:

```bash
make install
```

## Usage
- make install: Installs dependencies specified in requirements.txt.
- make format: Formats Python files using Black.
- make lint: Lints Python files using Pylint, ignoring specific patterns.
- make test: Runs tests using pytest and generates a coverage report.
- make clean: Removes pytest cache.
- make generate_report: Generates a profiling report in Markdown formats during CI/CD.

## CI/CD Setup
- Location: .github/workflows/
- Description: Contains GitHub Actions workflows for CI/CD, which automatically run setup, lint, and test actions on pushes to the GitHub repository.

## Summary Report Generation
The CI/CD pipeline automatically generates a Markdown report using Pandas. The report includes descriptive statistics (mean, median, standard deviation) and visualizations generated from the dataset. The report is then committed and pushed back to the repository, allowing for easy review and access.

