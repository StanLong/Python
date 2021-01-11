name = '刘伯温'
dynasty = '明朝人'
said = '年轻人，想要做成大事，就要学会等待'

s1 = '%s是%s, 他说过：%s'%(name, dynasty, said)
print(s1)

s2 = '{}是{}, 他说过：{}'.format(name, dynasty, said)
print(s2)

s3 = '{name}是{dynasty}, 他说过：{said}'.format(name=name, dynasty=dynasty, said=said)
print(s3)

s4 = '{0}是{1}, 他说过：{2}'.format(name, dynasty, said)
print(s4)