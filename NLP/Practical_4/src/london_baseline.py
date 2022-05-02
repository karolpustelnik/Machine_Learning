# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
birth_dev = open("/home/kp446518/ML/NLP/Practical_4/birth_dev.tsv")
counter = 0
lines = 0
for line in birth_dev:
    lines += 1
    line = line.replace("\t", "")
    line = line.replace("\n", "")
    line = line.rsplit('?', 1)
    if line[1] == "London":
        counter += 1

accuracy = counter/lines
print(accuracy)
    
