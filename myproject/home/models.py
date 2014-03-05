from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
	name = models.CharField(max_length=100, blank =False)
	ns_id = models.CharField(max_length=50, blank = False)
	address_line1 = models.CharField(max_length=50, blank=True)
	address_line2 = models.CharField(max_length=50, blank=True)
	address_line3 = models.CharField(max_length=50, blank=True)
	address_line4 = models.CharField(max_length=50, blank=True)
	tax_id = models.CharField(max_length=50, blank=True)
	email = models.CharField(max_length=50, blank=True)   
	USD = "USA"
	BP = "British pound"
	CND = "Canadian Dollar"
	EUR = "Euro"
	KRW = "KRW"
	NZD = "NZD"
	AUD = "AUD"
	SGD = "Singaport Dollar"
	HKD = "Hong Kong Dollar"

   	CURR_CHOICES = (
   		(USD, "USA"),
   		(BP, "British pound"),
   		(CND,"Canadian Dollar"),
   		(EUR, "EURO"),
   		(KRW, "KRW"),
   		(NZD, "NZD"),
   		(AUD, "AUD"),
   		(SGD, "SGD"),
   		(HKD, "HKD"),
   	)
   	currency = models.CharField(max_length =20,choices = CURR_CHOICES, default = USD)
   	balance = models.DecimalField(max_digits = 20, default = 0, decimal_places=2)

   	def __unicode__(self):
   		return self.name


class Account(models.Model):
	ns_id = models.CharField(max_length=50)
	number = models.IntegerField(blank = True)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100, blank=True)
	USD = "USA"
	BP = "British pound"
	CND = "Canadian Dollar"
	EUR = "Euro"
	KRW = "KRW"
	NZD = "NZD"
	AUD = "AUD"
	SGD = "Singaport Dollar"
	HKD = "Hong Kong Dollar"
	CURR_CHOICES = (

   		(USD, "USA"),
   		(BP, "British pound"),
   		(CND,"Canadian Dollar"),
   		(EUR, "EURO"),
   		(KRW, "KRW"),
   		(NZD, "NZD"),
   		(AUD, "AUD"),
   		(SGD, "SGD"),
   		(HKD, "HKD"),
   	)
   	currency = models.CharField(max_length =20,choices = CURR_CHOICES, default = USD)

  	def __unicode__(self):
  		return "{} {}".format(self.number, self.name)

class Department(models.Model):
	ns_id = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Approval(models.Model):
	id = models.AutoField(primary_key=True)
	approved = "Approved"
	assigned = "Assigned"
	unassigned = "Unassigned"
	denied = "Denied"

	STATUS_CHOICES = (

   		(approved, "Approved"),
   		(assigned, "Assigned"),
   		(unassigned,"Unassigned"),
   		(denied, "Denied"),
   	)
   	models.CharField(max_length =20,choices = STATUS_CHOICES, default = unassigned)

class ApprovalLine(models.Model):
	sent = "Sent"
	approved = "Approved"
	denied = "Denied"

	STATUS_CHOICES = (

   		(sent, "Sent"),
   		(approved, "Approved"),
   		(denied, "Denied"),
   	)
	approval_main = models.ForeignKey(Approval)
	approver = models.ForeignKey(User)
	line_status = models.CharField(max_length =25,choices = STATUS_CHOICES, default = sent)

	def __unicode__(self):
		return self.approver


class Location(models.Model):
	ns_id = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=15, blank = True)
	def __unicode__(self):
		return "{}".format(self.name)

class Bill(models.Model):
	vendor = models.ForeignKey(Vendor)
	inv_num  = models.IntegerField()
	DUR = "Due Upon Receipt"
	paid = "PAID"
	unpaid = "UNPAID"
	TERMS_CHOICES =(
		(DUR, "Due Upon Receipt"),
	)
	PAYMENT_CHOICES =(
		(paid, "PAID"),
		(unpaid, "UNPAID"),

	)
	terms = models.CharField(max_length =25,choices = TERMS_CHOICES, default = DUR)
	inv_date = models.DateField()
	due_date = models.DateField()
	gl_date = models.DateField()
	description =  models.CharField(max_length=100, blank=True)
	ammount = models.DecimalField(max_digits = 20, default = 0, decimal_places=2)
	approval_key = models.ForeignKey(Approval, blank=True, null=True)
	payment_status = models.CharField(max_length =25,choices = PAYMENT_CHOICES, default = unpaid)

	def __unicode__(self):
		return str(self.inv_num)

class BillLine(models.Model):
	bill_main = models.ForeignKey(Bill)
	account = models.ForeignKey(Account)
	ammount = models.DecimalField(max_digits = 20, decimal_places=2)
	department = models.ForeignKey(Department)
	description =  models.CharField(max_length=100, blank=True)
	location = models.ForeignKey(Location)








