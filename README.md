# 538 weather analysis

Using data from the git hub repo https://github.com/fivethirtyeight/data/tree/master/us-weather-history
I downloaded and cleaned the data from the repo.

I combined the base url for the raw csv data "https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/" with a weather station ID. Using a list comprehension to generate a list of URLS to download the data, I read in all 10 wether stations CSV. I examined them using the describe function to see check for extreme values and missing values. I combined these data frames into a list and double check with pd.datframe.isna.sum() to confirm the presence of missing value. one dat frame was mising a year for min_temp_record_year and max_temp_record_year. These values were imputed using the median value for each column resptively. I added a column to each dataframe with the header "city" and the value == to the wetherstation id. 
I double checked to make sure thateach dataframe had 365 values for the new column.  After making sure all datframes were uniform I concatenated them using the pd.concat function, to make a single datframe. This was done to minimize coding errors when generting graphs.

Intially I created a scatterplotmatrix to identify any trends between variables
![Scatterplot matrix](https://github.com/clayton-summitt/weather/blob/main/matrix.png)

The strongest trends are between actual and average temps (min, mean, max). We should not be surprised by this. The distributions of actual mean temp by city looked interesting and from here I examined the distributions of these values more closely with a plotly [histogram plot](https://chart-studio.plotly.com/~congruency/436) and a [violin plot](https://chart-studio.plotly.com/~congruency/446/#/ ). It appears that the means of all cities in this dataset may not be equal. Later on we will test this with a one way ANOVA.

I then followed up by making [hstogram of average precipitation](https://chart-studio.plotly.com/~congruency/440/#/ )  and [violin plot of average precipitation](https://chart-studio.plotly.com/~congruency/448/#/). Similar action were taken on actual precip [histogram](https://chart-studio.plotly.com/~congruency/450/#/) and a [violin plot](https://chart-studio.plotly.com/~congruency/438/#/). The actual precipitation plot is not very helpful, as the majority of days, there is no rain. With the violin plots we also can not easily spot differences in means of cities. I chose to do a 1 way ANOVA to test if all cities had equal mean rainfall. 

Finally, using a treemap, I visualized the proportion of total rainfall in the dataset, that fell on the respective cities using both the [actual](https://chart-studio.plotly.com/~congruency/444/#/) rainfall and [average](https://chart-studio.plotly.com/~congruency/442/#/) rainfall. As these two tree maps are not identical I will us a T-Test to see if the means of actual rainfal is equal to the means of average rainfall for all cities. Given the difference in area between average and 2015 actual precipitation for the following cities; KJAX, KHOU, and KCQT, I will do a T-test to see if the actual  precipitaion mean is diffrent than the average for these cities (each city is tested independently against itself). 


To perform an ANOVA I made a  two seperate dataframes from the columns of interst, actual mean temp and actual precipitation. The results from the ANOVA provides sufficient evidence that we can reject the null hypothesis, that all cities have equal mean temp (F-Statistic=120, p=3.72e-199). I then followed this up with a tuckeys test for honest significant difference to identify which cities were not equal.

Multiple Comparison of Means - Tukey HSD, FWER=0.05  
======================================================
group1 group2 meandiff p-adj   lower    upper   reject
------------------------------------------------------
  KCLT   KCQT   7.5123  0.001    3.826  11.1987   True
  KCLT   KHOU   8.6658  0.001   4.9794  12.3521   True
  KCLT   KIND  -9.6575  0.001 -13.3439  -5.9712   True
  KCLT   KJAX   7.9288  0.001   4.2424  11.6151   True
  KCLT   KMDW    -10.0  0.001 -13.6864  -6.3136   True
  KCLT   KNYC  -6.3123  0.001  -9.9987   -2.626   True
  KCLT   KPHL  -5.1644  0.001  -8.8508   -1.478   True
  KCLT   KPHX  16.2712  0.001  12.5849  19.9576   True
  KCLT   KSEA  -4.5068 0.0044  -8.1932  -0.8205   True
  KCQT   KHOU   1.1534    0.9   -2.533   4.8398  False
  KCQT   KIND -17.1699  0.001 -20.8562 -13.4835   True
  KCQT   KJAX   0.4164    0.9  -3.2699   4.1028  False
  KCQT   KMDW -17.5123  0.001 -21.1987  -13.826   True
  KCQT   KNYC -13.8247  0.001  -17.511 -10.1383   True
  KCQT   KPHL -12.6767  0.001 -16.3631  -8.9903   True
  KCQT   KPHX   8.7589  0.001   5.0725  12.4453   True
  KCQT   KSEA -12.0192  0.001 -15.7056  -8.3328   True
  KHOU   KIND -18.3233  0.001 -22.0097 -14.6369   True
  KHOU   KJAX   -0.737    0.9  -4.4234   2.9494  False
  KHOU   KMDW -18.6658  0.001 -22.3521 -14.9794   True
  KHOU   KNYC -14.9781  0.001 -18.6645 -11.2917   True
  KHOU   KPHL -13.8301  0.001 -17.5165 -10.1438   True
  KHOU   KPHX   7.6055  0.001   3.9191  11.2919   True
  KHOU   KSEA -13.1726  0.001  -16.859  -9.4862   True
  KIND   KJAX  17.5863  0.001  13.8999  21.2727   True
  KIND   KMDW  -0.3425    0.9  -4.0288   3.3439  False
  KIND   KNYC   3.3452  0.114  -0.3412   7.0316  False
  KIND   KPHL   4.4932 0.0046   0.8068   8.1795   True
  KIND   KPHX  25.9288  0.001  22.2424  29.6151   True
  KIND   KSEA   5.1507  0.001   1.4643   8.8371   True
  KJAX   KMDW -17.9288  0.001 -21.6151 -14.2424   True
  KJAX   KNYC -14.2411  0.001 -17.9275 -10.5547   True
  KJAX   KPHL -13.0932  0.001 -16.7795  -9.4068   True
  KJAX   KPHX   8.3425  0.001   4.6561  12.0288   True
  KJAX   KSEA -12.4356  0.001  -16.122  -8.7492   True
  KMDW   KNYC   3.6877 0.0498   0.0013    7.374   True
  KMDW   KPHL   4.8356 0.0014   1.1492    8.522   True
  KMDW   KPHX  26.2712  0.001  22.5849  29.9576   True
  KMDW   KSEA   5.4932  0.001   1.8068   9.1795   True
  KNYC   KPHL   1.1479    0.9  -2.5384   4.8343  False
  KNYC   KPHX  22.5836  0.001  18.8972  26.2699   True
  KNYC   KSEA   1.8055 0.8612  -1.8809   5.4919  False
  KPHL   KPHX  21.4356  0.001  17.7492   25.122   True
  KPHL   KSEA   0.6575    0.9  -3.0288   4.3439  False
  KPHX   KSEA -20.7781  0.001 -24.4645 -17.0917   True
------------------------------------------------------
