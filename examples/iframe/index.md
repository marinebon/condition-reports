---
title: Interactive Choropleth Map
---

This example from leaflet.
* [original rendered html](https://leafletjs.com/examples/choropleth/)
* [original source md](https://github.com/Leaflet/Leaflet/blob/master/docs/examples/choropleth/index.md)

# html iframe

<iframe src='https://leafletjs.com/examples/choropleth/example.html'
	width='816'
	height='516'>
</iframe>

# use jekyll (liquid) `include` or `include_relative` shortcut to iframe

{% include_relative iframe_template.html url="https://leafletjs.com/examples/choropleth/example.html" width=816 height=516 %}


# grafana in an iframe
<iframe src="https://snapshot.raintank.io/dashboard-solo/snapshot/y7zwi2bZ7FcoTlB93WN7yWO4aMiz3pZb?from=1493369923321&to=1493377123321&panelId=4" width="650" height="300"></iframe>


# data from erddap in iframe

<iframe src='https://coastwatch.pfeg.noaa.gov/erddap/tabledap/cwwcNDBCMet.htmlTable?station%2Clongitude%2Clatitude%2Ctime%2Cwd%2Cwspd%2Cgst%2Cwvht%2Cdpd%2Capd%2Cmwd%2Cbar%2Catmp%2Cwtmp%2Cdewp%2Cvis%2Cptdy%2Ctide%2Cwspu%2Cwspv&longitude%3E=-82.&longitude%3C=-81&latitude%3E=24.6&latitude%3C=25&time%3E=2018-10-01&time%3C=2018-10-04T17%3A00%3A00Z'
	width='100%'
	height='516'>
</iframe>

# png image from erddap in iframe:

<iframe src='https://coastwatch.pfeg.noaa.gov/erddap/tabledap/cwwcNDBCMet.png?longitude%2Clatitude%2Cwd&time%3E=2018-09-28T00%3A00%3A00Z&time%3C=2018-10-05T00%3A00%3A00Z&longitude%3E=-156&longitude%3C=-50&latitude%3E=-16&latitude%3C=90&.draw=markers&.marker=5%7C5&.color=0x000000&.colorBar=%7C%7C%7C%7C%7C&.land=under&.bgColor=0xffccccff' width="100%" height="300"></iframe>


# leaflet map in iframe
<iframe src='https://leafletjs.com/examples/choropleth/example.html' width='816' height='516'> </iframe>
