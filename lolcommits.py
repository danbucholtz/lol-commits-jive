import base64
import datetime
import json
import os.path, time
import sys
import random
import requests

walk_dir = ".lolcommits"

jive_username = "jive-username"
jive_password = "jive-password-plaintext"

jive_base_url = "http://jive-url"

# use the rest API to get the content ID.  NOTE:  Not the object ID - make sure you are using the ContentID
jive_thread_content_id = "72687"

earliest_date = None
selected_file_path = None

for root, subdirs, files in os.walk(walk_dir):

	# no idea what this actually does - but it seems important
    list_file_path = os.path.join(root, 'my-directory-list.txt')

    with open(list_file_path, 'wb') as list_file:
        
        for filename in files:

        	if ".jpg" in filename:

        		file_path = os.path.join(root, filename)

        		filetime = time.ctime(os.path.getmtime(file_path))

        		filedate = datetime.datetime.strptime(filetime, "%a %b %d %H:%M:%S %Y")
        		today = datetime.datetime.now()

        		# make sure it's from today

        		if filedate.year == today.year and filedate.month == today.month and filedate.day == today.day:

        			# it is from today, so now check and make sure it's the earliest one...

        			if earliest_date is None or earliest_date < filedate:
        				earliest_date = filedate
        				selected_file_path = file_path

# we may have a selected file now... if we do, go ahead and process it

if selected_file_path is not None:

	print("Using the following file: " + selected_file_path)
	# post the image to jive /images api

	images_endpoint = jive_base_url + "/api/core/v3/images"

	files = {'file': ('lol.jpg', open(selected_file_path, 'rb'), 'image/jpg', {'Expires': '0'})}
	r = requests.post(images_endpoint, files=files, auth=(jive_username, jive_password))
	response_data = r.json();

	image_url = response_data["ref"]

	#grab the url of the jive image, and now post it as a comment to the pre-defined thread

	payload = {'type': 'comment', "content": {"type": "text/html", "text":"<img src=" + image_url + "></img>"}, "parent":jive_base_url + "/api/core/v3/contents/" + jive_thread_content_id  }
	headers = {'content-type': 'application/json'}

	response = requests.post(jive_base_url + "/api/core/v3/comments", data=json.dumps(payload), headers=headers, auth=(jive_username, jive_password))
	response_data = r.json();
	
	# delete the image so it is not re-used
	os.remove(selected_file_path)
else:
	print("Could not find image to use.  Get coding!") 