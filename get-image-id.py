import digitalocean as do
import json

auth_key="API Key"
manager=do.Manager(token=auth_key)

image_id=manager.get_all_images()
print(image_id).json()
