import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer API',
}

data = {
    name = "test",
    region = "blr1",
    size="s-1vcpu-1gb",
    image="ubuntu-16-04-x64",
    #"ssh_keys":None,
    #"backups":False,
    #"ipv6":True,
    #"user_data":None,
    #"private_networking":None,
    #"volumes": None,
        }

response = requests.post('https://api.digitalocean.com/v2/droplets', headers=headers, data=data)

print(response)
