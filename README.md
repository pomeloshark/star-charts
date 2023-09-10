# Star Charts

This Python script will generate SVG star charts, like the ones shown below:

<img src="https://codebox.net/assets/images/star-charts-with-python/orion.png" height="480px" width="480px" alt="Star Chart showing Orion" /><br>
<sup>The constellation Orion, showing stars down to magnitude 8 [original SVG](https://codebox.net/assets/images/star-charts-with-python/orion.svg)</sup>

The script reads data about the position and brightness of stars from a CSV (comma-separated value) file like [this one](https://raw.githubusercontent.com/codebox/star-charts/master/stardata.csv).
Each row in the CSV file contains information about a single star in 4 columns, as follows:

+ **Right ascension**: the star's angular distance eastward from the vernal equinox (0 to 24)
+ **Declination**: the star's angular distance northward from the celestial equator (-90 to +90)
+ **Magnitude**: the star's brightness
+ **Label**: an optional field used to add labels to stars (see the Greek letters in the example chart above)

For example:

```
5.91937636,+76.86957095, 8.07
5.91952477,+07.40703634, 0.45,α
5.92011402,+61.86673905, 8.60
5.92045102,-73.15075170, 7.72
```

The area to be covered by the chart is specified using a **SkyArea** object, which must be referenced by the `main.py` file. A few pre-defined areas are included, such as complete northern and southern sky maps:

<img src="https://codebox.net/assets/images/star-charts-with-python/northern_sky.png" height="420px" width="420px" class="" alt="Star Chart showing the northern sky" />
<img src="https://codebox.net/assets/images/star-charts-with-python/southern_sky.png" height="420px" width="420px" class="" alt="Star Chart showing the southern sky" />

<sup>Maps of the Northern and Southern skies, showing stars down to magnitude 7 (original SVGs: [North](https://codebox.net/assets/images/star-charts-with-python/northern_sky.svg) and [South](https://codebox.net/assets/images/star-charts-with-python/southern_sky.svg)</sup>

## About the code

+ `coord_calc.py` calculates the coordinates on a 2d circular surface
+ `diagram.py` outputs the image
+ `input_file.py` processes the data in stardata.csv
+ `sky_area.py` defines the area of the sky to display on the map
+ `star_data.py`
+ `svg.py`
+ `main.py` the main script that imports all of the above and then runs

The script is run by simply executing the main.py file, as follows:

```
python main.py
```

The SVG file will be created in the current directory, and will be named `star-chart.svg` or whatever you name it in main.py.

Please note that the script is designed to be run using Python 3; it will not run correctly with Python 2.
