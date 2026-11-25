# 03_bundle_steering.py

The bundle is steered using a centerline that comes from the center of the bundle. Please see the attached image:

![Bundle steering distances annotated on the rendered eight-channel layout](images/bundle-steering.png)

Setting `spine=0` inside of the routing call will select the 0th waveguide inside the bundle as the waveguide to use as the spine for steering the bundle
