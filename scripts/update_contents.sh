# redirect output to syslog
# https://www.urbanautomaton.com/blog/2014/09/09/redirecting-bash-script-output-to-syslog/
exec 1> >(logger -s -t $(basename $0)) 2>&1

(cd /home/flock/roam-notes && git fetch && git reset --hard origin/master --quiet)
/home/flock/venvs/worldview/bin/python /home/flock/notes-garden/scripts/clean.py
if [ -n "$(git status --porcelain)" ]; then
  git add .
  git commit -m "Updated notes"
  git push &> /dev/null
fi
