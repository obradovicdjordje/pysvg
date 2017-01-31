from pysvg.svg import SVG, Ellipse, Rectangle, Line, Text, Box, Connection

svg = SVG(500, 300)
'''
for x in range(5):
    el = Ellipse(100+x*70, 50, 30, 20, style="fill:#ffffff;fill-rule:evenodd;stroke:#ffff00;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1; fill-opacity:0.5")
    svg.objects.append(el)

for x in range(5):
    el = Rectangle(100+x*70, 150, 30, 20, style="fill:#ffffff;fill-rule:evenodd;stroke:#ffff00;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1; fill-opacity:0.5")
    svg.objects.append(el)

svg.objects.append(Line(395, 50, 95, 75))
svg.objects.append(Text(200, 60, 'Evo nesto da napisem', font_size=12))
'''
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

print s

