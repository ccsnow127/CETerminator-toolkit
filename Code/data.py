import json
import os

input_dir = "AnJsonSet/100000+"
output_dir = "Testset"

for root, dirs, files in os.walk(input_dir):
    for file in files :
        if file.endswith('.json'):

            # 读取输入文件中的字典
            input_path = os.path.join(root, file)
            with open(input_path, "r") as input_file:
                input_dict = json.load(input_file)

            # 查找对应的输出文件
            # filename = os.path.splitext(filename)[0] + ".json"
            rlist = input_path.split('/')[-3:]
            foname = "/".join(rlist[:2])
            output_path = os.path.join(output_dir, os.path.join(foname, file))
            if not os.path.exists(output_path):
                print(f"Output file {output_path} not found.")
                continue

            # 读取输出文件中的字典，并将其合并到输入字典中
            with open(output_path, "r") as output_file:
                output_dict = json.load(output_file)
            output_dict.update(input_dict)

            # 将合并后的字典写入输出文件中
            with open(output_path, "w") as output_file:
                json.dump(output_dict, output_file, indent=4)

            print(f"Merged {input_path} into {output_path}.")
