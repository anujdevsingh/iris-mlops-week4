# Week 4 - MLOps CI/CD Assignment

## Objective
Implement Continuous Integration (CI) for an Iris classification pipeline using GitHub Actions, DVC, and Pytest.

## Steps
1. Train the Iris model.
2. Track data and model with DVC.
3. Add Pytest unit tests for validation and evaluation.
4. Configure GitHub Actions to:
   - pull DVC data
   - run tests
   - post report using CML.

## Commands
```bash
dvc init
dvc remote add -d gdrive gdrive://<your-folder-id>
dvc add data/iris.csv
dvc add model/model.pkl
git add .
git commit -m "Week 4 CI/CD setup"
dvc push
