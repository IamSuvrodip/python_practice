def full_name(n):
    print(n)
full_name("Suvrodip Chakroborty")

name_one=("sumit")
name_two=("anirban")
name_three = ("dipendu")

'''@IamSuvrodip ➜ /workspaces/codespaces-blank (main) $ python
Python 3.10.13 (main, Mar 21 2024, 17:51:02) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import name
Suvrodip Chakroborty
>>> name.name_one
'sumit'
>>> name.name_three
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'name' has no attribute 'name_three'
>>> from importlib import reload
>>> name.name_three
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'name' has no attribute 'name_three'
>>> reload(name)
Suvrodip Chakroborty
<module 'name' from '/workspaces/codespaces-blank/name.py'>
>>> name.name_three
'dipendu'''
