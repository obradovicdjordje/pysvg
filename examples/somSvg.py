from pysvg.svg import SVG, Ellipse, Rectangle, Line, Text, Box, Connection, Point

size = 10

nr = 10
d = 50
margin = 25

width = d*(size-1)+2*margin
height = d*(size-1)+2*margin

svg = SVG(width, height)

neuron_style = "fill:#aaffaa;stroke:#000;stroke-width:2px;fill-opacity:0.5"
connection_style = "stroke:#000;stroke-width:1px;stroke-opacity:0.5"


layers=[]
for i in range(size):
    x = margin+d*i
    for j in range(size):
        y = margin+d*j
        el = Ellipse(x, y, nr, nr, style=neuron_style)
        svg.objects.append(el)

win_style = "fill:#0000ff;stroke:#f00;stroke-width:2px;fill-opacity:0.5"
win_i = 6
win_j = 6
x = margin+d*win_i
y = margin+d*win_j
el = Ellipse(x, y, nr, nr, style=win_style)
svg.objects.append(el)

g_style = "stroke:#000;stroke-width:1px;fill-opacity:0.0"
x = margin+d*win_i
y = margin+d*win_j
for r in range(4):
    el = Ellipse(x, y, 0.5*r*d, 0.5*r*d, style=g_style)
    svg.objects.append(el)

s = svg.display()

print s
