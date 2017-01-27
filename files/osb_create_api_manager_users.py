connect(admin_username,admin_password,'t3://'+admin_server_listen_address+':'+admin_server_listen_port)

atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

edit()
startEdit(-1,-1,'false')

users = { 
			'apiadmin':'API Admins',
			'apiconsumer':'API Consumers',
			'apicurator':'API Curators',
			'apideveloper':'API Developers',
			'deployer':'Deployers',
			'monitor':'Monitors'
		}

for group in users.values():
	if not atnr.groupExists(group):
		atnr.createGroup(group,group)
		print "Created group %s" % (group)

for user in users:
	if not atnr.userExists(user):
		atnr.createUser(user,"password1",user)
		print "Created user %s" % (user)
	print "Adding user %s to group %s" % (user,users[user])
	atnr.addMemberToGroup(users[user],user)


for monitor in ['API Curators','API Developers','Deployers']:
	atnr.addMemberToGroup('Monitors',monitor)

activate()

try:
	grantAppRole('Service_Bus_Console','APICurator','weblogic.security.principal.WLSGroupImpl','API Curators')
except:
	pass

try:
	grantAppRole('Service_Bus_Console','Developer','weblogic.security.principal.WLSGroupImpl','API Developers')
except:
	pass

try:
	grantAppRole('Service_Bus_Console','Deployer','weblogic.security.principal.WLSGroupImpl','Deployers')
except:
	pass

try:
	grantAppRole('API_Manager','APIApplicationAdministrator','weblogic.security.principal.WLSGroupImpl','API Admins')
except:
	pass

try:
	grantAppRole('API_Manager','APIConsumer','weblogic.security.principal.WLSGroupImpl','API Consumers')
except:
	pass

disconnect()
exit()
