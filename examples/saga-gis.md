[SAGA-GIS](http://www.saga-gis.org/) examples from 2018-12 [OGTA Training Course](http://www.ocean-partners.org/otga-training-course-ocean-data-management-researchers).

The example area of interest (AoI) here is Liberia, defined as:
    - lat_n +9
    - lat_s -6
    - lon_e -23
    - lon_w -3

This is an example of how to use SAGA GIS via `saga_cmd` (bash cmd used via python `subprocess`) to process data.
The `.shp` output(s) are then displayed using [mapnik](https://github.com/mapnik/mapnik).
Some alternative display options are enumerated [here](https://gis.stackexchange.com/a/62652/107752).

## Project Dir Explaination
The expected directory structure here: (TODO: this might not be essential within these examples)
```
PROJECTS
  LIBERIA - Project files for this area
     DATA - information about datasets
        BASEMAP
            BORDERS - Shapes for mapping
            RELIEF- Bathymetry and topography
        OCEAN
            WOD- World Ocean Database
            WOA- World Ocean Atlas
            [OTHER SOURCES] - Separate folders identified by acronyms are optional here depending on your preferences
     PRODUCTS - Files created by the following main programs
      IDV - Maps and syntheses made by Integrated Data Viewer: synthesis program for many operational datasets and some GIS objects
      ODV - Collections and their products made with Ocean Data View; our principal ocean station data management, analysis and display tool
          COLLECTIONS - Individual collections of data by data type, area or other original selection criteria
          IMAGES - Saved images of graphics

          INTERPOLATIONS - XYZ data triplets exported from ODV's "surface mode" analyses; could also be called grids, because they are derived from grid-like interpolation schemes

          SUBSETS - Spreadsheets of data taken from larger collections, based on temporal, spatial or other station or sample criteria; can also be a completely new collection extracted from the parent collection

          TIMESERIES - Data analyses based mainly on data/time, not geographic location

      SAGA - Grids and vector products made by our "workhorse" public domain GIS program
              AUXILIARY - Saved settings (properties files) for the display of shapes or grids, and other similar helper files
              GEOIMAGES - Geo-referenced images, using either world files or KML/KMZ for positioning; includes also TIFF grid rasters (for WMS use only)
              GRIDS - grids in Saga format, including template grids
              PROJECTS - A special sort of file that contains lists of objects to place in one map, including the display properties of the objects
              TABLES - tabular data from within shapes, and also created alongside them for display management
              VECTORS - points, lines, contours, polygons, graticules, wind arrows, current arrows; all as either ESRI shapes or Google KML/KMZ

# Data Sources:
1. World Borders from [thematicMapping.org](http://thematicmapping.org/downloads/world_borders.php)
2. World EEZ v10 Marine Regions from [marineRegions.org](http://www.marineregions.org/downloads.php):
    * Claus S., De Hauwere N., Vanhoorne B., Souza Dias F., Oset García P., Schepers L., Hernandez F., and Mees J. (Flanders Marine Institute) (2018). MarineRegions.org. Accessed at http://www.marineregions.org on 2018-12-04.
3. Modis Aqua Chl Monthly Anomalies from [GMIS](http://gmis.jrc.ec.europa.eu/satellite/4km/anomalies/bz2/GMIS_M_ANO_CHLA_01_2003.nc.bz2
)
    * [gmis mapper url](http://gmis.jrc.ec.europa.eu/index_fullscreen.php?xml_selection=default4km&variable_selection=44&time_selection=YY&month_selection=12&year_selection=2017&extent_selection=-92.33 -96.08 141.77 83.92), [geotiff](http://gmis.jrc.ec.europa.eu/index_fullscreen.php?xml_selection=default4km&variable_selection=44&time_selection=YY&month_selection=07&year_selection=2017&extent_selection=-92.33 -96.08 141.77 83.92), [NetCDF](http://mcc.jrc.ec.europa.eu/gmis/satellite/4km/anomalies/bz2/GMIS_A_ANO_CHLA_07_2017.nc.bz2), & WMS available



TODO: must download data first (or load from remote within python)

```{python}
#!/usr/bin/env python
import subprocess
import mapnik
import os.path


class input_file(object):
    WORLD_EEZ_POLY = "DATA/BASEMAP/BORDERS/eez/eez_v10.shp"
    WORLD_EEZ_LINE = "DATA/BASEMAP/BORDERS/eez/eez_boundaries_v10.shp"

    LIBERIA_FRAME_POLY = "PRODUCTS/SAGA/VECTORS/frame_liberia_poly.shp"
    
    LIBERIA_FRAME_LINE = "PRODUCTS/SAGA/VECTORS/frame_liberia_line.shp"
    @staticmethod
    def list_all():
        return [
            getattr(input_file, a) for a in dir(input_file)
            if not a.startswith('_') and
            not callable(getattr(input_file, a))
        ]

# intermediate data:
LIBERIA_EEZ_LINE = "PRODUCTS/SAGA/VECTORS/liberia_eez.shp"

for infile in input_file.list_all():
    if(not os.path.isfile(infile)):
        raise ValueError("Missing Input file:\n\t{}".format(infile))

cmd = [
    'saga_cmd', 'shapes_lines', 'Line-Polygon Intersection',
    '-LINES', input_file.WORLD_EEZ_LINE,
    '-POLYGONS', input_file.LIBERIA_FRAME_POLY,
    '-INTERSECT', LIBERIA_EEZ_LINE
]
print("running bash command:\n\t{}".format(subprocess.list2cmdline(cmd)))
subprocess.check_output(cmd)

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
ds = mapnik.Shapefile(file=LIBERIA_EEZ_LINE)
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
# TODO: show here rather than save to file:
# mapnik.render_to_file(m, 'world.png', 'png')
```

# TODO:
1. compare EEZ & [Longhurst Province](http://www.marineregions.org/downloads.php) Biodiversity "health" (as defined by @bbest's indicies)
2. play with [saga-py](https://github.com/radical-cybertools/saga-python)
3. use more of chl_a anom [@gmis](http://mcc.jrc.ec.europa.eu/emis/)
4. can skip over saving intermediate products in python by using data in RAM (see [here](https://sourceforge.net/p/saga-gis/wiki/Creating%20Python%20scripts/)).

