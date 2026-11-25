import lumicron as lm
import lumicron_demo.all as pdk

@lm.pcell
def taper_to_taper_route():
    c = lm.CELL()
    
    t1 = c.add(pdk.Taper())
    t2 = c.add(pdk.Taper())
    
    c.Place(t1).at((0.0, 0.0))
    c.Place(t2).at((200.0, 500.0)).rotate_by(180.0)
    
    (
    c.Route(t1.ports["o1"])
    .go("E", by=100.0)
    .taper(width=2.0, length=5.0, offset=20.0)
    .go("N", by=150.0)
    .style("default", taper_length=5.0)
    .go("W", by=300.0)
    .go("N", to=t2.ports["o1"])
    .go("E", to=t2.ports["o1"])
    .to(t2.ports["o1"])
    )
        
    return c
    
if __name__ == "__main__":
    taper_to_taper_route()