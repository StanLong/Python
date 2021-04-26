import queue

# 先进先出队列
# q = queue.Queue(maxsize=5)
# # 后进先出队列 --> 栈
# lq = queue.LifoQueue(maxsize=6)
# # 优先级队列
# pq = queue.PriorityQueue(maxsize=5)
#
# for i in range(5):
#     q.put(i)
#     lq.put(i)
#     pq.put(i)
#
# print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
# print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
# print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))
#
# print(q.get(), lq.get(), pq.get())
#
# print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
# print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
# print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))

# 双端队列
dq=queue.deque(['a','b'])
dq.append('c')
print(dq)
print(dq.pop())
print(dq)
print(dq.popleft())
print(dq)
dq.appendleft('d')
print(dq)
print(len(dq))
queue.deque(['a', 'b', 'c'])
queue.deque(['a', 'b'])
queue.deque(['b'])
queue.deque(['d', 'b'])
