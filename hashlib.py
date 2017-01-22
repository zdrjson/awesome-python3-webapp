#import hashlib
#
#md5 = hashlib.md5()
#md5.update('how to use md5 in python hashlib?').encode('utf-8')
#print(md5.hexdigest())
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

def calc_md5(password):
	pass
	
db = {
     'michael': 'e10adc3949ba59abbe56e057f20f883e',
     'bob': '878ef96e86145580c38c87f0410ad153',
     'alice': '99b1c2188db85afee403b1536010c2c9'	
}

def login(user, password):
	pass
	
def calc_md5(password):
	return get_md5(password + 'the_Salt')
	
db = {}
def register(username, password):
	db[username] = get_md5(password + username + 'the-Salt')

