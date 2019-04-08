# -*- coding: utf-8 -*-
import commands
status,output = commands.getstatusoutput("kubectl get ns")
lines = output.split("\n")
namespaces={}
for i in range(0, len(lines)):
    ns = lines[i].split()[0]
    if ns == "NAME":
        continue
    namespaces[lines[i].split()[0]] = 0

#print namespaces

status, output = commands.getstatusoutput("kubectl get po --all-namespaces")
lines = output.split("\n")
for i in range(0, len(lines)):
    ns = lines[i].split()[0]
    if ns =="NAMESPACE":
        continue
    namespaces[ns] = namespaces[ns] + 1
for k,v in namespaces.items():
    print(k,v)
