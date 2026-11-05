import lumicron as lm

top = lm.CELL("TOP")
# Replace this inspection tile with your design and environment packages.
top.add(lm.Rectangle(40, 20, layer=lm.LayerSpec(layer=1, datatype=0), centered=False))
