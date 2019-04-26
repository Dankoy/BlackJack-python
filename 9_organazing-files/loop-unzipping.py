 
import tarfile, shutil, os

out1 = tarfile.open('tarfile.tar', 'r')
name = out1.getnames()
name = ''.join(name)
print(name)
while name == './tarfile.tar':
    name = ''
    shutil.move('./tarfile.tar', './tarfile.tar.tmp')
    out = tarfile.open('tarfile.tar.tmp', 'r')
    for j in out.getnames():
        print(j)
        f = out.extract(j, './')
    out.close()
    os.unlink('./tarfile.tar.tmp')
    
    out1 = tarfile.open('tarfile.tar', 'r')
    name = out1.getnames()
    name = ''.join(name)
    

 
