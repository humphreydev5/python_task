# To create a simple collection 
users = {'Hans' : 'active', 'Emmanuel' : 'inactive', 'Jacob' : 'active'}

#Strategy: Iterate over a copy
for user, status in users.copy().items():
  if status == 'inactive':
    del users[user]

#Strategy: Create a new collection 
active_users = {}
for user, status in users.items():
  if status == 'active':
    active_users[user] = status

