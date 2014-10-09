import base64
import datetime
import json
import os.path, time
import sys
import random
import requests

walk_dir = ".lolcommits"

jive_username = "dan.bucholtz@7summitsagency.com"
jive_password = "asdf1234"

jive_base_url = "https://7summitsagency-hive.jiveon.com/"

jive_thread_content_id = "72687"

list_of_files = []

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

        		#if filedate.year == today.year and filedate.month == today.month and filedate.day == today.day:

        		list_of_files.append(file_path)

# we now have a list of .jpg files that were modified today.  Choose a random one.

num_files = len(list_of_files)

if num_files > 0:

	index = random.randint(0, num_files - 1)

	random_file = list_of_files[index]

	# post the image to jive /images api

	images_endpoint = jive_base_url + "/api/core/v3/images"

	files = {'file': ('lol.jpg', open(random_file, 'rb'), 'image/jpg', {'Expires': '0'})}
	r = requests.post(images_endpoint, files=files, auth=(jive_username, jive_password))
	response_data = r.json();

	image_url = response_data["ref"]

	#grab the url of the jive image, and now post it as a comment to the pre-defined thread

	payload = {'type': 'comment', "content": {"type": "text/html", "text":"<img src=" + image_url + "></img>"}, "parent":jive_base_url + "/api/core/v3/contents/" + jive_thread_content_id  }
	headers = {'content-type': 'application/json'}

	response = requests.post(jive_base_url + "/api/core/v3/comments", data=json.dumps(payload), headers=headers, auth=(jive_username, jive_password))
	response_data = r.json();
	print(response_data)
