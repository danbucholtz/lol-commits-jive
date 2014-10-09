lol-commits-jive
================

This small python application is designed to be post a random lol commit to a jive community.  It uses the Mac launchd system to execute the python script every 15 minutes.  These values are all configurable.

To get started, run the following commands in order (this may not be necessary in your dev set-up.  Just make sure pip and requests are installed and working)

1.  brew install python
2.  pip install requests
3.  sudo rm /usr/bin/python
3.  sudo ln -s /usr/local/bin/python /usr/bin/python

After that, clone the git project.  Place the cloned project somewhere where it can live indefinitely.  Navigate to that directory using the terminal and execute the following commands.

1.  nano com.sevensummits.lolcommits.plist.  
	
	Find PATH_TO_SCRIPT in the file and replace it with the full path to the python script.

2.  nano lolcommits.py.  Replace USER_DIRECTORY, JIVE_USERNAME, JIVE_PASSWORD_PLAINTEXT, and FULL_JIVE_URL_INCLUDE_HTTP with the proper values.

3.  sudo mv ./com.sevensummits.lolcommits.plist /Library/LaunchDaemons/com.sevensummits.lolcommits.plist 

4.  sudo chown root /Library/LaunchDaemons/com.sevensummits.lolcommits.plist

5.  sudo launchctl load /Library/LaunchDaemons/com.sevensummits.lolcommits.plist