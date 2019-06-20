import main

def test_nearestSlot():
    n = 3
    p = main.Parking()
    p.setSlots(n)
    nSlot = p.findNearestSlot()
    assert nSlot == 1
    
def test_createParking():
    n = 3
    p = main.Parking()
    p.setSlots(n)
    totalSlot = len(p.getTotalSlots())
    assert totalSlot == n

  