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
def taper_bundle(n_tapers: int):
    c = lm.CELL()
    
    left = c.add(taper_array(n_tapers=n_tapers))
    right = c.add (taper_array(n_tapers=n_tapers))
    
    c.Place(left).using("C").at((-400.0, 0.0))
    c.Place(right).using("C").at((400.0, 300.0)).flipX()
    
    sources = [left.ports[f"out_{i}"] for i in range(int(n_tapers/2))]
    destinations = [right.ports[f"out_{i}"] for i in range(int(n_tapers/2))]
    
    sources1 = [left.ports[f"out_{i}"] for i in range(int(n_tapers/2), n_tapers)]
    destinations1 = [right.ports[f"out_{i}"] for i in range(int(n_tapers/2), n_tapers)]

    b1 = c.Route(sources, style="manhattan", radius=25.0).to(destinations).match_lengths(flip=True, flatten=0.8)
    b2 = c.Route(sources1, style="manhattan", radius=25.0).to(destinations1).match_length_to(b1, flatten=0.8)
    
    return c
    
if __name__ == "__main__":
    taper_bundle(n_tapers = 16)
    

    