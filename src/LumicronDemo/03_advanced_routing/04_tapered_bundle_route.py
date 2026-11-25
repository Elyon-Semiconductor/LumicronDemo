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
def tapered_bundle(n_tapers: int):
    c = lm.CELL()
    
    left = c.add(taper_array(n_tapers=n_tapers))
    right = c.add (taper_array(n_tapers=n_tapers))
    
    c.Place(left).using("C").at((-400.0, 0.0))
    c.Place(right).using("C").at((800.0, 800.0)).flipX()
    
    sources = [left.ports[f"out_{i}"] for i in range(n_tapers)]
    destinations = [right.ports[f"out_{i}"] for i in range(n_tapers)]

    (
    c.Route(sources, style="manhattan", spine=0)
    .go("E", by=2000)
    .taper(width=2.0, length=5.0, offset=20.0)
    .go("N", by=300)
    .style("default", taper_length=5.0)
    .go("W", by=1500)
    .go("N", by=200)
    .to(destinations)
    )
    
    #You can control the widths, taper length, and offsets in each waveguide in the bundle as well
    #Comment the above routing call and un-comment the code below to see how the N by 300 section of the route 
    #changes its width across each waveguide in the bundle
    
    # widths = [1.25 + 0.25 * i for i in range(n_tapers)]
    # taper_lengths = [5.0 + i for i in range(n_tapers)]
    # taper_offsets = [10.0 + 2.0 * i for i in range(n_tapers)]

    # (
        # c.Route(sources, style="manhattan", spine=0)
        # .go("E", by=2000)
        # .taper(
            # width=widths,
            # length=taper_lengths,
            # offset=taper_offsets,
        # )
        # .go("N", by=300)
        # .style("default", taper_length=5.0)
        # .go("W", by=1500)
        # .go("N", by=200)
        # .to(destinations)
    # )
    
    
    return c
    
if __name__ == "__main__":
    tapered_bundle(n_tapers = 8)
    

    