import os, shutil
source, target = './cifar10_full/train/', './cifar10_mini/train/'
for path in os.listdir(source):
    os.makedirs(os.path.join(target, path), exist_ok=True)
    for index, file in enumerate(sorted(os.listdir(os.path.join(source, path)))):
        if index<100:
            shutil.copy(os.path.join(source, path, file), os.path.join(target, path, file))
        else:
            break
