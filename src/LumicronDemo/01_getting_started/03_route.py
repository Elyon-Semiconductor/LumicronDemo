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
    
    c.Route(splitter.ports["o2"]).to(combiner.ports["o1"])
    
    return c
    
if __name__ == "__main__":
    mzi(x_sep=100.0, dL=50.0)