| NIVELLS | Nº MINIM DISCS | Nº MAXIM DISCS FALLATS | CAPACITAT | READ | WRITE |
| :-----: | :------------: | :--------------------: | :-------: | :--: | :---: | 
| RAID 0  |       2        |         0              |    100%   |  E   |   E   |
| RAID 1  |       2(MAX)   |         1              |     50%   |  VG  |   G   |
| RAID 5  |       3        |         1              | 67%-94%   |  VG  |   G   |
| RAID 6  |       4        |         2              | 50%-88%   |  G   |   G   |
| RAID10  |       4        |         1/mirror       |     50%   |  VG  |   G   |


# DESCRIPCION DE LA METODOLOGIA UTILIZADA EN CLASE PER FER PROVAS EN MAQUINAS VIRTUALS


1. 	Una vegada creada la maquina virtual 
2.	Creem 3 discs de 200MB cada un
3.	Ens posem com root
4.	Executem la comanda **mdadm**
5. 	**mdadm --create < nom dispositiu> --level=< nivell del raid> --raid-devices=< nº de discos> < disc1> < disc2>**
6.	Quedaria així mdadm -- create /dev/md0 --level=1 --raid-devices=2 /dev/vda /dev/vdb
7.	**cat /proc/mdstat** (fitxer on tenim l'estat del raid)
8.	lsblk
9.	mkfs.ext4 /dev/md0
10.	mount /dev/md0 /mnt
11.	df -h
12.	cd /mnt
13.	dd if= /dev/cero of=test.img bs=4k count=1000
14.	ls -lh
15.	less test.img
	DESPRES FEM FALLAR EL DISC PER VEURE COM ES COMPORTA EL RAID
