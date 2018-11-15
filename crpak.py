import io,os,struct,glob,codecs,math,re
lst='FONT.PAK_list.txt'
hsize=os.path.getsize(lst)
src =lst.replace('_list.txt','')
dirname = src+'_unpacked\\'
src='o_'+src
fl = open(src,'wb')
filename = os.path.basename(src)
fls=open(lst,'r')
file_num = int(fls.readline().replace('\n',''))
fl.seek(4)
fl.write(struct.pack('<I',file_num))
fl.write(b'\01\00\00\00\00\02\00\00')
fl.write(struct.pack('<I',20+file_num*8))#name_pos
fl.seek(20+file_num*8)
for i in range(file_num):
    fl.write(bytes(fls.readline().replace('\n',''),encoding='shift-jis'))
    fl.write(b'\00')
fl.seek(32,1)
now_pos=fl.tell()#记录位置
fl.seek(0)
fl.write(struct.pack('<I',now_pos))
fl.seek(now_pos)

fls.seek(0)
fls.readline()
for i in range(file_num):
    name=fls.readline().replace('\n','')
    now_pos=fl.tell()#记录位置
    file_data=open(dirname+name,'rb')
    size=os.path.getsize(dirname+name)
    fl.write(file_data.read())
    file_data.close()
    
    fl.seek(20+i*8)
    
    fl.write(struct.pack('<I',now_pos))#name_pos
    fl.write(struct.pack('<I',size))#name_pos
    print(i,now_pos,size,name)
    fl.seek(now_pos)
    fl.seek(32,1)
    

    

fls.close()

fl.close()

