# 538 weather analysis

Using data from the git hub repo https://github.com/fivethirtyeight/data/tree/master/us-weather-history
I downloaded and cleaned the data from the repo.

I combined the base url for the raw csv data "https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/" with a weather station ID. Using a list comprehension to generate a list of URLS to download the data, I read in all 10 wether stations CSV. I examined them using the describe function to see check for extreme values and missing values. I combined these data frames into a list and double check with pd.datframe.isna.sum() to confirm the presence of missing value. one dat frame was mising a year for min_temp_record_year and max_temp_record_year. These values were imputed using the median value for each column resptively. I added a column to each dataframe with the header "city" and the value == to the wetherstation id. 
I double checked to make sure thateach dataframe had 365 values for the new column.  After making sure all datframes were uniform I concatenated them using the pd.concat function, to make a single datframe. This was done to minimize coding errors when generting graphs.

Intially I created a scatterplotmatrix to identify any trends between variables
![Scatterplot matrix](https://github.com/clayton-summitt/weather/blob/main/matrix.png)

The strongest trends are between actual and average temps (min, mean, max). We should not be surprised by this. The distributions of actual mean temp by city looked interesting and from here I examined the distributions of these values more closely with a plotly histogram plot https://chart-studio.plotly.com/~congruency/436 and a violin plot https://chart-studio.plotly.com/~congruency/446/#/ . It appears that the means of all cities in this dataset may not be equal. Later on we will test this with a one way ANOVA.

I then followed up by making [hstogram of average precipitation] (https://chart-studio.plotly.com/~congruency/440/#/ )  and [violin plot of average precipitation](https://chart-studio.plotly.com/~congruency/448/#/). Similar action were taken on actual precip [histogram](https://chart-studio.plotly.com/~congruency/450/#/) and a [violin plot]  (https://chart-studio.plotly.com/~congruency/438/#/). The actual precipitation plot is not very helpful, as the majority of days, there is no rain. With the violin plots we also can not easily spot differences in means of cities. I chose to do a 1 way ANOVA to test if all cities had equal mean rainfall. 

Finally, using a treemap, I visualized the proportion of total rainfall in the dataset, that fell on the respective cities using both the [actual](https://chart-studio.plotly.com/~congruency/444/#/) rainfall and [average](https://chart-studio.plotly.com/~congruency/442/#/) rainfall.
