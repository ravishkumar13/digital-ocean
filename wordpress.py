import digitalocean as do
import time
import json

auth_key="API"
print("Enter the name of your site:")
site_name=input()
droplet = do.Droplet(token=auth_key,
                     name=site_name,#name of the site
                     region='blr1', # Bangalore
                     image='30943092', # wordpress image ID
                     size='s-1vcpu-1gb',  # 1vCPU, 1Gb Ram and 25GB Storage
                     backups=True) #autometic backups 

response=droplet.create()
#print(response)
print("Your server is getting created...")
time.sleep(60)

#final_response=json.loads(response.content.decode('utf-8'))
#print(final_response)

manager = do.Manager(token=auth_key)
my_droplets = manager.get_all_droplets()
print(my_droplets)
