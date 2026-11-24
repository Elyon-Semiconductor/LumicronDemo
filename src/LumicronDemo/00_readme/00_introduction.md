# Welcome to Lumicron!

Thanks for being here with us! This brief introduction will give you a preview into what you can expect in this demo project, as well as what topics we will be covering.
This project is meant to be a living example library and documentation for Lumicron. We encourage you to have this document open side by side with your Lumicron workspace 
so you can easily follow along and partake in some exercises

## Table of Contents
* [1. Place](#1-place)
* [2. Route](#2-route)

## 1. Place

Placement in Lumicron uses a single Place command with a chain of .functions() as modifiers to transform your placement. Chain order in placement matters.
Common modifiers include:

- `.at()`: to specify a place coordinate. This typically is the first chain in you Place chain, and it takes in a hard (x, y) coordinate or port.
- `.using()`: to specify the anchor of the instance you are using as the placement center. Arguments include bbox anchors like "W", "NE", "SW", and a port of the instance you are trying to place.
- `.relative_to()`: to specify an anchor or port or world coordinate to use as reference for your placement.
- `.rotate_by()`: to specify the rotation of your instance. This will rotate the component around its own origin. It takes degrees for rotation.
- `.move_by()`: to specify a dx and/or dy movement for your component after its placement
- `.above()`, `below()`, `left_of()`, `right_of()`: to place your instance above, below, left of, right of another instance. It will align your instance anchors with the target in the following way "S" to "N", "N" to "S", "E" to "W", and "W" to "E"

## 2. route

Routing in Lumicron also follows the same convention as Place; with a single Route command that uses a chain of routing specific .functions() to create your routes. Chain order in routing matters.
Common modifiers include:

- `.go()`: to specify cardinal directions for manhattan routes. You can chain multiple `.go()` modifiers to steer the route, almost like giving the router directions.
