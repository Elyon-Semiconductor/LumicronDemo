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
def composite_bundle(n_tapers: int):
    c = lm.CELL()
    
    left = c.add(taper_array(n_tapers=n_tapers))
    right = c.add (taper_array(n_tapers=n_tapers))
    
    c.Place(left).using("C").at((-400.0, 0.0))
    c.Place(right).using("C").at((800.0, 800.0)).flipX()
    
    sources = [left.ports[f"out_{i}"] for i in range(n_tapers)]
    destinations = [right.ports[f"out_{i}"] for i in range(n_tapers)]
    
    # (
    # c.Route(sources, style="manhattan", spine=0)
    # .go("E", by=2000)
    # .taper(width=2.0, length=5.0, offset=20.0)
    # .go("N", by=300)
    # .taper(width=sources[0].width, length=5.0)
    # .style(profile=pdk.RP.nitride,
           # transition_at="start", transition_offset=20)
    # .go("W", by=1500)
    # .style("default",
           # transition_at="end", transition_offset=20)
    # .go("N", by=200)
    # .to(destinations)
    # )
    
    profiles = [
        pdk.RP.nitride if i % 2 == 0 else None
        for i in range(n_tapers)
    ]
    restore_profiles = [
        "default" if i % 2 == 0 else None
        for i in range(n_tapers)
    ]

    # Return tapers for lanes that will change layers.
    return_widths = [
        sources[i].width if i % 2 == 0 else None
        for i in range(n_tapers)
    ]

    # Return the other lanes to their original width.
    strip_resets = [
        None if i % 2 == 0 else "default"
        for i in range(n_tapers)
    ]

    entry_offsets = [20.0 + 10.0 * i for i in range(n_tapers)]
    exit_offsets = [40.0 + 5.0 * i for i in range(n_tapers)]

    (
        c.Route(sources, style="manhattan", spine=0, radius=25)
        .go("E", by=2000)

        # All lanes widen on the northbound leg.
        .taper(width=2.0, length=5.0, offset=20.0)
        .go("N", by=300)

        # All lanes taper back before the westward turn.
        .taper(width=return_widths, length=5.0)
        .style(strip_resets, taper_length=5.0)

        # Only even-numbered lanes transition to nitride.
        .style(
            profile=profiles,
            transition_at="start",
            transition_offset=entry_offsets,
        )
        .go("W", by=1500)

        # Transition those lanes back before leaving this straight.
        .style(
            restore_profiles,
            transition_at="end",
            transition_offset=exit_offsets,
        )
        .go("N", by=300)
        .to(destinations)
    )
    
    
    return c
    
if __name__ == "__main__":
    composite_bundle(n_tapers = 8)
    

    