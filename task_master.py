#task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManger继承的QueueManger:
class QueueManger(BaseManager):
     pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象:
QueueManger.register('get_task_queue', callable=lambda: task_queue)
QueueManger.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000，设置验证码‘abc':
manger = QueueManger(address=('', 5000), authkey=b'abc')
#启动Queue:
manger.start()
# 获得通过网络访问的Queue对象
task = manger.get_task_queue()
result = manger.get_result_queue()
# 放几个任务进去：
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)
# 从result队列读取结果：
print('Try get results...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)
# 关闭：
manger.shutdown()
print('master exit.')







		
		