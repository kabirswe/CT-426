# PIP
# Python packages manager

# pip install pip

# install a package
# pip install camelcase
# uninstall package
# pip uninstall camelcase
# package list
# pip list

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
