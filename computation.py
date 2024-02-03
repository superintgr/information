# computation

def computation(state, operator):
  variables = None
  for x in state:
    variable = (x, operator(x))
    if variables == None:
      variables = variable
    else:
      variables += variable
  
