import os
for root, dirs, files in os.walk("."):
#    for name in files:
#       print(os.path.join(root, name))
   for name in dirs:
        print(name)
#       print(os.path.join(root, name))