lol-commits-jive
================

This script should be set-up to run once-a-day via a cron job or however you'd like.  It will choose a random LOL commit image from the current day and upload it to a Jive document/discussion/whatever as a comment.  LOL!

Run the following commands in order:

1.  brew install python
2.  pip install requests
3.  sudo rm /usr/bin/python
3.  sudo ln -s /usr/local/bin/python /usr/bin/python