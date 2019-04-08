# -*- coding: utf-8 -*-
import commands
status, output = commands.getstatusoutput("kubectl get node")
lines = output.split("\n")
nodes = {}
#node['<none>'] = 0
for i in range(0, len(lines)):
    no = lines[i].split()[0]
    if no == "NAME":
        continue
    nodes[lines[i].split()[0]] = 0

#print nodes

status, output = commands.getstatusoutput("kubectl get po --all-namespaces -o wide")
lines = output.split("\n")
for i in range(0, len(lines)):
    no = lines[i].split()[7]
    if no == "NODE":
        continue
    nodes[lines[i].split()[7]] = nodes[lines[i].split()[7]] + 1
for k, v in nodes.items():
    print(k, v)
