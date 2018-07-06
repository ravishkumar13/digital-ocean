import digitalocean as do

auth_key="API Key"
manager=do.Manager(token=auth_key)

all_droplets=manager.get_all_droplets()
for droplets in all_droplets:
    droplets.destroy()

