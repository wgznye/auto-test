
import shutil
import os



class CleanCache:
    @staticmethod
    def clean_dir(*args):
        for ar in args:
            print(ar)
            for f in os.listdir(ar):
                filepath = os.path.join(ar, f)
                if os.path.isfile(filepath):
                    os.remove(filepath)
            #  模板文件都是json格式的
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)


