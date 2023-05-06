import os
import glob
import re
import json 
folder_path = "AnTXTSet/100000+"
out_path = "AnJsonSet"

for root, dirs, files in os.walk(folder_path):
    for file in files :
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                pattern = r'^@.*'
                matches = []
                for line in lines:
                    if re.match(pattern, line):
                        matches.append(line.strip())
                j={}
                ctr = {
                    "@notice": 0,
                    "@param": 0,
                    "@return": 0,
                }
                rlist = file_path.split('/')[-3:]
                foname = "/".join(rlist[:2])
                fname = rlist[2].split('.')[0] # 去掉后缀名
                with open(f"{out_path}/{os.path.join(foname,fname)}.json", 'w')as f:
                    for item in matches:
                        key = item.split(' ', 1)[0]
                        if key in ctr:
                            ctr[key] += 1
                            if key =="@notice":
                                j["@gnotice"] = item.split(' ', 1)[1]
                            elif key =="@param":
                                j["@gparam"+str(ctr[key])] = item.split(' ', 1)[1]
                            else:
                                j["@greturn"+str(ctr[key])] = item.split(' ', 1)[1]


                    json.dump(j,f,indent=4)
