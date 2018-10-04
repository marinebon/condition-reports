---
title: Interactive Choropleth Map
---

This example from leaflet. 
* [original rendered html](https://leafletjs.com/examples/choropleth/)
* [original source md](https://github.com/Leaflet/Leaflet/blob/master/docs/examples/choropleth/index.md)



# grafana in an iframe
<iframe src="http://grafana.marine.usf.edu:3000/dashboard-solo/db/fl_keys_dash?orgId=2&panelId=3&from=1475611938029&to=1538683938030&var-product=chlor_a&var-roi=fgbnms&var-weeks_ago=4&var-weeks_ago=3&var-weeks_ago=2&var-weeks_ago=1&var-weeks_ago=0&var-area=carbon&var-station=08030500&var-station=08041780" width="450" height="200" frameborder="0"></iframe>


# use raw html to create iframe

<iframe src='https://github.com/USF-IMARS/condition-reports/blob/master/data/imars-logo.gif'
	width='100%'
	height='516'>
</iframe>


# use jekyll (liquid) `include` or `include_relative` shortcut to iframe
 
{% include_relative iframe_template.html url="../data/" width=816 height=516 %}


<iframe src='https://leafletjs.com/examples/choropleth/example.html'
	width='816'
	height='516'>
</iframe>

# data .csv from erddap in iframe 

<iframe src='http://imars-physalis.marine.usf.edu:8080/erddap/tabledap/cwwcNDBCMet.csv?station%2Clongitude%2Clatitude%2Ctime%2Cwd%2Cwspd%2Cgst%2Cwvht%2Cdpd%2Capd%2Cmwd%2Cbar%2Catmp%2Cwtmp%2Cdewp%2Cvis%2Cptdy%2Ctide%2Cwspu%2Cwspv&longitude%3E=-82.733&longitude%3C=-80.49&latitude%3E=24.6&latitude%3C=25.254&time%3E=2018-04-01&time%3C=2018-10-04T17%3A00%3A00Z'
	width='816'
	height='516'>
</iframe>

# png image from erddap in iframe:

<iframe src='https://coastwatch.pfeg.noaa.gov/erddap/tabledap/cwwcNDBCMet.png?longitude%2Clatitude%2Cwd&time%3E=2018-09-28T00%3A00%3A00Z&time%3C=2018-10-05T00%3A00%3A00Z&longitude%3E=-156&longitude%3C=-50&latitude%3E=-16&latitude%3C=90&.draw=markers&.marker=5%7C5&.color=0x000000&.colorBar=%7C%7C%7C%7C%7C&.land=under&.bgColor=0xffccccff'></iframe>

# png image markdown

![the hover text]( http://imars-physalis.marine.usf.edu:8080/erddap/tabledap/cwwcNDBCMet.transparentPng?longitude,latitude,wd&time%3E=2018-09-28T00%3A00%3A00Z&time%3C=2018-10-05T00%3A00%3A00Z&longitude%3E=-156&longitude%3C=-50&latitude%3E=-16&latitude%3C=90&.draw=markers&.marker=5%7C5&.color=0x000000&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff )

![other hover text]( /data/imars-logo.gif )

![other other hover](https://github.com/USF-IMARS/condition-reports/blob/master/data/imars-logo.gif)

# xss err
<iframe src='https://github.com/USF-IMARS/condition-reports'
	width='100%'
	height='516'>
</iframe>
