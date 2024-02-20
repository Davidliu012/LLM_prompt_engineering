import json
import os

# Specify the path to your JSON file
for dir in os.listdir("datasets"):
    if(dir == ".DS_Store"):
        continue
    json_file_path = "datasets/" + dir + "/task.json"
    with open(json_file_path, 'r') as json_file:
        prompt = ""
        json_data = json.load(json_file)
        if "task_prefix" not in json_data.keys():
            json_data["task_prefix"] = ""
        if "example_input_prefix" not in json_data.keys():
            json_data["example_input_prefix"] = "\nQ: "
        if "example_output_prefix" not in json_data.keys():
            json_data["example_output_prefix"] = "\nA: "
        if "choice_prefix" not in json_data.keys():
            json_data["choice_prefix"] = "\n  choice: "
        if "append_choices_to_input" not in json_data.keys() and "exact_str_match" not in json_data["metrics"]:
            json_data["append_choices_to_input"] = True
        for example in json_data["examples"]:
            prompt += json_data["task_prefix"]
            prompt += json_data["example_input_prefix"]
            prompt += example["input"]
            if "append_choices_to_input" in json_data.keys() and json_data["append_choices_to_input"]:
                for choice in example["target_scores"].keys():
                    prompt += json_data["choice_prefix"]
                    prompt += choice
            prompt += json_data["example_output_prefix"]
            prompt += "\n"
            print(prompt)
            print("=====================================================")
            break

    