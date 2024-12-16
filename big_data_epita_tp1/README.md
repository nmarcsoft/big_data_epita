# RENDU

Ce projet utilise hadoop pour segmenter les opérations de map reduce sur un fichier.txt donnée en entrer.

### Prérequis:
```bash
docker pull liliasfaxi/hadoop-cluster:latest
docker network create --driver=bridge hadoop
```

### Container à executer :
```bash
docker run -itd --net=hadoop -p 9870:9870 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/hadoop-cluster:latest
docker run -itd -p 8040:8042 --net=hadoop --name hadoop-worker1 --hostname hadoop-worker1 liliasfaxi/hadoop-cluster:latest
docker run -itd -p 8041:8042 --net=hadoop --name hadoop-worker2 --hostname hadoop-worker2 liliasfaxi/hadoop-cluster:latest
```

### Exemple d'utilisation

```bash
docker cp exercice/ hadoop-master:/root/
docker exec -it hadoop-master
cd exercice/
cat purchases.txt | python3 mapper_wanted.py > mapper_wanted_output.txt

```
