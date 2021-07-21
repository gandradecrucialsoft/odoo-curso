from xmlrpc import client
url = 'https://gandradecrucialsoft-odoo-curso-mainv1-1-2916418.dev.odoo.com'
db = 'gandradecrucialsoft-odoo-curso-mainv1-1-2916418'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/common".format(url))
print(common.version())

uid = common.authenticate(db,username,password,{})
print(uid)


#models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
#model_access = models.execute_kw(db,uid,password,'sale.order','check_access_rights',['write'],{'raise_exception':False})
#print(model_access)