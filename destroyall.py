import digitalocean as do

auth_key="4ef1f11c5aea95ff064c4f3daddbfac17b0d118233613666ae64e5519f430edc"
manager=do.Manager(token=auth_key)

all_droplets=manager.get_all_droplets()
for droplets in all_droplets:
    droplets.destroy()

