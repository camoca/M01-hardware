## VOLUMS LÒGICS

Descripció del que són:

LVM (Gestor de volumns lògics) o Logical Volume Manager es una capa d'abstracció entre un dispositiu d'emmagatzematge i un sistema de fitxers.

Que volen dir les sigles, definició, analogies i exemples de comandes (explicant el que fan) vistes a classe de:

**PV** → Phisical Volume: Identificació de discs, crea un disc dur a partir de 3 discs durs

**COMANDES**

```
    pvcreate /dev/vda
   pvs → mostrava els fisicals Volums que tenies
```

__VG__  → Volume Groups: Discs Virtuals, son els discs que creem despres de crear el PV

**COMANDES**

```
    vgcreate multimedia /dev/vda → crea els discs virtuals
vgs → mostra els discs digitals creats
```

**LV** → Logical Volume: Particions dins dels volums logics creats 

**COMANDES**

```
    lsvcreate -L 250M -n Videos multimedia → crea els volums logics 
lvs→ mostra els volums logics creats
```

++**PRACTICA 1**++

primer de tot creem els discs virtuals 

![image](/home/users/inf/hism1/ism25366309/Videos/HD.png)

entrem com a root

y executem la seguent comanda qu creara l'identificador de discs

```
[root@localhost ~]# pvcreate /dev/vda /dev/vdb
  Physical volume "/dev/vda" successfully created.
  Physical volume "/dev/vdb" successfully created.
[root@localhost ~]# **
```
comprobem que esta ben creat 

```
[root@localhost ~]# pvs
  PV         VG     Fmt  Attr PSize   PFree  
  /dev/sda2  fedora lvm2 a--   19.51g      0 
  /dev/vda          lvm2 ---  512.00m 512.00m
  /dev/vdb          lvm2 ---  512.00m 512.00m
[root@localhost ~]# 
```
ara creem els discs virtuals 

```
[root@localhost ~]# vgcreate practica1 /dev/vda
  Volume group "practica1" successfully created
``` 
y els comprovem 

```
[root@localhost ~]# vgcreate practica1 /dev/vda
  Volume group "practica1" successfully created
```
creem els volums logics

```
[root@localhost ~]# lvcreate -l 100%FREE -n P1 practica1
  Logical volume "P1" created.
```
y els comprovem 

```
[root@localhost ~]# lvs
  LV   VG        Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root fedora    -wi-ao----  17.51g                                                    
  swap fedora    -wi-ao----   2.00g                                                    
  P1   practica1 -wi-a----- 508.00m                                                    
[root@localhost ~]# 
```


++**PRACTICA 2**++

creem un sistema de fitxers xfs

```
[root@localhost ~]# mkfs.xfs /dev/practica1/P1 
meta-data=/dev/practica1/P1      isize=512    agcount=4, agsize=32512 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=0
data     =                       bsize=4096   blocks=130048, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=855, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0

```
i ho montem a /mnt

```
[root@localhost ~]# mount /dev/practica1/P1 /mnt/
```
i creem el fitxer de 180M

```
[hardware@localhost ~]$ dd if=/dev/zero of=practica.img bs=1K count=180000
180000+0 records in
180000+0 records out
184320000 bytes (184 MB, 176 MiB) copied, 0.5659 s, 326 MB/s
[hardware@localhost ~]$ 
```

++**PRACTICA 3**++

creem el raid1 i el comprobem

```
[root@localhost ~]# mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/vdb /dev/vdc
mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
Continue creating array? yes
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
[root@localhost ~]# cat /proc/mdstat 
Personalities : [raid1] 
md0 : active raid1 vdc[1] vdb[0]
      523712 blocks super 1.2 [2/2] [UU]
      
unused devices: <none>
[root@localhost ~]# 
```

++**PRACTICA 4**++

creem el /dev/md0

```
[root@localhost ~]# pvcreate /dev/md0 
  Physical volume "/dev/md0" successfully created.
```

extenem practica1

```
[root@localhost ~]# vgextend practica1 /dev/md0
  Volume group "practica1" successfully extended
```

i extenem el volum logic 

```
[root@localhost ~]# lvextend -l 100%FREE /dev/practica1/dades
  New size (127 extents) matches existing size (127 extents)
```


++**PRACTICA 5**++

fem xfs_growfs /dev/practica1/dades

```
[root@localhost ~]# xfs_growfs /dev/practica1/dades
meta-data=/dev/mapper/practica1-dades isize=512    agcount=4, agsize=32512 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1 spinodes=0
data     =                       bsize=4096   blocks=130048, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=855, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
[root@localhost ~]# 
```

ho comprobem amb lsblk 

```
[root@localhost ~]# lsblk
NAME              MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                 8:0    0    20G  0 disk  
├─sda1              8:1    0   500M  0 part  /boot
└─sda2              8:2    0  19.5G  0 part  
  ├─fedora-root   253:0    0  17.5G  0 lvm   /
  └─fedora-swap   253:1    0     2G  0 lvm   [SWAP]
sr0                11:0    1  1024M  0 rom   
vda               252:0    0   512M  0 disk  
└─practica1-dades 253:2    0   508M  0 lvm   /mnt
vdb               252:16   0   512M  0 disk  
└─md0               9:0    0 511.4M  0 raid1 
vdc               252:32   0   512M  0 disk  
└─md0               9:0    0 511.4M  0 raid1 
[root@localhost ~]# 
```

i amb df -h

```
[root@localhost ~]# df -h
Filesystem                   Size  Used Avail Use% Mounted on
devtmpfs                     998M     0  998M   0% /dev
tmpfs                       1008M  204K 1008M   1% /dev/shm
tmpfs                       1008M  960K 1007M   1% /run
tmpfs                       1008M     0 1008M   0% /sys/fs/cgroup
/dev/mapper/fedora-root       18G  3.3G   13G  20% /
tmpfs                       1008M   36K 1008M   1% /tmp
/dev/sda1                    477M  130M  318M  30% /boot
tmpfs                        202M   12K  202M   1% /run/user/1000
/dev/mapper/practica1-dades  505M   26M  480M   6% /mnt
[root@localhost ~]# 
```

dins de /mnt:

creem l'arxiu que ens demanen

```
[root@localhost mnt]# dd if=/dev/zero of=itxer1.img bs=1K count=180000
180000+0 records in
180000+0 records out
184320000 bytes (184 MB, 176 MiB) copied, 0.553675 s, 333 MB/s
[root@localhost mnt]# 
```
