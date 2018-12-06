import mapnik


def mapnik_plot(shp_file):
    m = mapnik.Map(600, 300)
    m.background = mapnik.Color('steelblue')
    s = mapnik.Style()
    r = mapnik.Rule()
    # polygon_symbolizer = mapnik.PolygonSymbolizer()
    # polygon_symbolizer.fill = mapnik.Color('#f2eff9')
    # r.symbols.append(polygon_symbolizer)

    line_symbolizer = mapnik.LineSymbolizer()
    line_symbolizer.stroke = mapnik.Color('rgb(100%,100%,100%)')
    line_symbolizer.stroke_width = 3.0
    r.symbols.append(line_symbolizer)
    s.rules.append(r)
    m.append_style('My Style', s)
    ds = mapnik.Shapefile(file=shp_file)
    layer = mapnik.Layer('world')
    layer.datasource = ds
    layer.styles.append('My Style')
    m.layers.append(layer)
    m.zoom_all()
    # TODO: show here rather than save to file:
    # mapnik.render_`to_file(m, 'world.png', 'png')
