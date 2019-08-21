
NOTE: to embed an image, it **must** first be hosted somewhere. URLs to
externally hosted images can be used, but images can also be added to
github directly. For these examples the image has been uploaded in this
repository’s
[assets/images](https://github.com/marinebon/condition-reports/tree/master/assets/images)
directory.

# images in html

<img src="https://github.com/USF-IMARS/condition-reports/blob/master/assets/images/imars-logo.gif?raw=true">

# images in markdown

## full url

![long full
url](https://github.com/USF-IMARS/condition-reports/blob/master/assets/images/imars-logo.gif?raw=true)

## shorter local url

![short local url](../assets/images/imars-logo.gif)

# “Dynamic” images from a data API

## ERDDAP

![the hover
text](https://coastwatch.pfeg.noaa.gov/erddap/tabledap/cwwcNDBCMet.png?longitude%2Clatitude%2Cwd&time%3E=2018-09-28T00%3A00%3A00Z&time%3C=2018-10-05T00%3A00%3A00Z&longitude%3E=-156&longitude%3C=-50&latitude%3E=-16&latitude%3C=90&.draw=markers&.marker=5%7C5&.color=0x000000&.colorBar=%7C%7C%7C%7C%7C&.land=under&.bgColor=0xffccccff)

1.  browser requests a URL (using RESTful API )
2.  ERDDAP server makes the png & sends it
3.  browser displays in the same way as a static image (image only
    updates on page refresh)
