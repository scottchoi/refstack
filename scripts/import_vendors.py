import csv
from refstack.models import *

_file = 'members_sponsors_20131030.csv'
with open(_file, 'rb') as csvfile:
    parsed = csv.reader(csvfile, delimiter=',')
    for row in parsed:
        try:
            vendor = Vendor()
            vendor.vendor_name = row[1]
            vendor.contact_email = row[3]
            db.add(vendor)
            db.commit()
        except:
            print 'vendor skipped:'+row[1]
