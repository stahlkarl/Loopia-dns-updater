import cookielib, urllib, urllib2, cre, client, json, time
class Loopia:
	configuration_filename = "pyloopia.conf"

	def conf(self):
		conf_file = open(self.configuration_filename, 'r')
		accounts = []
		for account in conf_file.read().split("\n"):
			if account != "":
				accounts.append(json.loads(account))
		conf_file.close()
		return accounts

	def login(self, username, password):
		client.log("Logging in as %s" % username)
		cookiejar     = cookielib.CookieJar()
		loopia_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
		loopia_opener.add_headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10')]
		urllib2.install_opener(loopia_opener)
		login_query = urllib.urlencode({'username': username, 'password': password, 'action': 'submit', 'submit.x': '0', 'submit.y': '0', 'new': 0})
		urllib2.urlopen("https://www.loopia.com/login", login_query)
	
	def logged_in(self):
		client.log("Validating login")
		html = urllib2.urlopen("https://customerzone.loopia.se/").read()
		if '<div class="logged-in-user">' in html:
			client.log("Logged in as %s" % cre.between('<div class="logged-in-user">', '</div>', html))
			return True
		client.log("Not logged in")
		return False
	
	def domains(self):
		html    = urllib2.urlopen("https://customerzone.loopia.se/domains/properties/index/domain/").read()
		options = cre.all_between("<option", '</option>', html)
		domains = []
		for option in options:
			label = cre.between('label="', '"', option)
			name  = option.split(">")[-1]
			id    = cre.between('value="', '"', option)
			if name == label and "." in name:
				domains.append({'id': id, 'name': name})
		return domains
	
	def update_dns(self, domain, type, target):
		#Type can be either A or CNAME
		client.log("Updating DNS settings for %s. Pointing %s --> %s" % (domain['name'], domain['name'], target))
		html = urllib2.urlopen("https://customerzone.loopia.se/domains/properties/index/domain/%s" % domain['id']).read()
		hash = cre.between('<input type="hidden" name="hash" value="', '"', html)
		settings = urllib.urlencode({'type': type, 'target': target, 'hash': hash})
		urllib2.urlopen("https://customerzone.loopia.se/domains/properties/dns/domain/%s/subdomain/0/synchronize/1/context/json" % domain['id'], settings).read()
