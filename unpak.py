import io,os,struct,glob,codecs,math,re,sys
src = 'SCRIPT.PAK'

fl = open(src,'rb')
filename = os.path.basename(src)
if os.path.isdir(filename+'_unpacked') == False:
        os.makedirs(filename+'_unpacked')
flh=open(src+'_list.txt','w')


data_pos, = struct.unpack('<I',fl.read(4))
file_num, = struct.unpack('<I',fl.read(4))
flh.write(str(file_num)+'\n')
fl.seek(8,1)
name_pos, = struct.unpack('<I',fl.read(4))
print(file_num)
temp_name_pos=0

for i in range(file_num):
    fl.seek(20+i*8)
    offset, = struct.unpack('<I',fl.read(4))
    size, = struct.unpack('<I',fl.read(4))

    fl.seek(name_pos+temp_name_pos)
    temp, = struct.unpack('B',fl.read(1))
    temp_name_pos=temp_name_pos+1
    leng=0
    while temp != 0 :
        leng=leng+1
        temp, = struct.unpack('B',fl.read(1))
    temp_name_pos=temp_name_pos+leng
    fl.seek(-leng-1,1)
    byte=fl.read(leng)
    fl.seek(1,1)
    name=str(byte, encoding="shift-jis")
    print(offset,size,name)
    
    flh.write(name+'\n')
    
    old = open(filename+'_unpacked\\'+name,'wb')
    fl.seek(offset)
    old.write(fl.read(size))
    old.close()
    

flh.close()  
fl.close()

