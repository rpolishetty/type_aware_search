import pickledb
import re
import sys
import os 



TAG_RE = re.compile(r'<[^>]+>')
COMMON_DICT={"this":0,\
            "at":0,\
            "that":0,\
            "is":0,\
            "are":0}

CATEGORY_DB = ['sports','food','relations'] 
SAMPLE_DB = ['love','marriage','rose','amor']

#db1 = pickledb.load('keywords.db', False)
#db2 = pickledb.load('category.db',False)
db1 = dict()
db2 = dict()

def add_to_db(db_name,item,value):
    keys = db_name.keys()
    if item in keys:

        db_name[item].append(value)
    else:
        db_name[item] = [value]   


    


def remove_tags(text):
    return TAG_RE.sub('',text)

def main(file_name):
    #creation of keywords index
    file_loc = os.path.normpath(os.path.join(os.path.dirname(__file__),file_name))
    with open(file_loc,'r') as f:
        read_data = f.read()
        new_data=remove_tags(read_data)
        #print new_data
        new_data2 =new_data.splitlines()
        #lines = [line.rstrip('\n') for line in new_data]
        line_no = 0
        for line in new_data2:
            
            #print line + ">"
            stripped_line = line.split(' ')
            for item in stripped_line:
                if item not in COMMON_DICT.keys():
                    value=file_loc+":"+str(line_no)

                    add_to_db(db1,item,value)
                else:
                    pass
            line_no += 1

    # creation of catagory index
    for item in SAMPLE_DB:
        add_to_db(db2,'relations',item)




def get_search_result(user_catagory):
    result = []
    return_val = db2[user_catagory]
    print(return_val)
    for item in return_val:
        for item in db1:
            result.append(db1[item])

    return result    




# def print_db(db_name):
#     print ("dumping db")
#     print(db_name.getall())
    
    
if __name__=='__main__':
    file_name=sys.argv[1]
    main(file_name)
    #print_db()
    #print (db1.get('pleasure'))  
    print(get_search_result('relations'))
