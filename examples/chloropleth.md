---
layout: tutorial_v2
title: Interactive Choropleth Map
---

This example from leaflet. 
* [original rendered html](https://leafletjs.com/examples/choropleth/)
* [original source md](https://github.com/Leaflet/Leaflet/blob/master/docs/examples/choropleth/index.md)

## Interactive Choropleth Map

This is a case study of creating a colorful interactive [choropleth map](http://en.wikipedia.org/wiki/Choropleth_map) of US States Population Density with the help of [GeoJSON](../geojson/) and some [custom controls](/reference.html#control) (that will hopefully convince all the remaining major news and government websites that do not use Leaflet yet to start doing so).

The tutorial was inspired by the [Texas Tribune US Senate Runoff Results map](http://www.texastribune.org/library/data/us-senate-runoff-results-map/) (also powered by Leaflet), created by [Ryan Murphy](http://www.texastribune.org/about/staff/ryan-murphy/).

{% include_relative frame.html url="example.html" width=816 height=516 %}

### Data Source

We'll be creating a visualization of population density per US state. As the amount of data (state shapes and the density value for each state) is not very big, the most convenient and simple way to store and then display it is [GeoJSON](../geojson/).

Each feature of our GeoJSON data ([us-states.js](us-states.js)) will look like this:

	{
		"type": "Feature",
		"properties": {
			"name": "Alabama",
			"density": 94.65
		},
		"geometry": ...
		...
	}

The GeoJSON with state shapes was kindly shared by [Mike Bostock](http://bost.ocks.org/mike) of [D3](http://d3js.org/) fame, extended with density values from [this Wikipedia article](http://en.wikipedia.org/wiki/List_of_U.S._states_by_population_density) based on July 1st 2011 data from [US Census Bureau](http://www.census.gov/) and assigned to `statesData` JS variable.
