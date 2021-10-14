import time
import pandas as pd
import numpy as np
from statistics import mode
days ={'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
cities = ['chicago','new york city','washington']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('city (chicago, new york city, washington)')
    print('month (all, january, february, ... , june)')
    print('day of week (all, monday, tuesday, ... sunday)')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)

    city = str(input("enter the city :")).lower()
    month = str(input("enter the month :")).lower()
    day = str(input("enter the day : ")).lower()
    if (city in cities) & (day in days.keys()) & (month in months.keys()):
        print('-'*40)
        return city,month,day
    else :
        print('invalid input')
        get_filters()
        
    
    
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    if "Start Time" in df.columns :
        df["Start Time"] = pd.to_datetime(df["Start Time"]) 
        df["Time"]  = df["Start Time"].dt.hour
        df["day"]   = df["Start Time"].dt.day
        df["month"] = df["Start Time"].dt.month
        days ={'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
        months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}

            # use the index of the months list to get the corresponding int
        # filter by month to create the new dataframe
        df = df[(df['month'] == months[month]) & (df['day'] == days[day])]
        return df
    else : 
        print("no Start Time in your city ")
        input1 = input("print y to restart or any key to stop ")
        if input1== "y":
            get_filters()
        else : 
            print("stpoed")
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    print( f"the most common month : {mode(df['month'])}")

    # display the most common day of week
    print(f"most common day of week : {mode(df['day'])}")

    # display the most common start hour
    print(f"most common start hour : {mode(df['Time'])}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most
    try :
        if ("Start Station"|"End Station") in df.columns :

            print("commonly used start station")
            print(mode(df['Start Station']))
            print("---------------------")
            # display most commonly used end station
            print("commonly used end station")

            print(mode(df['End Station']))
            print("---------------------")

            # display most 
            print("frequent combination of start station and end station trip")
            print(mode(zip(df['Start Station'],df['End Station'])))
            print("---------------------")
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
        else : 
            print("no Stations  in your city ")
            input2 = input("print y to restart or p to pass or any key to stop ")
            if input2== "y":
                get_filters()
            elif input2 == "p":
                pass
            else : 
                print("stpoed")
    except : 
        pass

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    try : 
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display 
        print("total travel time")
        print(df['Trip Duration'].sum())
        print("total travel mean")
        print(df['Trip Duration'].mean())

        # display mean travel time


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except : 
        pass


def user_stats(df):
    """Displays statistics on bikeshare users."""
    try :
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        if 'User Type' in df.columns :
            print(df['User Type'].value_counts())
        else : 
            print("no such column")
        # Display counts of gender
        # Display earliest, most recent, and most common year of birth
        if "Gender" in df.columns : 
            print("counts of gender")
            print(df['Gender'].value_counts())
        if "Birth Year" in df.columns: 

            print('-----------------------')
            print("old Birth Year",':',df["Birth Year"].min()) #old
            print('-----------------------')

            print("latest Birth Year",':',df["Birth Year"].max()) #young
            print('-----------------------')

            print("common Birth Year",':',mode(df["Birth Year"])) #young



            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
        else : 
            print("your city is not containing all data ")
    except : 
        pass
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
