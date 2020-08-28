from servicenow import ServiceNow
from servicenow import Connection

# Connect using default api method (JSON)
#conn = Connection.Auth(username='a0g06a8', password='TheAb@wmlab@123', instance='walmartglobal')

# For Dublin+ instances, connect using JSONv2
# http://wiki.servicenow.com/index.php?title=Dublin_Release_Notes
conn = Connection.Auth(username='a0g06a8', password='TheAb@wmlab@123', instance='walmartglobal', api='JSONv2')

# For SOAP connection
#
#from servicenow.drivers import SOAP
#conn = SOAP.Auth(username='a0g06a8', password='TheAb@wmlab@123', instance='walmartglobal')
#
# SOAP support more than 250 results, example
# Get the changes updated on the last 30 minutes, Display values instead of sys_ids and change response limit to 10k
# http://wiki.servicenow.com/index.php?title=Direct_Web_Services#Extended_Query_Parameters
#
# chg.last_updated(minutes=30, params={'displayvalue': 'true'}, extended={'__limit': 10000}):

inc = ServiceNow.Incident(conn)
srv = ServiceNow.Server(conn)
grp = ServiceNow.Group(conn)
chg = ServiceNow.Change(conn)
tkt = ServiceNow.Ticket(conn)

# Custom table
#custom = ServiceNow.Base(conn)
#custom.__table__ = "custom_table.do"

#machine = srv.fetch_one({'name': 'machine0001'})
#print machine

#inc = inc.fetch_one({'number': 'INC14685317'})
#print(inc)

group = grp.fetch_one({'name': 'GDO-GG'})
print group

#changes = chg.fetch_all({'cmdb_ci': machine['sys_id'], 'review_status': 3})
#print changes

# Fetch changes updated on the last 60 minutes
#changes = chg.last_updated(minutes=60)
#print changes

# list only sys_ids
#changes = chg.list({'cmdb_ci': machine['sys_id'], 'review_status': 3})
#print changes

#ticket = tkt.fetch_one({'number': 'TICKET0185412'})
#print ticket

# Creating a new ticket based on another one
#del ticket["number"]
#new_ticket = tkt.create(ticket)
#print ticket