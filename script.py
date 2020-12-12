import urllib.request
import json

previous_images_filename = 'previous_images.json'
new_images_filename = 'new_images.json'

request = urllib.request.urlopen("https://hub.docker.com/v2/repositories/library/?page=1&page_size=100")
new_data = json.load(request)
with open(previous_images_filename) as previous_images_file:
    previous_images = json.load(previous_images_file)
    new_names = [image['name'] for image in new_data['results']]
    old_names = [image['name'] for image in previous_images['results']]
    for new_name in new_names:
        if new_name not in old_names:
            print(new_name)

with open(new_images_filename, "w") as new_images_file:
    json.dump(new_data, new_images_file)
