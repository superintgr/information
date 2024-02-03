# computation

def pi(input):
  output = [0] * len(input)
  for index in range(len(input)):
    variable = input[index]
    if variable not in output:
        output[index] = variable
  return output

def union(array):
  output = []
  for index in array:
    if index not in output:
      output.append(index)
  return output

def compute(memory, operator):
  output = []
  for slot in memory:
    input = operator(slot)
    output += input
  return union(output)
