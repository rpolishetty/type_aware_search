import pickledb
import re
import sys
import os 
import hashedindex
from hashedindex import textparser




TAG_RE = re.compile(r'<[^>]+>')
COMMON_DICT={"this":0,\
            "at":0,\
            "that":0,\
            "is":0,\
            "are":0}

CATEGORY_DB = ['sports','food','relations'] 
SAMPLE_DB = ['love','marriage','rose']

similar_words_dict = {}
catagory_dict = {}


catagory_dict['relations'] = ['love','marriage','rose','amor']
catagory_dict['sports'] = ['sports','cricket','golf','soccer','messi','ronaldo']

similar_words_dict['love'] = [{'love':1,'marriage':.8,'couple':.6,'happy':.5,'affectionate':.7}]
similar_words_dict['need'] = [{'need':1,'require':.8,'essential':.7}]
similar_words_dict['joy'] = [{'joy':1}]
#db1 = pickledb.load('keywords.db', False)
#db2 = pickledb.load('category.db',False)
db1 = dict()
db2 = dict()
index = hashedindex.HashedIndex()
def add_to_db(db_name,item,value):
    keys = db_name.keys()
    counter = 1
    if item in keys:
        counter = db_name[item][1] + 1
        db_name[item].append([value,counter])
    else:
        db_name[item] = [value,counter]   


    


def remove_tags(text):
    return TAG_RE.sub('',text)

def build_inv_index(file_name):
    

    #creation of keywords index
    file_loc = os.path.normpath(os.path.join(os.path.dirname(__file__),file_name))
    with open(file_loc,'r') as f:
        read_data = f.read()
        new_data=remove_tags(read_data)
        new_data2 =new_data.splitlines()

        for line in new_data2:

            stripped_line = line.split(' ')

            for item in stripped_line:

                index.add_term_occurrence(item, file_loc)


    # creation of catagory index
    for item in SAMPLE_DB:
        add_to_db(db2,'relations',item)

def search(query, category):
    result = {}
    for item in query.split():
        sim_item = {}
        sim_item[item]=1.0
        if item in similar_words_dict.keys():
            sim_item = similar_words_dict[item]

        print (sim_item)
        for token,value in sim_item.items():    
            try:
                
                if token in result.keys():
                    result[token].append(index.get_documents(token))
                    print("[added]", result[item])
                else :
                    result[token]=index.get_documents(token)
                    #print("[created]", result[item])
                    print("keys:", result.keys())
            except Exception as e:
                print ("Got error with ", token)

    return result    




def get_search_result(user_catagory):
    result = []
    return_val = db2[user_catagory]
    print(return_val)
    for item in return_val:
        for item in db1:
            result.append(db1[item])

    return result    


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]



def user_interface():
    query = input('enter your search string:')
    print("1.sports \n 2.love\n")
    category = input ('select catagory:')
    search_in=''
    if category==1:
        search_in="sports"
    elif category==2:
        search_in="relations"    
    return query, search_in


# def print_db(db_name):
#     print ("dumping db")
#     print(db_name.getall())
    
    
if __name__=='__main__':
    #file_name=sys.argv[1]
    query, category = user_interface()
    print(query,category)
    listdir = listdir_fullpath('/Users/rohith/type_aware_search/data')
    for file_name in listdir:
        #os.path.join(__file__,'data',file_name)
        print (file_name)
        
        build_inv_index(file_name)

    #index.add_term_occurrence('love','null')
    #print(index.get_documents('love'))
    result = (search(query,category))
    for key, value in result.items() :
        print ("key:",key,"\n" ,value)
        print ("------------\n")

