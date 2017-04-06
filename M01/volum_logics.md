#		 VOLUMS LÒGICS

 * __Descripció del que són:__

    LVM (Gestor de volumns lògics) o Logical Volume Manager es una capa d'abstracció entre un dispositiu d'emmagatzematge i un sistema de fitxers.

* __Que volen dir les sigles, definició, analogies i exemples de comandes (explicant el que fan) vistes a classe de:__

	__PV__ → Phisical Volume: Identificació de discs, crea un disc dur a partir de 3 discs durs 
	
__COMANDES__

- pvcreate /dev/vda 
- pvs  → mostrava els fisicals Volums que tenies 



    __VG__  → Volume Groups: Discs Virtuals, son els discs que creem despres de crear el PV
    
**COMANDES**
    
- vgcreate 
- vgs


    **LV** → Logical Volume: Particions dins dels volums logics creats 
    
**COMANDES**
    
- lsvcreate
- lvs 

***practica 1*** 
