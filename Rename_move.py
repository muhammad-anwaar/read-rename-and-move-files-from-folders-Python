import os

folder='Trainset_W_M_set1'

for root, dirs, files in os.walk(folder):
    for i,f in enumerate(files):
        absname = os.path.join(root, f)
        f_name, f_ext = os.path.splitext(f)
        #newname = os.path.join(root, str(i))
        if f_ext == '.jpg':   
            name_number, age= f_name.split('M');
            name_1=age+'_0_0_'+name_number+'M_morph'
            name_1=name_1.strip()
            new_name = '{}{}'.format(name_1, f_ext)
            new_name='Male/'+new_name
            #print absname,'=====> New Name =======>', new_name 
            #exit(0)
            #print 'f name===>', f_name , '==ext===>', f_ext
            #print 'age=', age, '===>number name <=====', name_number
            os.rename(absname, new_name)
        