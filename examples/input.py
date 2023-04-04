from sprig_circuitpython import Sprig

sprig = Sprig()

left_inputs = [0,1,2,3]
right_inputs = [4,5,6,7]

while True:
    inp = sprig.poll_input()
    print(inp)
    sprig.ledLeft.value = False
    sprig.ledRight.value = False
    if inp in left_inputs:
        sprig.ledLeft.value = True
    elif inp in right_inputs:
        sprig.ledRight.value = True