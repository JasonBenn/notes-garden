python scripts/clean.py
if ! git diff-index --quiet HEAD --; then
  git add .
  git commit -m "Updated notes"
  git push
fi
