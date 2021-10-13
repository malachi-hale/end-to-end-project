# What Makes a Hit?
## Predicting the Popularity of Songs on Spotify 

## Objectives 

### Project Goals 
 - To document **code**, **process**, **findings**, and **key takeaways** in a Jupyter Notebook report. 
 
 - To create a module `prepare.py` which contains certain function that make our processes repeatable.
 
 - To construct a model that predicts the popularity index of tracks in the Spotify library.
 
### Business Goals 
 - To predict the popularity index of tracks in the Spotify library in April 2021. 
 
 - To use clusters to create classifications for different styles of music. 
 

### Audience 

 - The Codeup Data Science Team. 
 
## Data Dictionary

|    | Feature            | Dataype   | Definition                                                                     |
|---:|:-------------------|:----------|:-------------------------------------------------------------------------------|
|  0 | id                 | object    | ID of each track in the Spotify catalogue.                                     |
|  1 | name               | object    | Name of the Track                                                              |
|  2 | popularity         | int64     | Popularity Index of the Track (0-100)                                          |
|  3 | duration_ms        | int64     | Duration of the Track in milliseconds                                          |
|  4 | explicit           | int64     | 0 for non explicit tracks, 1 for explicit tracks                               |
|  5 | artists            | object    | Names of the artists credited on the track                                     |
|  6 | id_artists         | object    | The Spotify ID of each artist on the track                                     |
|  7 | release_date       | object    | The Date the song was released                                                 |
|  8 | danceability       | float64   | The danceability score of each track                                           |
|  9 | energy             | float64   | The energy score of each track                                                 |
| 10 | key                | int64     | The key of each track. Each key number corresponds to the twelve musical keys. |
| 11 | loudness           | float64   | The loudness score for each track.                                             |
| 12 | mode               | int64     | 0 for minor, 1 for major                                                       |
| 13 | speechiness        | float64   | The speechiness score of the track                                             |
| 14 | acousticness       | float64   | The acousticness score of the track.                                           |
| 15 | instrumentalness   | float64   | The instrumentalness score of the track.                                       |
| 16 | liveness           | float64   | The liveness score of the track.                                               |
| 17 | valence            | float64   | The valence score of the track.                                                |
| 18 | tempo              | float64   | The tempo score of the track.                                                  |
| 19 | time_signature     | int64     | The time signature of the track, between 0 and 5.                              |
| 20 | year_of_release    | int64     | The year the track was released.                                               |
| 21 | duration_ms_scaled | float64   | THe duration of each song mapped to a value from 0 to 1.                       |
| 22 | loudness_scaled    | float64   | The loudness score of each song, mapped to a value from 0 to 1.                |

## Hypothesis Testing

### Continuous Variables

 - We run hypothesis testing for correlation on our of our continuous features and find that all continuous features except `valence` are signficantly correlated with popularity. 
 
### Categorical Features

 - We find a difference in mean for different groups of all of our categorical features.


## Executive Summary 
 - With the goal of determining the features most predictive of `popularity`, we used Select K Best, Recursive Feature Elimination, and hypothesis testing to determine that the most predictive features of `popularity` are:
     - `duration_ms_scaled`, 
     - `explicit`, 
     - `energy`, 
     - `danceability`, 
     - `acousticness`, 
     - `instrumentalness`,
     - `tempo`,
     - `loudness_scaled`, 
     - `year_of_release`, and 
     - `liveness`.
 
 - I used the above features to predict `popularity` using the following methods:
     - Linear Regression, 
     - LassoLars, 
     - TweedieRegressor, 
     - Polynomial Linear Regression. 
 
 - Based on the RMSE and R squared value, I concluded that Linear Regression Fourth Degree was the best model. I ran this model on the test dataset. 
 
 - On the baseline, the selected model performed better than baseline at the predicting the tracks' popularity.
 
## Pipeline Stages Breakdown

### Project planning 

 - Create a `READ.me` file with an outline of a plan for the project.
 
 - Brainstorm ideas and form hypotheses related to how variables relate to each other. 
 
### Data Acquisition 

 - Download the `tracks.csv` file from Kaggle. 
 
 - Complete intitial data summarization (`info()`, `describe()`). 
 
 - Plot distributions of individual variables. 
 

### Data Preparation 

#### In the `prepare.py` module

 - Eliminate rows and columns which fail to meet a certain threshold of non-null values.
 
 - Impute remaining null values with the most frequent value of that column. 
 
 - Eliminate extreme outliers. 
 
 - Split the data into `train`, `validate`, and `test` datasets. 
 
 - Scale the features `loudness` and `duration_ms` using MinMax scaler. 
 
#### In the Notebook 

 - Run the functions from the `prepare.py` module. 
 
 - Create a new columns `year_of_release`.
 

### Data Exploration and Analysis

 - Create multivariate visualizations. 
 
 - Visualize all variables with `popularity`. 

 - Use Recursive Feature Elimination and Select K Best to determine which features are most predictive of `popularity`. 
 
 - Run statistical tests on all categorical and continuous features to determine relationship with `popularity`. 
 

 
### Modeling 

 - Establish a bseline model. 
 
 - Document various algorithms and hyperparameters used along with evaluation code and results. 
 
 - Evaluate the model using standard techniques. Compute the evaluation metrics, compare the model to baseline, etcetera. 
 
## Reproduce my Project

To reproduce my project, you will need to download the CSV file `tracks.csv` from the following link:

 - https://www.kaggle.com/subhaskumarray/spotify-tracks-data
 
Once you have downloaded teh file, you will need to:

 - Read this `READ.me` file. 
 
 - Download the `prepare.py` and the `Final Project.ipynb` files. 
 
 - Run the `Final Project.ipynb` notebook. 
 
 