---
title: Interactive Choropleth Map
---

This example from leaflet. 
* [original rendered html](https://leafletjs.com/examples/choropleth/)
* [original source md](https://github.com/Leaflet/Leaflet/blob/master/docs/examples/choropleth/index.md)


## use raw html to create iframe

<iframe src='chloropleth_example_html.html'
	width='816'
	height='516'>
</iframe>


## use jekyll (liquid) `include` or `include_relative`
 
{% include_relative iframe_template.html url="chloropleth_example_html.html" width=816 height=516 %}

## can do the same with external pages

<iframe src='https://leafletjs.com/examples/choropleth/example.html'
	width='816'
	height='516'>
</iframe>
