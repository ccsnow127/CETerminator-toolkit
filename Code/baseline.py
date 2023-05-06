import openai
import json
import time
import os
openai.api_key = "XXX"#write your API key here
messages=[]
dir_path = 'dataset/testset-1'#write the path of testset

sim = {
    "n":[0,0,0,0],
    "p":[0,0,0,0],
    "d":[0,0,0,0],
    "r":[0,0,0,0],
}

out_path = "AnTXTSet/Baseline"

for root, dirs, files in os.walk(dir_path):
    for file in files :
        if file.endswith('.json'):
            tag = {
                        "n":[0,0,0,0],#[TP,FP,FN,TN]
                        "p":[0,0,0,0],
                        "d":[0,0,0,0],
                        "r":[0,0,0,0],
                    }
            with open(os.path.join(root, file), 'r') as f:
                data = json.load(f)

            if "@dev" in data:
                messages = [{"role": "user","content":"should"+data["@dev"]+"be under @dev? given the code"+data["func"]+"; your answer can only be \"yes\" or \"no\", no other response is allowed"}]
            else:continue

            start_time = time.time() # 记录开始时间
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=messages,
            max_tokens = 1500
            )

            end_time = time.time() # 记录结束时间
            fp = os.path.join(root, file)
            rlist = fp.split('/')[-3:]
            foname = "/".join(rlist[:2])
            fname = file.split('.')[0] # 去掉后缀名

            with open(f"{out_path}/{os.path.join(foname,fname)}.txt", "w") as f:
                f.write(response['choices'][0]['message']['content'])
                if (response['choices'][0]['message']['content'].split()[0]=="Yes."):
                    if data["@tdev"] == 1:
                        tag["d"][1]+=1
                    else:
                        tag["d"][0]+=1
                else:
                    if data["@tdev"] == 1:
                        tag["d"][3]+=1
                    else:
                        tag["d"][2]+=1

            print(f"Have responsed for {fname}, using {end_time-start_time:.2f} seconds.")

            for k,v in tag.items():
                if len(v)==4:
                    sim[k][0]+=v[0]
                    sim[k][1]+=v[1]
                    sim[k][2]+=v[2]
                    sim[k][3]+=v[3]   