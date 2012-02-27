import pyloopia, client
loopia = pyloopia.Loopia()
for account in loopia.conf():
	loopia.login(account['username'], account['password'])
	loopia.logged_in()
	for domain in loopia.domains():
		for domain2 in account['domains']:
			if domain2['name'] == domain['name']:
				loopia.update_dns(domain, domain2['type'], client.external_ip())
