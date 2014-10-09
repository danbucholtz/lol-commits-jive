import base64
import datetime
import json
import os.path, time
import sys
import random
import requests

walk_dir = ".lolcommits"

jive_username = "JIVE_USERNAME"
jive_password = "JIVE_PASSWORD_PLAINTEXT"

jive_base_url = "FULL_JIVE_URL_INCLUDE_HTTP"

# use the rest API to get the content ID.  NOTE:  Not the object ID - make sure you are using the ContentID
jive_thread_content_id = "72687"

file_list = []

for root, subdirs, files in os.walk(walk_dir):

	# no idea what this actually does - but it seems important
    list_file_path = os.path.join(root, 'my-directory-list.txt')

    with open(list_file_path, 'wb') as list_file:
        
        for filename in files:

        	if ".jpg" in filename:

        		file_path = os.path.join(root, filename)

        		file_list.append(file_path);

# we may have a selected file now... if we do, go ahead and process it

num_files = len(file_list);

if num_files > 0:

	index = random.randint(0, num_files - 1)

	random_file = file_list[index]

	print("Using the following file: " + random_file)
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
	
	# delete the image so it is not re-used
	os.remove(random_file)
else:
	print("Could not find image to use.  Get coding!") 