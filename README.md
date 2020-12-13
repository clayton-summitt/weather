# 538 weather analysis

Using data from the git hub repo https://github.com/fivethirtyeight/data/tree/master/us-weather-history
I downloaded and cleaned the data from the repo.

I combined the base url for the raw csv data "https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/" with a weather station ID. Using a list comprehension to generate a list of URLS to download the data, I read in all 10 weather stations CSV. I examined them using the describe function to see check for extreme values and missing values. I combined these data frames into a list and double check with pd.datframe.isna.sum() to confirm the presence of missing value. one dat frame was mising a year for min_temp_record_year and max_temp_record_year. These values were imputed using the median value for each column resptively. I added a column to each dataframe with the header "city" and the value == to the weather station id. 
I double checked to make sure thateach dataframe had 365 values for the new column.  After making sure all datframes were uniform I concatenated them using the pd.concat function, to make a single datframe. This was done to minimize coding errors when generting graphs.

Intially I created a scatterplotmatrix to identify any trends between variables
![Scatterplot matrix](https://github.com/clayton-summitt/weather/blob/main/matrix.png)

The strongest trends are between actual and average temps (min, mean, max). We should not be surprised by this. The distributions of actual mean temp by city looked interesting and from here I examined the distributions of these values more closely with a plotly [histogram plot](https://chart-studio.plotly.com/~congruency/436) and a [violin plot](https://chart-studio.plotly.com/~congruency/446/#/ ). It appears that the means of all cities in this dataset may not be equal. Later on we will test this with a one way ANOVA.

I then followed up by making [hstogram of average precipitation](https://chart-studio.plotly.com/~congruency/440/#/ )  and [violin plot of average precipitation](https://chart-studio.plotly.com/~congruency/448/#/). Similar action were taken on actual precip [histogram](https://chart-studio.plotly.com/~congruency/450/#/) and a [violin plot](https://chart-studio.plotly.com/~congruency/438/#/). The actual precipitation plot is not very helpful, as the majority of days, there is no rain. With the violin plots we also can not easily spot differences in means of cities. I chose to do a 1 way ANOVA to test if all cities had equal mean rainfall. 

Finally, using a treemap, I visualized the proportion of total rainfall in the dataset, that fell on the respective cities using both the [actual](https://chart-studio.plotly.com/~congruency/444/#/) rainfall and [average](https://chart-studio.plotly.com/~congruency/442/#/) rainfall. As these two tree maps are not identical I will us a T-Test to see if the means of actual rainfal is equal to the means of average rainfall for all cities. Given the difference in area between average and 2015 actual precipitation for the following cities; KJAX, KHOU, and KCQT, I will do a T-test to see if the actual  precipitaion mean is diffrent than the average for these cities (each city is tested independently against itself). 


To perform an ANOVA I made a  two seperate dataframes from the columns of interst, actual mean temp and actual precipitation. The results from the ANOVA provides sufficient evidence that we can reject the null hypothesis, that all cities have equal mean temp (F-Statistic=120, p=3.72e-199). I then followed this up with a Tukeys test for honest significant difference to identify which pairwise cities were not equal. The vast majority of cities do not have equal mean temperatures (please see the jupyter notebook for the full breakdown. The cities that did not reject the null are;

City 1| City 2
------------ | -------------
KCQT | KHOU
KCQT | KJAX
KHOU| KJAX
KIND | KMDW
KIND| KNYC
KNYC | KPHL
KNYC| KSEA
KPHL | KSEA

THhe ANOVA on recipitation, with the hypothesis that all cities have equal rain fall also had similar results. with an F-Statistic=7.989, p=8.577e-12, we have sufficient evidence to  reject the null hypothesis that all cities actual precipitation is equal is equal. Conversely the Tuckey test revealed a larger mix of cities having equal precipitation (please see jupyter notebook). 

prior to performing the Ttest, variables were set to columns from dataframes  that were converted to numpy arrays as required by scipy.stats.ttest_ind().
With the T-tests we asked 4 questions: 
* was 2015 equal to the average year for precipitaion?
* was KJAX 2015 actual precipitation is equal to average precipitation?
* was KHOU 2015 actual precipitation is equal to average precipitation?
* was KCQT 2015 actual precipitation is equal to average precipitation?

The results from these T tests are as follows:
* All cities:  

'Test Statistic'| 'p-value'
------------ | -------------
0.480|0.631

* KJAX:  

'Test Statistic'| 'p-value'
------------ | -------------
1.280| 0.201

* KHOU:  

'Test Statistic'| 'p-value'
------------ | -------------
-1.532|0.126

* KCQT:  

'Test Statistic'| 'p-value'
------------ | -------------
2.41|0.016


We have sufficient evidence to reject our null hypothesis that KCQT's 2015 actual precipitation is equal to average precipitation. All other cities we fail to reject the null hypothesis.
