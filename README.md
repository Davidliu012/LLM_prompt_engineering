# Postprocess method on BigBench Dataset (for chatGPT3.5)

## "exact_str_match" tasks
1. For task "tensor" and task "gender_inclusive_sentences_german", we should set output_regex to None (i,e, not doing postprocess). Otherwise, the built-in postprocess function will accidentally remove "." at the end of the sentence, which leads to much lower score than expected!

2. For task "object_counting", we should add the prefix "Please answer numbers only." to prevent LLM from answering "eight animals" instead of "8".

## "multi_choice_grade" tasks

### Example for the "check_ans_prompt"
1. Please help me verify the answer return by another LLM model.  
The answer list is ['(a)', '(b)'].
The first anwser in the list is labeled as the number 0. The last anwser in the list is labeled as the number 1.  
The answer return by the LLM model is "(b) Just like Hitler. A True demagogue.".  
Please choose the number that best represent the answer return by the LLM model. If the answer is not in the list, please choose the number 1000.   
You are requested to give me an integer only!  
LLM output: 1
2. Please help me verify the answer return by another LLM model.  
The answer list is ['(a)', '(b)'].  
The first anwser in the list is labeled as the number 0. The last anwser in the list is labeled as the number 1.  
The answer return by the LLM model is "I quit. This problem is nonsense.".  
Please choose the number that best represent the answer return by the LLM model. If the answer is not in the list, please choose the number 1000.  
You are requested to give me an integer only!  
LLM output: 1000

### Bug remaining
