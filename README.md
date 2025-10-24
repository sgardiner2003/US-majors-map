# Visualizing the concentration of female science & engineering majors
For a long time, women have been under-represented in STEM fields. The phenomenon is so well known that it's earned itself a name -- "the leaky pipeline" -- and much research devoted to it (https://pmc.ncbi.nlm.nih.gov/articles/PMC10317101/). Personally, I needed no studies to confirm that it was true, as one of the few women in my math classes throughout high school and college. Educators in my life often mentioned that the lack of representation in STEM fields was a problem that needed solving. But have their efforts, if any, made a measurable impact on the disparity between male and female participation in STEM?

I was thinking about this question as I browsed the datasets available on the Census Bureau website. Fortunately, I found something that might give an answer: the percent of women with Bachelor's degrees who majored in science or engineering fields, by state or county, from 2015 to 2024 (excluding 2020). I'll be exploring this data to get a sense of female participation in STEM geographically and over time. (The project is still in progress.)

# Data sourcing
The Census Bureau's American Community Survey is conducted annually and measures a wide range of demographics. Among the data collected, the survey asks people who hold a Bachelor's degree what their majors were. The first major listed is treated as the primary major, and then categorized into Science and Engineering, Science and Engineering Related Fields, Business, Education, and Humanities. The data set I've used (found by searching S1502 on the Census Bureau data site; https://www.census.gov/data.html) records, among other things, the percent of males and females above the age of 25 with a Bachelor's degree who majored in each of the categories listed above.

# Method and results
I took the percent of males majoring in Science and Engineering and subtracted the percent of females majoring in Science and Engineering, and then constructed a map of this difference in percentages by U.S. county (see Fig. 1 for the 2015 map).

<img width="1809" height="789" alt="image" src="https://github.com/user-attachments/assets/4824747a-3348-464d-97a4-184d45629cc3" />
Fig. 1: Screenshot of Plotly map.

The survey is missing data for many counties (about 21% of them), so we have a hard time recognizing trends. The same data is available at the state level, and is not missing data for any of the variables I'm using, so that map is nicer to look at.

<img width="896" height="460" alt="image" src="https://github.com/user-attachments/assets/acd90be9-b3f2-49d5-95a0-185a00c5c724" />
Fig. 2: A much less patchy map of the U.S.

This map isn't missing holes like the county map is, but I'm wary of how it might be misleading given the lack of data at the county level. I'm curious to know if the state-level data is more complete than the county-level, or if graphing by state just extrapolates data from the few counties that we do have data for. If so, this map would be an inaccurate representation of each state as a whole. The only advantage would be the ease and clarity of viewing the data physically, since the county map is too dispersed to notice any regional trends. The state map might allow that at the cost of being reductive and glossing over the data's complexity.

At this point I've added a slider for the years, but I've found it's not very helpful given how small our year range is (2015-2024, excluding 2020). A line graph to show overall change for each state over the years will be my next step. This would also allow me to visually depict the margin of error that comes with the data, courtesy of the Census (equivalent to a 90% confidence interval).

More coming soon!

# Line Graphs

<img width="1854" height="851" alt="image" src="https://github.com/user-attachments/assets/0ac690bb-75ad-4367-875a-0f5679343cf1" />
