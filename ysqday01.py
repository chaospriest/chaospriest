# import sys
# def myprint(s = ''):
#     sys.stdout.write(s)
#     sys.stdout.flush()
#     data = sys.stdin.readline()
#     return data.strip('\n')


from select import select
from socket import *
# s1 = socket()
# s1.bind(('0.0.0.0',8888))
# s1.listen(3)
#
# s2 = socket(AF_INET,SOCK_DGRAM)
# s2.bind(('0.0.0.0',8889))
#
# f = open('test.log','r+')
#
# print('监控IO')
# rs,ws,xs = select([s1],[],[],3)

# from select import select
# from socket import *
#
# s1 = socket()
# s1.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s1.bind(('0.0.0.0',8888))
# s1.listen(3)
#
# rlist = [s1]
# wlist = []
# xlist = []
#
# while True:
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r is s1:
#             c,addr = r.accept()
#             print("来自%s的连接"%addr)
#             rlist.append(c)
#         else:
#             data = r.recv(1024).decode()
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#                 continue
#             print(data)
#             #r.send(b'ok')
#             wlist.append(r)
#
#     for w in ws:
#         w.send(b'ok')
#         wlist.remove(w)

s1 = socket()
s1.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s1.bind(('0.0.0.0',8888))
s1.listen(3)

from select import *
# p = poll()
#
# map = {s1.fileno():s1}
# p.register(s1,POLLIN)
#
# while True:
#     events = p.poll()
#     for fd,event in events:
#         if fd == s1.fileno():
#             c,addr = map[fd].accept()
#             print('connect from',addr)
#             p.register(c,POLLIN)
#             map[c.fileno()] = c
#         elif event & POLLIN:
#             data = map[fd].recv(1024).decode()
#             if not data:
#                 p.unregister(fd)
#                 map[fd].close()
#                 del map[fd]
#                 continue
#             print(data)
#             map[fd].send('ok')
#


# p = epoll()
#
# map = {s1.fileno(): s1}
# p.register(s1, EPOLLIN)
#
# while True:
#     events = p.poll()
#     for fd, event in events:
#         if fd == s1.fileno():
#             c, addr = map[fd].accept()
#             print('connect from', addr)
#             p.register(c, EPOLLIN)
#             map[c.fileno()] = c
#         elif event & EPOLLIN:
#             data = map[fd].recv(1024).decode()
#             if not data:
#                 p.unregister(fd)
#                 map[fd].close()
#                 del map[fd]
#                 continue
#             print(data)
#             map[fd].send('ok')
# from sys import *
# f = open('test.log','a')
# i1 = stdin
# rlist = [s1,i1]
# wlist = []
# xlist = []
# 
# while True:
#     while True:
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r is s1:
#             c,addr = r.accept()
#             print("来自%s的连接"%addr)
#             rlist.append(c)
#         elif r is i1:
#             f.write(r.readline())
#         else:
#             data = r.recv(1024).decode()
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#                 continue
#             print(data)
#             #r.send(b'ok')
#             wlist.append(r)

import re
pattern = r'(ab)cd(?P<name>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefgh')
print(obj.lastgroup)
print(obj.lastindex)
print(obj)