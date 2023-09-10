
import sky_area # enables the script to access the coordinates of the different possible SKY_AREAs
from input_file import InputFile
from diagram import Diagram # enables the script to draw the diagram of the SKY_AREA with the proper coordinates
from coord_calc import CoordCalc # how to display the coordinates

f = InputFile('stardata.csv') # retrieves the data from the .csv file

area = sky_area.SKY_AREA_NORTH # selects the sky_area to display
star_data_list = f.get_stars(area)

cc = CoordCalc(star_data_list, area, 500)
cc.process()

d = Diagram('My Star Map', area, star_data_list)
list(map(d.add_curve, cc.calc_curves()))
d.render_svg('star-chart.svg') # the title of the generated svg file
