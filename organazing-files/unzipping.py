 
import tarfile, shutil, os

for i in range(10):
    shutil.move('./tarfile.tar', './tarfile.tar.tmp')
    out = tarfile.open('tarfile.tar.tmp', 'r')
    for j in out.getnames():
        print(j)
        f = out.extract(j, './')
    out.close()
    os.unlink('./tarfile.tar.tmp')

 
