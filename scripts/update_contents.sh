python scripts/clean.py
if [ -n "$(git status --porcelain)" ]; then
  git add .
  git commit -m "Updated notes"
  git push &> /dev/null
fi
