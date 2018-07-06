import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 4ef1f11c5aea95ff064c4f3daddbfac17b0d118233613666ae64e5519f430edc',
}

data = '{"name":"wp-test,"region":"blr1","size":"s-1vcpu-1gb","image":"30943092","ssh_keys":null,"backups":false,"ipv6":true,"user_data":null,"private_networking":null,"volumes": null,"tags":["web"]}'

response = requests.post('https://api.digitalocean.com/v2/droplets', headers=headers, data=data)
