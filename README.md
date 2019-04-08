# k8s-pod-count
## 1.统计k8s集群每个节点的pod数量
```shell
# python count_node_pods.py 
('k8s-node2', 19)
('k8s-node1', 23)
```
## 1.统计k8s集群每个namespace下pod数量
```shell
# python count_ns_pods.py 
('kube-public', 0)
('quota-test', 5)
('istio-system', 13)
('default', 6)
('kube-system', 18)
('test', 0)
```
