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

def add_to_db(item):
    

def remove_common_words(test):
    pass

def remove_tags(text):
    return TAG_RE.sub('',text)

def main(file_name):
    #db = pickledb.load('data.db', False)
    # read data/1342.html
    file_loc = os.path.normpath(os.path.join(os.path.dirname(__file__),file_name))
    with open(file_loc,'r') as f:
        read_data = f.read()
        new_data=remove_tags(read_data)
        print new_data
        new_data2 =new_data.splitlines()
        #lines = [line.rstrip('\n') for line in new_data]
        for line in new_data2:
            #print line + ">"
            stripped_line = line.split(' ')
            for item in stripped_line:
                if item not in COMMON_DICT.keys():
                    add_to_db(item)
                else:
                    print "<skip>"    
        
    
    

    
if __name__=='__main__':
    file_name=sys.argv[1]
    main(file_name)    
