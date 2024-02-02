# information

I : "information"
i : "copy"
S : "substrate"
x : "variable"
X : "state"

def computation(substrate, medium):
    """
    Defines a function `C(S)` on substrate `S` of at least two possible state `x` in `X`, whose transformation consists of applying permutation to each `x` in substrate `S` where `x` -> `permutation(x)`.

    C(S) := union(for all x in S -- {x -> permutations(x)}).
    .. permutation task must be possible in order to cause the commutation relation to be possible, although with side effects allowed if required.
    """
    output = []
    for state in substrate:
        p = permutations(state)
        result = []
        for x in p:
            if x in medium(x):
                result.append(x)
        variable = union(result)
        output.append(variable)
    return output
            
                
