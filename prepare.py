import pandas as pd

from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split

import sklearn.preprocessing



def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    '''
    We will eliminate all columns with less than 50% non-null, and all rows with less than 75% non-null.
    '''
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def impute_null_values(df):
    '''
    We will use SimpleImputer to impute the mean value into the null values into each column.
    '''
    #We will use the mean imputer function.
    imputer = SimpleImputer(strategy='most_frequent')

    #We will create a for loop that will impute all the null values in each one of our columns.
    for col in df.columns:
        df[[col]] = imputer.fit_transform(df[[col]])
    
    return df


#This function removes extreme outliers from our DataFrame
def remove_outliers(df, k, col_list):
    ''' remove the outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

continuous = ['duration_ms', 'danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness',
       'liveness', 'valence', 'tempo', ]

def make_dummies(df):

    df.time_signature = df.time_signature.replace(regex = {
                           0: 'Time_Signature_0',
                           1: 'Time_Signature_1', 
                           2: 'Time_Signature_2', 
                           3: 'Time_Signature_3', 
                           4: 'Time_Signature_4', 
                           5: 'Time_Signature_5'})
    
    df.key = df.key.replace(regex = {
                           0: 'Key_0',
                           1: 'Key_1', 
                           2: 'Key_2', 
                           3: 'Key_3', 
                           4: 'Key_4', 
                           5: 'Key_5', 
                           6:  'Key_6',
                           7: 'Key_7',
                           8: 'Key_8',
                           9: 'Key_9',
                           10: 'Key_10',
                            11: 'Key_11'})
    
    ## Now we will substitute the object values for dummy values that are easier to process. 
    time_signature_dummies = pd.get_dummies(df['time_signature'])
    
    key_dummies = pd.get_dummies(df['key'])
    
    ##Concatenate our dummy values to our main Dataframe. 
    df = pd.concat([df, time_signature_dummies, key_dummies], axis=1)
    
    ## Drop the redundant columns.
    df = df.drop(columns = ['key', 'time_signature'])
    
    return df

def prepare_data(df):

    df = handle_missing_values(df)

    df = impute_null_values(df)
    
    return df

def data_no_outliers(df):
    df = remove_outliers(df, 3, continuous)
    
    return df

def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on churn to get an even mix of each churn, yes or no
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    
    # splits train_validate into train and validate using train_test_split() stratifying on churn to get an even mix of each churn
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123)
    return train, validate, test


def add_scaled_columns(train, validate, test):
    '''
    Scales columns using min-max scaler. We scale loudness and duration
    because those columns are not on the 0-1 scale.
    '''
    columns_to_scale = ['duration_ms', 'loudness', 'tempo']
    # new column names
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    
    #Define scaler
    scaler_min_max = sklearn.preprocessing.MinMaxScaler()
    
    # Fit the scaler on the train
    scaler_min_max.fit(train[columns_to_scale])
    
    # transform train validate and test
    train = pd.concat([
        train,
        pd.DataFrame(scaler_min_max.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler_min_max.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    
    
    test = pd.concat([
        test,
        pd.DataFrame(scaler_min_max.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)
    
    return train, validate, test