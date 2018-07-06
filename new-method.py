import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer API',
}

data = '{"name":"wp-test,"region":"blr1","size":"s-1vcpu-1gb","image":"30943092","ssh_keys":null,"backups":false,"ipv6":true,"user_data":null,"private_networking":null,"volumes": null,"tags":["web"]}'

response = requests.post('https://api.digitalocean.com/v2/droplets', headers=headers, data=data)
