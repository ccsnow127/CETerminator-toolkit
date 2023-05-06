import openai
import json
import time
import os
openai.api_key = ""#write your API key here
messages=[]

dir_path = 'dataset/testset-1'#write the path of testset

out_path = "AnTXTSet"#write the path of output directory

for root, dirs, files in os.walk(dir_path):
    for file in files :
        if file.endswith('.json'):
            with open(os.path.join(root, file), 'r') as f:
                data = json.load(f)

            messages = data['message']
            start_time = time.time() 

            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=messages,
            max_tokens = 1500
            )

            end_time = time.time()
            fp = os.path.join(root, file)
            rlist = fp.split('/')[-3:]
            foname = "/".join(rlist[:2])
            fname = file.split('.')[0]

            with open(f"{out_path}/{os.path.join(foname,fname)}.txt", "w") as f:
                f.write(response['choices'][0]['message']['content'])

            print(f"Have responsed for {fname}, using {end_time-start_time:.2f} seconds.")
