import lumicron as lm
from lumicron_demo.all import MMI1x2

@lm.pcell
def mzi(
    x_sep: float,
    dL: float
):
    c = lm.CELL()
    
    splitter = c.add(MMI1x2())
    combiner = c.add(MMI1x2())
    
    c.Place(splitter).using(splitter.ports["o1"]).at((-x_sep/2,0))
    c.Place(combiner).using(combiner.ports["o1"]).relative_to(splitter.ports["o2"]).move_by(dx=x_sep).rotate_by(180.0)
    
    r1 = c.Route(splitter.ports["o2"]).to(combiner.ports["o1"])
    
    c.Route(splitter.ports["o1"]).to(combiner.ports["o2"]).match_length_to(r1, dL=dL, style="direct", flip=True)
    
    
    #Below are alternate ways to express path length matched routes. Style changes the detour route and flatten changes the spread of the shape 
    #Comment line 19 and un-comment each line below to see the resulting layout
    
    # c.Route(splitter.ports["o1"]).to(combiner.ports["o2"]).match_length_to(r1, dL=dL, style="manhattan", flip=True)
    # c.Route(splitter.ports["o1"]).to(combiner.ports["o2"]).match_length_to(r1, dL=dL, flip=True, style="direct", flatten=0.9)
    # c.Route(splitter.ports["o1"]).to(combiner.ports["o2"]).match_length_to(r1, dL=dL, flip=True, style="manhattan", flatten=0.9)


    
    return c
    
if __name__ == "__main__":
    mzi(x_sep=200.0, dL=100.0)