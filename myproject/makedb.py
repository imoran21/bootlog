from home.models import Department, Vendor, Account, Location
import csv

class CsvFile(object):
	def __init__(self, name):
		self.name = name
		self.data = []
		self.columns = []
	def __str__(self):
		return self.name

	def empty(self):
		self.data = []

	def fill(self):
		self.data = [x for x in csv.DictReader(open(self.name, 'rU'))]
		self.columns = self.data[0].keys()


''' 
The Repo class is similar to the csv file object 
but lets you gather all csv files in a directory at once
the get() method just instantiates a CsvFile object. 
'''

class Repo(object):
	def __init__(self, pathdir = '.', fillall = False):
		if not fillall:
			self.items = [CsvFile(f).empty() for f in os.listdir(pathdir) if os.path.isfile(f) and f.lower().endswith('.csv')]
		else:
			self.items = [CsvFile(f) for f in os.listdir(pathdir) if os.path.isfile(f) and f.lower().endswith('.csv')]
	def fill_all(self):
		self.items = [x.fill for x in self.items]
	def get(self, filea):
		return CsvFile(str(filea))



def add_departments():
	dep = CsvFile('records/Departments.csv')
	dep.fill()
	for x in dep.data:
		d = Department(ns_id = x['Internal ID'], name = x['Name'])
		d.save()

def add_accounts():
	acc = CsvFile('records/Accounts.csv')
	acc.fill()
	for x in acc.data:
		if x['Inactive'] == 'No':
			if x['Number'] == "":
				a = Account(ns_id = x['Internal ID'], name = x['Account'], description = x['Description'])
				a.save()
			else:
				a = Account(ns_id = x['Internal ID'], number = x['Number'], name = x['Account'], description = x['Description'])
				a.save()

def add_vendors():
	vendors = CsvFile('records/Suppliers.csv')
	vendors.fill()
	for x in vendors.data:
		v = Vendor(ns_id = x['Internal ID'], name = x['Name'])
		v.save()


def add_locations():
	locations = CsvFile('records/Locations.csv')
	locations.fill()
	for x in locations.data:
		l = Location(ns_id=x['Internal ID'], name = x['Name'], country = x['Country'])
		l.save()

def fill_db():
	add_departments()
	add_locations()
	add_vendors()
	add_accounts()


