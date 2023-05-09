import nltk
import os
import json
import math
import re
import numpy as np

data_dir = "dataset/testset-1"#write your testset path here

thres=50
stop_words = set(nltk.corpus.stopwords.words('english'))
from nltk.stem import PorterStemmer
ps = PorterStemmer()
TsimCtr = 0
TunsimCtr = 0

sim = {
    "@notice":[0,0],
    "@param":[0,0],
    "@return":[0,0],
    "@dev":[0,0],
    "n":[0,0,0,0],
    "p":[0,0,0,0],
    "d":[0,0,0,0],
    "r":[0,0,0,0],
    "np":np.empty(0),
    "pp":np.empty(0),
    "rp":np.empty(0)
}

for root, dirs, files in os.walk(data_dir):

    for file in files :

        if file.endswith('.json'):

            file_path = os.path.join(root, file)
            rlist = file_path.split('/')[-3:]
            filename = "/".join(rlist[1:3])

            with open(file_path, 'r') as f:

                if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:

                    data = json.load(f)
                    keys = [key for key in data.keys() if key.startswith('@') and key[1] != 'g' and key[1]!='t']
                    gkeys = [key for key in data.keys() if key.startswith('@') and key[1] == 'g' and key[2]!='t']

                    tag = {
                        "@notice":[0,0],
                        "@param":[0,0],
                        "@return":[0,0],
                        "@dev":[0,0],
                        "n":[0,0,0,0],
                        "p":[0,0,0,0],
                        "d":[0,0,0,0],
                        "r":[0,0,0,0],
                        "np":np.empty(0),
                        "pp":np.empty(0),
                        "rp":np.empty(0)
                    }

                    for key in keys:
                            
                            if key=="@dev":
                                gkey="@gnotice"

                            elif key=="@notice":
                                gkey="@gnotice"

                            else:
                                gkey = key[:1] + 'g' + key[1:]

                                if gkey not in gkeys:
                                    continue

                            text1 = data[key]
                            text2 = data[gkey]

                            words1 = text1.split()
                            words2 = text2.split()

                            filtered_words1 = [word for word in words1 if word.casefold() not in stop_words and len(word)!=1]
                            filtered_words2 = [word for word in words2 if word.casefold() not in stop_words and len(word)!=1]

                            cleaned_words1 = [re.sub(r'[^a-zA-Z]', '', word) for word in filtered_words1]
                            cleaned_words2 = [re.sub(r'[^a-zA-Z]', '', word) for word in filtered_words2]

                            stemmed_words1 = [ps.stem(word) for word in cleaned_words1]
                            stemmed_words2 = [ps.stem(word) for word in cleaned_words2]

                            count = 0

                            for word in set(stemmed_words1):

                                if word in stemmed_words2:
                                    count += 1

                            if len(stemmed_words1)!=0:
                                percentage = (count / len(stemmed_words1)) * 100
                                percentage = math.ceil(percentage)

                                if percentage>=thres:
                                    TsimCtr+=1

                                    if key!="@dev":
                                        tag[key[1]+"p"] = np.append(tag[key[1]+"p"],percentage)

                                    if key[0:6]=="@param":
                                        tag[key[0:6]][0]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["p"][0]+=1

                                        else:
                                            tag["p"][1]+=1

                                    elif key[0:7]=="@return":
                                        tag[key[0:7]][0]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["r"][0]+=1

                                        else:
                                            tag["r"][1]+=1

                                    elif key=="@notice":
                                        tag["@notice"][0]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["n"][0]+=1

                                        else:
                                            tag["n"][1]+=1

                                    else:
                                        tag["@dev"][1]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["d"][2]+=1

                                        else:
                                            tag["d"][3]+=1

                                else:
                                    TunsimCtr+=1    

                                    if key!="@dev":
                                        tag[key[1]+"p"] = np.append(tag[key[1]+"p"],percentage)

                                    if key[0:6]=="@param":
                                        tag[key[0:6]][1]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["p"][2]+=1

                                        else:
                                            tag["p"][3]+=1

                                    elif key[0:7]=="@return":
                                        tag[key[0:7]][1]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["r"][2]+=1

                                        else:
                                            tag["r"][3]+=1

                                    elif key=="@notice":
                                        tag["@notice"][1]+=1

                                        if data["@t"+key[1:]]==0:
                                            tag["n"][2]+=1

                                        else:
                                            tag["n"][3]+=1

                                    else:
                                        tag["@dev"][0]+=1

                                        if data["@t"+key[1:]]==1:
                                            tag["d"][1]+=1

                                        else:
                                            tag["d"][0]+=1

                    for k,v in tag.items():

                        if isinstance(v, np.ndarray):
                            sim[k] = np.append(sim[k],v)

                        elif len(v)==2:
                            sim[k][0]+=v[0]
                            sim[k][1]+=v[1]
                            
                        elif len(v)==4:
                            sim[k][0]+=v[0]
                            sim[k][1]+=v[1]
                            sim[k][2]+=v[2]
                            sim[k][3]+=v[3]     