import digitalocean as do
import json

auth_key="4ef1f11c5aea95ff064c4f3daddbfac17b0d118233613666ae64e5519f430edc"
manager=do.Manager(token=auth_key)

image_id=manager.get_all_images()
print(image_id).json()