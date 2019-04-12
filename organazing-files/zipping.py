 
import tarfile, shutil

for i in range(10):
    shutil.copy('./tarfile.tar', './tarfile.tar.tmp')
    out = tarfile.open('tarfile.tar.tmp', 'w')
    out.add('./tarfile.tar')
    out.close()
    shutil.move('./tarfile.tar.tmp', './tarfile.tar')
