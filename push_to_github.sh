#!/bin/bash

# Set your repo and token
REPO_URL="https://github.com/Aerodinamika911/brand-workspace-ci.git"
TOKEN="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"

# Unzip workspace
unzip full_ci_cd_workspace_bundle.zip -d full_ci_cd_workspace
cd full_ci_cd_workspace

# Initialize and push
git init
git checkout -b main
git config user.name "GPT Auto Deploy"
git config user.email "gpt-deploy@automation.local"
git remote add origin https://$TOKEN@github.com/Aerodinamika911/brand-workspace-ci.git
git add .
git commit -m "Initial auto-deploy of CI/CD workspace"
git push -u origin main
