
# condition-reports

[![Build
Status](https://travis-ci.org/marinebon/condition-reports.svg?branch=master)](https://travis-ci.org/marinebon/condition-reports)

This repo is an experiment designed to explore markdown,
jekyll, Rmd, jupyter, travis, and other technologies to 
produce continuously up-to-date reports like those of the
NMS Specific Condition Report Questions (SCRQs).
Details on the CR questions can be found [here](https://sanctuaries.noaa.gov/science/condition/rating.html).

Although unrelated examples may be included, the regional focus of this particular repo is on the Florida Key National Marine Sanctuary.

A similar experiment is ongoing for the Channel Islands over at [ioos-eco/cinms-cr](https://github.com/ioos-eco/cinms-cr).

----------------------------------

To get started look first in `./examples` and compare the files there to the corresponding outputs on the website in [marinebon.github.io/condition-reports/examples](https://marinebon.github.io/condition-reports/examples).

----------------------------------

Within the “pages” directory is an R-markdown (`.Rmd`) file addressing
each of the SCRQs sections from the 2018 CR Guidance document (pg 7).
These sections (and their IMaRS developer usertag) are:

  - Drivers and Pressures (NONE)
  - Water Quality
  - Habitat Resources
  - Living Resources
  - Maritime Archaeological Resources (NONE)

Additional documents in `./examples/` highlight specific features
independed of the content.

Only files with the `.Rmd` extension are checked for code (`R`,
`python`, `bash`) chunks and built into the website. Other files will be
accessible via the static file server, but will not be modified by
travis or jekyll. Files with `.Rmarkdown`, for example are so named to
specifically avoid travis/jekyll because the environment may not yet be
configured to handle the functionality included.

## Relevant links:

  - [2018 Condition Report
    Guidance](https://github.com/USF-IMARS/condition-reports/blob/master/2018-condition-report-guidance.pdf)
  - [markdown
    cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## External Demos & Links

Every link below is powered by the jekyll stack. All demonstrated
functionality should be reproducible. A www groups below are included to
demonstrate different aspects of the stack.

overall website design: \* [feeling
responsive](https://github.com/Phlow/feeling-responsive) \* any on the
[planet jekyll showcase](http://planetjekyll.github.io/showcase/) \*
[leaflet](https://leafletjs.com/)

simplicity: \* this repo is about as simple as it gets, complexity is
not yet added.

interactive graphs/plots/maps: \* [using
plotly](https://davistownsend.github.io/blog/PlotlyBloggingTutorial/) \*
[using flot](http://www.flotcharts.org/)
([source](https://github.com/flot/flot.github.com)) \* [using
D3](http://d3.js.yaml.jekyll.apievangelist.com/bar-chart/)
([source](https://github.com/api-evangelist-tools/d3-js-using-yaml-jekyll))
\* [leaflet](https://leafletjs.com/)

interactive code demonstration notebooks: \* python jupyter notebooks :
[GIS
example](http://nbviewer.jupyter.org/github/mqlaql/geospatial-data/blob/master/Geospatial-Data-with-Python.ipynb)
\* R-markdown : [example
dashboard](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-highcharter/htmlwidgets-highcharter.html)

## The CR Process in Theory

1.  (in development) automatically pull together existing indicator data
2.  expert workshops to identify publications/studies relevant to CRs

<!-- end list -->

  - indicators are constantly rotating
  - lots of customization for each sanctuary
