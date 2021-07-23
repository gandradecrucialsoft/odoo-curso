from xmlrpc import client
url = 'https://gandradecrucialsoft-odoo-curso-mainv1-1-2933962.dev.odoo.com'
db = 'gandradecrucialsoft-odoo-curso-mainv1-1-2933962'
username = 'gandrade@crucialsoft.com.mx'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/common".format(url))
print(common.version())

uid = common.authenticate(db,username,password,{})
print(uid)


models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db,uid,password,'sale.order','check_access_rights',['write'],{'raise_exception':False})
print(model_access)

draft_quotes = models.execute_kw(db,uid,password,'sale.order','search',[[['state','=','draft']]])
print(draft_quotes)

if_confirmed = models.execute_kw(db,uid,password,'sale.order','action_confirm',[draft_quotes])
print(if_confirmed)


#session_fields = models.execute_kw(db,uid,password,'account.payment','fields_get',[],{'attributes':['string','type','required']})
#print(session_fields)

#vals = {
#    'journal_id' : 1,
#    'payment_method_id': 1,
#    'amount': 123,
#    'payment_type': 'inbound',
#    'partner_type': 'customer',
#    'currency_id':33,
#    'partner_id': 14,
#    'destination_account_id' : 3,
#    'ref': 'INV/2021/06/0010',
#    'is_reconciled':True,
#}
#payment = models.execute_kw(db,uid,password,'account.payment','create',[vals])
#print(payment);

#vals = {
#    'journal_id' : 8,
#    'partner_bank_id' : 9,
#    'payment_method_id': 1,
#    'amount': 987,
#    'payment_type': 'inbound',
#    'partner_type': 'customer',
#    'currency_id':33,
#    'partner_id': 14,
#    'destination_account_id' : 3,
#    'ref': 'INV/2021/06/0008'
#    ,'communication': 'INV/2021/06/0008',
#}
#payment = models.execute_kw(db,uid,password,'account.payment','action_create_payments',[vals])
#print(payment)

vals = {
    'session_id' : 1,
    'session_student_ids' : [2,5],
    'student_ids' : [2,5],
}
wizard_test= models.execute_kw(db,uid,password,'academy.sale.wizard','create_sale_orders',[vals])
print(wizard_test)