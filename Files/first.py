import os 


print(os.getcwd())
os.chdir('/home/ezelenin/git/python-learning/Files')
print(os.getcwd())

try:
    os.makedirs('/tmp/mypython')
except FileExistsError:
    print('Folder is already exist')

print(os.path.basename('/home/ezelenin/git/python-learning/Files/first.py'))
print(os.path.dirname('/home/ezelenin/git/python-learning/Files/first.py'))

print(os.listdir('/home/ezelenin/git/python-learning/'))
print(str(os.path.getsize('/home/ezelenin/git/python-learning/Files/first.py')) + ' bytes')

# Read only mode
openFile = open('/home/ezelenin/git/python-learning/Files/hello.txt', 'r')
readFile = openFile.readlines()
print(readFile)
openFile.close()

# Overwrite Files
openFile = open('/home/ezelenin/git/python-learning/Files/hello.txt', 'w')
openFile.write('Modified string\n')
openFile.close()
openFile = open('/home/ezelenin/git/python-learning/Files/hello.txt', 'r')
readFile = openFile.readlines()
print(readFile)
openFile.close()

# Append to File
openFile = open('/home/ezelenin/git/python-learning/Files/append.txt', 'a')
openFile.write('New line to be written here2\n')
openFile.close()
openFile = open('/home/ezelenin/git/python-learning/Files/append.txt', 'r')
readFile = openFile.readlines()
openFile.close()
print(readFile)












