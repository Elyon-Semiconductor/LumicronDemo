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
    
    c.Place(splitter).at((0,0))
    c.Place(combiner).at((x_sep, 0))
    
    return c
    
if __name__ == "__main__":
    mzi(x_sep=200.0, dL=50.0)
    
    