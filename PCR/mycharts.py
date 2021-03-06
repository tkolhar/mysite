from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.lib import colors
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker
from datetime import date, timedelta


class MyLineChartDrawing(Drawing):
    def __init__(self, width=1000, height=500, *args, **kw):
        apply(Drawing.__init__, (self, width, height) + args, kw)
        self.add(LinePlot(), name='chart')

        self.add(String(800, 300, 'Blood pressure'), name='title')

        # set any shapes, fonts, colors you want here.  We'll just
        # set a title font and place the chart within the drawing.
        # pick colors for all the lines, do as many as you need
        self.chart.x = 50
        self.chart.y = 60
        self.chart.width = self.width - 100
        self.chart.height = self.height - 75
        self.chart.lines[0].strokeColor = colors.blue
        self.chart.lines[1].strokeColor = colors.green
        self.chart.lines[2].strokeColor = colors.yellow
        self.chart.lines[3].strokeColor = colors.red
        self.chart.lines[4].strokeColor = colors.black
        self.chart.lines[5].strokeColor = colors.orange
        self.chart.lines[6].strokeColor = colors.cyan
        self.chart.lines[7].strokeColor = colors.magenta
        self.chart.lines[8].strokeColor = colors.brown

        self.chart.fillColor = colors.yellow
        self.title.fontName = 'Times-Roman'
        self.title.fontSize = 18
        self.chart.data = [((0, 50), (100, 100))]
        self.chart.xValueAxis.labels.fontSize = 18
        self.chart.xValueAxis.labels.boxAnchor = 'nw'
        self.chart.xValueAxis.forceZero = 0
        self.chart.xValueAxis.valueMin = 50
        self.chart.xValueAxis.valueMax = 250
        #self.chart.xValueAxis.labelTextFormat = formatter
        #self.chart.xValueAxis.valueSteps = [100, 150, 190,200]
        self.chart.xValueAxis.valueStep = 50
        self.chart.yValueAxis.labels.fontSize = 18
        self.chart.yValueAxis.valueMin = 0
        self.chart.yValueAxis.valueMax = 250
        self.chart.yValueAxis.valueStep = 50
        #self.chart.yValueAxis.valueSteps = [100, 150, 190,200]
      #  self.chart.xValueAxis.gridEnd = 115
        self.chart.xValueAxis.tickDown = 3
      #  self.chart.xValueAxis.visibleGrid = 1
      #  self.chart.yValueAxis.tickLeft = 3
      #  self.chart.yValueAxis.labels.fontName = 'Times-Roman'
      #  self.chart.yValueAxis.labels.fontSize = 12
        self.title.x =  60#self.width / 2
        self.title.y = 8
        self.title.textAnchor = 'middle'
        self.add(Legend(), name='Legend')
        self.Legend.fontName = 'Times-Roman'
        self.Legend.fontSize = 12
        self.Legend.x = self.width
        self.Legend.y = 85
        self.Legend.dxTextSpace = 5
        self.Legend.dy = 5
        self.Legend.dx = 5
        self.Legend.deltay = 5
        self.Legend.alignment = 'right'
        self.add(Label(), name='XLabel')
        self.XLabel.fontName = 'Times-Roman'
        self.XLabel.fontSize = 18
        self.XLabel.x = 450
        self.XLabel.y = 20
        self.XLabel.textAnchor = 'middle'
        # self.XLabel.height = 20
        self.XLabel._text = ""
        self.add(Label(), name='YLabel')
        self.YLabel.fontName = 'Times-Roman'
        self.YLabel.fontSize = 18
        self.YLabel.x = 8
        self.YLabel.y = 250
        self.YLabel.angle = 90
        self.YLabel.textAnchor = 'middle'
        self.YLabel._text = ""
        self.chart.yValueAxis.forceZero = 1
        self.chart.xValueAxis.forceZero = 1

def formatter(val):
    #return val
    #return 'x=%s'%val
    print val
    return (date(2017,1,1) + timedelta(val)).strftime('%Y-%m-%d')
