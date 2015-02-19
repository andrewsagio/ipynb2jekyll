#!/usr/bin/python

import sys
import json
def convert(inFile, title = 'Title'):
    
    # open ipython notebook
    json_data=open(inFile)
    data = json.load(json_data)

    # Jekyll post header
    s = str()
    s+='---\ntitle: '+title+'\nlayout: post\n---\n'

    # convert notebook to md
    for m in data["worksheets"][0]['cells']:
        if m['cell_type'] == 'markdown':
            for source in m['source']:
                s += source
            s+='\n'
        elif m['cell_type'] == 'heading':
            s+= '#'*m['level']+ m['source'][0]+'\n\n'
        elif m['cell_type'] == 'code':
            s+= '\n```'+m['language']+'\n'
            for codes in m['input']:
                s += codes
            s+= '\n```\n \n<br>\n'
            if m['outputs']:
                s += '\n```\n'
                s+='Output:\n'
                for op in m['outputs']:
                    for t in op['text']:
                        s+=t
                s += '\n```\n\n<br>\n'

    # write to file
    outFile = inFile.replace('.ipynb', '.md')
    print 'Writing file: '+outFile
    text_file = open(outFile, "w")
    text_file.write(s)
    text_file.close()
    return s

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Usage: ipynb2jekyll inFile [title]'
        sys.exit(1)
    elif len(sys.argv) == 2:
        convert(sys.argv[1])
    elif len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
        
    print "Converted ipython notebook to jekyll markdown successfully."

