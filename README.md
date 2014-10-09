lol-commits-jive
================

This script should be set-up to run once-a-day via a cron job or however you'd like.  It will choose a random LOL commit image from the current day and upload it to a Jive document/discussion/whatever as a comment.  LOL!

Run the following commands in order (this may not be necessary in your dev set-up.  Just make sure pip and requests are installed and working)

1.  brew install python
2.  pip install requests
3.  sudo rm /usr/bin/python
3.  sudo ln -s /usr/local/bin/python /usr/bin/python

Place the python script somewhere on your computer.  Update the com.lolcommits.plist file to reflect the location of the script.

Then, execute the following commands

1.  sudo mv /Library/LaunchDaemons/com.sevensummits.lolcommits.plist ./com.sevensummits.lolcommits.plist
2.  sudo chown root com.sevensummits.lolcommits.plist