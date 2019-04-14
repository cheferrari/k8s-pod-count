# k8s-pod-count
![language](https://img.shields.io/badge/language-python-orange.svg) [![Build Status](https://travis-ci.com/cheferrari/k8s-pod-count.svg?branch=master)](https://travis-ci.com/cheferrari/k8s-pod-count)
## 1.统计k8s集群每个节点的pod数量
```shell
$ python count_node_pods.py 
('k8s-node2', 19)
('k8s-node1', 23)
```
直接使用命令统计
```shell
$ kubectl get pod --all-namespaces -o wide | grep -v NAMESPACE | awk '{print $8}' | sort | uniq -c | sort -nr
     23 k8s-node1
     19 k8s-node2
```
## 2.统计k8s集群每个namespace下pod数量
```shell
$ python count_ns_pods.py 
('kube-public', 0)
('quota-test', 5)
('istio-system', 13)
('default', 6)
('kube-system', 18)
('test', 0)
```
直接使用命令统计
```shell
$ kubectl get po --all-namespaces | grep -v NAMESPACE | awk '{print $1}' | uniq -c | sort -nr
     18 kube-system
     13 istio-system
      6 default
      5 quota-test
```
