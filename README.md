## Postprocess method on BigBench Dataset (for chatGPT3.5)

### "exact_str_match" tasks
1. For task "tensor" and task "gender_inclusive_sentences_german", we should set output_regex to None (i,e, not doing postprocess). Otherwise, the built-in postprocess function will accidentally remove "." at the end of the sentence, which leads to much lower score than expected!

2. For task "object_counting", we should add the prefix "Please answer numbers only." to prevent LLM from answering "eight animals" instead of "8".

### Bug remaining

There is still some bugs for a few task.