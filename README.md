# Visualizing the concentration of female science & engineering majors
Educators and researchers have put more of a focus in recent years on bringing women and minority groups into STEM fields. Have their efforts made a measurable impact on the disparity between male and female STEM majors since 2015?

# Data sourcing
The Census Bureau's American Community Survey is conducted annually and measures a wide range of demographics. Among the data collected, the survey asks people who hold a Bachelor's degree what their majors were. The first major listed is treated as the primary major, and then categorized into Science and Engineering, Science and Engineering Related Fields, Business, Education, and Humanities. The following data set (insert Census data set code) records percent of males and females above the age of 25 with a Bachelor's degree who majored in each of the categories listed above. 

# Method and results
We take the percent of males majoring in Science and Engineering and subtract the percent of females majoring in Science and Engineering, and then construct a map of this difference in percentages by U.S. county (see Fig. 1 for the map for the year 2015)

<img width="1809" height="789" alt="image" src="https://github.com/user-attachments/assets/4824747a-3348-464d-97a4-184d45629cc3" />
Fig. 1: (caption here -- this is actually the map for all years combined; fix) Screenshot of Plotly map.

The survey is missing data for many counties (insert percentage of total -- around 25%), so we have a hard time recognizing trends. The next step is to animate the map by year (between 2015 and 2024, excluding 2020) and create a new map for states instead of counties.
