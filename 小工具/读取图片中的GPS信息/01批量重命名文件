import os


class BatchRename():

    def rename(self):
        path = "D:/StanLong/Python/photo"
        filelist = os.listdir(path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.jpg'):
                new_name = item.replace(" 拷贝", "")
                src = os.path.join(os.path.abspath(path), item)
                dst = os.path.join(os.path.abspath(path), new_name)
                try:
                    os.rename(src, dst)
                    i += 1
                except:
                    continue
        print('total %d to rename & converted %d png' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
