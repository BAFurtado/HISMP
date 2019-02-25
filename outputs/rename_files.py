import os

for dirpath, dirnames, files in os.walk(os.getcwd()):
    for f in files:
        if f.startswith('fig_'):
            new = f.replace('.', '').replace('_50rep', '.')
            os.rename(os.path.join(dirpath, f), os.path.join(dirpath, new))
