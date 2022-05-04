# -*- coding: utf-8 -*-
"""
#              Author : Melvin M. Flores
#          Student ID : 30352985
#        Date Created : 23 June 2019
#        Program Name : BiorythmCycleGenerator.py
# Program Description : Biorythm are biological cycles in 3 various domains:
#                     : Physical, Intellectual and Emotional 	
#                     : This program generates the 3 biological cycles,
#                     : asking the user to input the birthday and target date.
#          Input File : None.txt
#         Output File : Biorythm.pdf
"""
# imported for date processing
from datetime import date

# imported for mathematical, figure, plot and date processing
import matplotlib.dates

# imported for savefigure processing
import matplotlib.pyplot as plt

# imported for figure and plot processing
from pylab import plot, grid, legend, xlabel, ylabel, title, show, figure
#from pylab import *

# imported for number processing
from numpy import array, sin, pi

# ask user to input birthday
print ("Please input a birthday:")
birth_day   = int(input("Day of birth(dd)?"))
birth_month = int(input("Month of birth(mm)?"))
birth_year  = int(input("Year of birth(ccyy)?"))

# transform birth date to a date format
birth_date = date(birth_year,birth_month,birth_day)

# transform birth date to its ordinal value
birth_date_ordinal = birth_date.toordinal()

# ask user to input target date
print ("Please input a target date.")
target_day   = int(input("Target Day (dd): "))
target_month = int(input("Target Month(mm): "))
target_year  = int(input("Target Year(ccyy): "))

# transform target date to a date format
target_date = date(target_year,target_month,target_day)

# transform target date to its ordinal value
target_date_ordinal = target_date.toordinal()

# transform current date to its ordinal value
current_date_ordinal = date.today().toordinal()

# calculate number of days alive
number_of_days_alive = current_date_ordinal - birth_date_ordinal

# spread date array range of 31 days, so that the Intellectual Cycle 
# is displayed as a whole cycle
spread_date_ordinal = array(range(target_date_ordinal-17, target_date_ordinal+17)) 

y = (sin(2*pi*(spread_date_ordinal - birth_date_ordinal)/23),  # Physical cycle
     sin(2*pi*(spread_date_ordinal - birth_date_ordinal)/28),  # Emotional cycle
     sin(2*pi*(spread_date_ordinal - birth_date_ordinal)/33))  # Intellectual cycle  

# converting ordinals to date
x_axis = []
for x_axis_values in spread_date_ordinal:
    x_axis.append(date.fromordinal(x_axis_values))

# use matplotlib figure function
fig = figure(figsize=(20,10))

# use current axes function
ax = fig.gca()

# use plot function
# set color and linewidth of biorythm cycles
plot(label,y[0], color="red", linewidth=5, alpha=1.0)
plot(label,y[1], color="blue", linewidth=10, alpha=1.5)
plot(label,y[2], color="green", linewidth=15, alpha=2.0)

# enable grid-lines
grid(True)
    
# use legend function
legend(['Physical', 'Emotional', 'Intellectual'])

# display dates on the x-axis, format is dd/Mon
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))

# display x and y labels
xlabel('Phase')
ylabel('Amplitude')

# display title
title_string="Biorythm cycles \n\n Birthday:" + str(birth_date) +  "     No. Of Days Alive:" + str(number_of_days_alive) + "     Target Date:" + str(target_date)
title(title_string)

# save the generated biorythm cycle figure as pdf file 
plt.savefig("Biorythm.pdf")

# display the figure
show()
