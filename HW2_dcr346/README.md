# Note to self >> This is not done yet!!!

# PUI2017_dcr346/HW2_dcr346 - README.md

## Assignment #1:

Worked with several students, primarily with Prince and Sarah 
- Learned from Sarah about the Json formatter for Google Chrome which made everything much more clear
- Prince help me to better understand the difference between indexing a list and range(len(list))
- Felt pretty good with navigating through the Json type of data structure
- The code was first writen in Jupyter notebook. After running it in notebook I copied it to emacs and changed the url to suit a py script with the env variables and sys.argv[] > the methode was understandable to me

## Assignment #2:

Found the logic to be quite similar to Assignment#1, worked mostly alone
- Overviewed the script with Sarah and Prince

## Assignment #3:

Worked with several students 
- Before DF was set I refered to a link from NYC Open Data website
- Rebecca showed me how to access Urban Profiler from CUSP's Data Hub

## Extra Credit:

Worked with several students, primarily with Sarah and Unisse 
- Before DF was set I refered to a link from NYC Open Data website
- Figured out how to convert the str dates to date-time format using StackOverFlow
- My selected data included a very large list of dates that didn't plotted properly (super-densed text); I reduced the number of plotted bars by assigning steps of 5 to the df2 values:

```
df2[::5].plot(kind="bar",x='Date', y='Block', rot=45, color="#D7F08F", figsize=(35,10), fontsize=15)
```
