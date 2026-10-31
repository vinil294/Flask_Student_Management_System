# CI/CD Setup Guide

## Continuous Integration

GitHub Actions runs on every push and pull request targeting `main`.

Workflow: `.github/workflows/ci.yml`

- Python versions: 3.10, 3.11, 3.12
- Dependency installation: `pip install -r requirements.txt`
- Automated tests: `python -m pytest -v`
- Deployment job depends on the complete test matrix.

## Continuous Deployment with Render

1. Sign in to Render and create a **Web Service**.
2. Connect the GitHub repository `vinil294/Flask_Student_Management_System`.
3. Select branch `main`.
4. Build command: `pip install -r requirements.txt`.
5. Start command: `gunicorn app:app`.
6. Create a Deploy Hook in the Render service settings.
7. In GitHub, navigate to **Settings → Secrets and variables → Actions**.
8. Add repository secret:
   - Name: `RENDER_DEPLOY_HOOK`
   - Value: the Render Deploy Hook URL.
9. Push a new commit to `main`. GitHub Actions will run tests first and call the Render hook only when tests pass.

If the secret is absent, the workflow reports that deployment was skipped; a successful GitHub Actions job alone does not mean the app was deployed.

## Local verification

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Current validation

The latest verified `Flask CI/CD` run passed the test matrix on Python 3.10, 3.11, and 3.12. The Render deployment step completed without an error but was skipped because `RENDER_DEPLOY_HOOK` had not yet been configured.
