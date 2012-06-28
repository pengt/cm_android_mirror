import sys
from pygithub3 import Github
import xml.dom.minidom

gh = Github()
repos = gh.repos.list('CyanogenMod').all()

doc = xml.dom.minidom.Document()
root = doc.createElement('manifest')
doc.appendChild(root)

e = doc.createElement('remote')
e.setAttribute('name', 'github')
e.setAttribute('fetch', 'git://github.com/CyanogenMod/')
root.appendChild(e)

e = doc.createElement('default')
e.setAttribute('remote', 'github')
e.setAttribute('revision', 'master')
e.setAttribute('sync-j', '4')
root.appendChild(e)

for repo in repos:
    e = doc.createElement('project')
    e.setAttribute('name', repo.name)
    root.appendChild(e)

#fd = sys.stdout
fd = open('default.xml', 'w')
doc.writexml(fd, '', '  ', '\n', 'UTF-8')