lol-commits-jive
================

This script should be set-up to run once-a-day via a cron job or however you'd like.  It will choose a random LOL commit image from the current day and upload it to a Jive document/discussion/whatever as a comment.  LOL!

This small python application is designed to be post a random lol commit to a jive community.  It uses the Mac launchd system to execute the python script every 15 minutes.  These values are all configurable.

To get started, run the following commands in order (this may not be necessary in your dev set-up.  Just make sure pip and requests are installed and working)

1.  brew install python
2.  pip install requests
3.  sudo rm /usr/bin/python
3.  sudo ln -s /usr/local/bin/python /usr/bin/python

After that, clone the git project.  Place the cloned project somewhere where it can live indefinitely.  Navigate to that directory using the terminal and execute the following commands.

1.  nano com.sevensummits.lolcommits.plist.  
	
	Find PATH_TO_SCRIPT in the file and replace it with the full path to the python script.

2.  sudo mv ./com.sevensummits.lolcommits.plist /Library/LaunchDaemons/com.sevensummits.lolcommits.plist 

3.  sudo chown root /Library/LaunchDaemons/com.sevensummits.lolcommits.plist

4.  sudo launchctl load /Library/LaunchDaemons/com.sevensummits.lolcommits.plist