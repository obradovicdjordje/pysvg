from util import intersection
import numpy as np

class SVG():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []

    def display(self):
        stt = ""
        for obj in self.objects:
            stt += obj.draw()
        nested_svg="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg id="svg2" xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}" version="1.0">       
    <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L9,3 z" fill="#000" />
    </marker>
    </defs>
    <svg x="0">
    {2}
    </svg>
</svg>""".format(self.width, self.height, stt)
        return nested_svg

class Line():
    def __init__(self, x1, y1, x2, y2, style=None):
        if style != None:
            self.style = style
        else:
            self.style = "stroke:#000000;stroke-width:2px;"
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        ret = """<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" style="{4}" marker-end="url(#arrow)"/>""".format(self.x1, self.y1, self.x2, self.y2, self.style)
        return ret

class Ellipse():
    def __init__(self, x, y, rx, ry, style=None):
        if style != None:
            self.style = style
        else:
            self.style = "fill:#ff0000;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry

    def center_point(self):
        return self.x, self.y

    def border_point(self, xt, yt):
        def inside_ellipse(x, y, xc, yc, rx, ry):
            d = (x-xc)**2/(rx**2)+(y-yc)**2/(ry**2)
            if d<=1:
                return True
            else:
                return False
        A = np.array([xt, yt])
        B = np.array([self.x, self.y])
        u1 = 0
        u2 = 1

        for it in range(100):
            d = u2-u1
            u = (u2+u1)/2.0
            T = A+u*(B-A)
            if inside_ellipse(T[0], T[1], self.x, self.y, self.rx, self.ry):
                u2 = u        
            else:
                u1 = u
            if d<0.01:
                x = T[0]
                y = T[1]
                return x, y

    def draw(self):
        ret = """
            <ellipse
               style="{4}"
               cx="{0}"
               cy="{1}"
               rx="{2}"
               ry="{3}" />
        """.format(self.x, self.y, self.rx, self.ry, self.style)
        return ret

class Text():
    def __init__(self, x, y, text, font='Verdana', font_size='12'):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.font_size = font_size

    def draw(self):
        ret = """
            <text x="{0}" y="{1}" font-family="{3}" font-size="{4}">
            {2}
            </text>""".format(self.x, self.y, self.text, self.font, self.font_size)
        return ret

class Rectangle():
    def __init__(self, x, y, w, h, style=None):
        if style != None:
            self.style = style
        else:
            self.style = "fill:#ff0000;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        ret = """
            <rect
               style="{4}"
               x="{0}"
               y="{1}"
               height="{2}"
               width="{3}" />
        """.format(self.x, self.y, self.w, self.h, self.style)
        return ret

class Box():
    def __init__(self, x, y, w, h, style=None, text=None):
        if style != None:
            self.style = style
        else:
            self.style = "fill:#ff0000;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def center_point(self):
        return self.x+self.w/2.0, self.y+self.h/2.0

    def border_point(self, xt, yt):
        x1 = self.x+self.w/2.0
        y1 = self.y+self.h/2.0        
        ac = np.array([x1, y1])
        bc = np.array([xt, yt])
        lines = []
        lines.append([[self.x,   self.y],[ self.x+self.w, self.y]])
        lines.append([[self.x+self.w, self.y],[ self.x+self.w, self.y+self.h]])
        lines.append([[self.x, self.y+self.h],[ self.x+self.w, self.y+self.h]])
        lines.append([[self.x, self.y],[ self.x, self.y+self.h]])
        for e in lines:
            t1 = np.array(e[0])
            t2 = np.array(e[1])
            rez = intersection(ac, bc, t1, t2)
            if(rez != None):
                p, u, v = rez
                if u>=0 and u<=1 and v>=0 and v<=1:
                    tc = t1+0.5*(t2-t1)
                    x1 = p[0]
                    y1 = p[1]
                    #self.x1 = tc[0]
                    #self.y1 = tc[1]
                    return x1, y1        

    def draw(self):
        rec = """
            <svg x="{0}" y="{1}" width="{2}" height="{3}">
              <rect x="0" y="0" width="{2}" height="{3}" stroke="red" stroke-width="3px" fill="white"/>
              <text x="50%" y="50%" alignment-baseline="middle" text-anchor="middle" font-family="Verdana">{4}</text>    
            </svg>
        """.format(self.x, self.y, self.w, self.h, self.text)
        return rec

class Connection():
    def __init__(self, a, b, style=None):
        if style != None:
            self.style = style
        else:
            self.style = "stroke:#000000;stroke-width:2px;"

        self.x1, self.y1 = a.center_point()
        self.x2, self.y2 = b.center_point()

        self.x1, self.y1 = a.border_point(self.x2, self.y2)
        self.x2, self.y2 = b.border_point(self.x1, self.y1)

    def draw(self):
        ret = """<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" style="{4}" marker-end="url(#arrow)"/>""".format(self.x1, self.y1, self.x2, self.y2, self.style)
        return ret
