## pySql 


Python package for block diagram generator. Generated image is in SVG format. 
[img](test.svg)

```python
w = 100
h = 70
box1 = Box(50, 50, w, h, text='Prvi box')
box2 = Box(150, 150, w, h, text='Drugi box')
box3 = Box(300, 150, w, h, text='Treci box')
el1 = Ellipse(200, 50, 30, 20, style="fill:#ffffff;stroke:#000;stroke-width:2px;fill-opacity:0.5")
el2 = Ellipse(300, 50, 40, 30, style="fill:#eee;stroke:#0f0;stroke-width:1px;fill-opacity:0.9")

svg.objects.append(box1)
svg.objects.append(box2)
svg.objects.append(box3)
svg.objects.append(el1)
svg.objects.append(el2)

svg.objects.append(Connection(box1, box2))
svg.objects.append(Connection(box2, box3))
svg.objects.append(Connection(box3, el1))
svg.objects.append(Connection(el2, box3))


s = svg.display()
```
