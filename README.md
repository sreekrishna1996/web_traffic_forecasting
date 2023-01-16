## Web Traffic Forescasting 

['Streamlit_app'](https://sreekrishna1996-web-traffic-forecas-web-traffic-forecast-yri83q.streamlit.app/)

### Business Case: AdEase - Time Series

#### Problem Statement:

Ad Ease is an ads and marketing based company helping businesses elicit maximum clicks @ minimum cost. AdEase is an ad infrastructure to help businesses promote themselves easily, effectively, and economically. The interplay of 3 AI modules - Design, Dispense, and Decipher, come together to make it this an end-to-end 3 step process digital advertising solution for all.

You are working in the Data Science team of Ad ease trying to understand the per page view report for different wikipedia pages for 550 days, and forecasting the number of views so that you can predict and optimize the ad placement for your clients. You are provided with the data of 145k wikipedia pages and daily view count for each of them. Your clients belong to different regions and need data on how their ads will perform on pages in different languages.

#### Solution: EDA | ML model building

Ad Ease is an ads and marketing based company helping businesses elicit maximum clicks @ minimum cost. Ad Ease is an ad infrastructure to help businesses promote themselves easily, effectively, and economically. The interplay of 3 AI modules - Design, Dispense, and Decipher, come together to make it this an end-to-end 3 step process digital advertising solution for all.

Clients of Ad ease belong to different regions. As per the business problem, they need data on how their ads will perform on pages in different languages. We were provided with the data of 145k Wikipedia pages along with their view count for 550 days  from 2015-07-01 to 2016-12-31. We as a data science team were tasked to forecast the number of views for each language so that we can predict and optimize the ad placement for Ad ease clients.

It was a simple data frame which had data of  145k Wikipedia pages along with their view count for 550 days from 2015-07-01 to 2016-12-31.Extracted necessary information from the page name viz. title, language, access type, and access origin. Missing values were imputed and outliers were treated. 

With the help of given data, I built multiple forecasting models viz. ARIMA, SARIMAX, and Prophet for all pages combined in each language.

1. I performed EDA on the whole data set before I started building forecasting models. All the inferences from my EDA have been mentioned in my notebook.

2. The data set consisted of webpages which are in chinese, french, english, german, russian, japanese and spanish. I grouped the pages on the basis of language and created new data frames. The data frames only had dates as columns and each webpage as a row. All the values were No. of views. Rest of the features were dropped.

3. In each of the data frames, some pages did not have views for some of the dates. Some missing values might be due to some pages not yet being created for the earlier dates while other pages already existed. I dropped the rows which had missing values in more than 5% of the total columns. For the rest of the rows I used 'bfill' technique to fill the missing values.

4. For each language, I added the views for each date for all the webpages combined. Finally each language data set had only 2 features which were the dates in order and the no. of views for each date.

5. I used the last 3 months of the data to forecast and tune my hyper parameters on the basis of MAPE scores.

6. Decomposed the time series of all the languages into trend, seasonality and errors. Built the line plots for each of these decompositions. From the line plots, I came to know that, almost all the time series had no trend or trend was sideways. Weekly seasonality existed in most of the time series with Saturdays and Sundays having peak number of views.

7. Since, all the modeIs required the data to be stationary, I used the Dickey fuller to test stationarity. If the data was not stationary, I had to deseasonalise it (by differencing a view value with another value which is 7days prior) and detrend it if needed. (by differencing a view value with its immediate previous neighbour).

8. I clipped the outliers by using the line plots.

9. I built multiple forecasting models viz. ARIMA, SARIMAX, and Prophet. I used the ACF and PACF plots to choose the total number of lags (higher limit). I tuned my hyperparameters for best MAPE score on test data. 

10. Depending on the type of language data, either ARIMA, SARIMAX or Prophet gave the best forecast. I got my best forecast of 3.3% on chinese data set using Prophet algorithm. 

11. I also built a pipeline function which can preprocess a given data set and build models end to end. 

12. In the end, I deployed the model on the streamlit cloud.

To whoever reads this, I hope my insights and recommendations from this case study were meaningful.

Thank you,

Krishna

