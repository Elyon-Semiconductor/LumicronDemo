import lumicron as lm
import lumicron_demo.all as pdk

@lm.pcell
def taper_array(n_tapers: int):
    c = lm.CELL()
    
    for i in range(n_tapers):
        ref = c.add(pdk.Taper())
        c.Place(ref).at((0.0, 127.0 * i))
        
        ref.promote(ports={
            "i1": f"in_{i}",
            "o1": f"out_{i}",
        })
        
    return c
    
@lm.pcell
def bundle_steering(n_tapers: int):
    c = lm.CELL()
    
    left = c.add(taper_array(n_tapers=n_tapers))
    right = c.add (taper_array(n_tapers=n_tapers))
    
    c.Place(left).using("C").at((-400.0, 0.0))
    c.Place(right).using("C").at((800.0, 800.0)).flipX()
    
    sources = [left.ports[f"out_{i}"] for i in range(n_tapers)]
    destinations = [right.ports[f"out_{i}"] for i in range(n_tapers)]

    (
    c.Route(sources, style="manhattan")
    .go("E", by=2000.0)
    .go("N", by=160.0)
    .go("W", by=1500.0)
    .go("N", by=150.0)
    .to(destinations)
    )
    
    #In the routing call below, the argument spine=0 inside of Route() makes the router use wg number 0 in the bundle as the spine to create the bundle route
    #You can change the spine number to select a certain waveguide in the bundle as the spine for the bundle route
    
    # (
    # c.Route(sources, style="manhattan", spine=0)
    # .go("E", by=2000.0)
    # .go("N", by=160.0)
    # .go("W", by=1500.0)
    # .go("N", by=150.0)
    # .to(destinations)
    # )
    
    return c
    
if __name__ == "__main__":
    bundle_steering(n_tapers = 8)
    

    