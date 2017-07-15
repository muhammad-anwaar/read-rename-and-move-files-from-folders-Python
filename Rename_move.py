import os
#folder name here
folder=''

for root, dirs, files in os.walk(folder):
    for i,f in enumerate(files):
        absname = os.path.join(root, f)
        f_name, f_ext = os.path.splitext(f)
        #check file extension
        if f_ext == '.jpg':   
            name_number, age= f_name.split('M');
            #renaming file
            name_1=age+'_0_0_'+name_number+'-'
            name_1=name_1.strip()
            new_name = '{}{}'.format(name_1, f_ext)
            new_name='Male/'+new_name
            #finallly move to another folder
            os.rename(absname, new_name)
        
