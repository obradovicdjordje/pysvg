from pysvg.svg import SVG, Ellipse, Rectangle, Line, Text, Box, Connection, Point

nn_model = [10, 1]
nr = 10

width = 15*nr*1+2*50
height = (10-2)*3*nr+2*50
svg = SVG(width, height)

neuron_style = "fill:#aaffaa;stroke:#000;stroke-width:2px;fill-opacity:0.5"
connection_style = "stroke:#000;stroke-width:1px;stroke-opacity:0.5"


layers=[]
for i, n in enumerate(nn_model):
    layer = []
    layer_h = 2*nr*n+nr*(n-1)
    layer_offy = height/2.0 - layer_h/2.0
    for j in range(n):
        x = 50+15*nr*i
        y = layer_offy+3*nr*j
        el = Ellipse(x, y, nr, nr, style=neuron_style)
        layer.append(el)
        svg.objects.append(el)
    layers.append(layer)

# input layer arrows
for el_00 in layers[0]:
    point = Point(el_00.x-3*nr, el_00.y)
    svg.objects.append(point)
    svg.objects.append(Connection(point, el_00, style=connection_style))

# output layer arrows
for el_00 in layers[-1]:
    point = Point(el_00.x+3*nr, el_00.y)
    svg.objects.append(point)
    svg.objects.append(Connection(el_00, point, style=connection_style))


for i in range(1, len(layers)):
    prev_layer = layers[i-1]
    curr_layer = layers[i]
    for el_0 in prev_layer:
        for el_1 in curr_layer:
            svg.objects.append(Connection(el_0, el_1, style=connection_style))
        
'''
for x in range(5):
    el = Ellipse(100+x*70, 50, 30, 20, style="fill:#ffffff;fill-rule:evenodd;stroke:#ffff00;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1; fill-opacity:0.5")
    svg.objects.append(el)

for x in range(5):
    el = Rectangle(100+x*70, 150, 30, 20, style="fill:#ffffff;fill-rule:evenodd;stroke:#ffff00;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1; fill-opacity:0.5")
    svg.objects.append(el)

svg.objects.append(Line(395, 50, 95, 75))
svg.objects.append(Text(200, 60, 'Evo nesto da napisem', font_size=12))
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
'''


s = svg.display()

print s
