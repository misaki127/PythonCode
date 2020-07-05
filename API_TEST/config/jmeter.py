import io
import requests
import time
import threading

# url = 'http://192.168.2.215:10098/hydra-digital-village/api/v1/market-activity/addActivityRecord'
url = 'https://yms.lyj.zj.gov.cn/webapi/api/DataAnalysis/TypicalModeList'

# json1 = {'householdId':'748a832416694c4e8a5b166ac4c82480',
# 	'openId':'1'}
json1 ={'param.pageNum':1,'param.pageSize':10}
headers = {'Content-Type':'text/json;charset=utf-8','Accept':'application/json','Connection':'keep-alive'}   #,'Authorization':''}

a =int(input("输入执行次数："))

def login(headers):
	url1 = 'https://yms.lyj.zj.gov.cn/webapi/api/User/UserLogin'
	json_login = {"ticket":"adbecbe9aca94e7e957ed1921c291f30","userLoginId":"18271568890"}
	try:
		r = requests.post(url1,json=json_login,headers=headers)
		token = r.json()['data']['token']
		return token
	except:
		print('error!')


list_t = []
def getmarket(url,headers,i):
	# json1['openId'] = i
	r = requests.get(url,headers=headers)
	#t = r.elapsed.total_seconds()
	# f.write(str(r.text))
	# f.write('\n')
	#f.write(str(t))
	# f.write('\n')
	# localtime = time.asctime(time.localtime(time.time()))
	# f.write(str(localtime))
	#
	# f.write('\n')
	print(i)


	return r

def ces(a,f):
	f.write(str(a))
	f.write('\n')
	localtime = time.asctime(time.localtime(time.time()))
	f.write(str(localtime))
	f.write('\n')


# #多次访问接口
# for i in range(1,51):
# 	json1['openId'] = i
# 	t = getmarket(url,i,headers,f,json1)
# 	list_t.append(t)
#

#并发访问

thread = []
headers['Authorization'] = str(login(headers))
print(headers)
# target =getmarket(url,headers,i)
# print(target.text)


for i in range(1,a):

	exec('t{0} = threading.Thread(target=getmarket,args=(url,headers,i))'.format(i))
	exec('thread.append(t{0})'.format(i))

	# exec('t{0} = threading.Thread(target=ces,args=(i,f))'.format(i))
	# exec('thread.append(t{0})'.format(i))

for t in thread:
	t.setDaemon(True)
	t.start()

for i in thread:
	i.join()
print("finall")



# f.close()
