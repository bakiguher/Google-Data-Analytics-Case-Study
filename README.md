**Google-Data-Analytics-Case-Study**
How Does a Bike-Share Navigate Speedy Success?

**Introduction**

This case study is about Capstone project requirement for Google Data Analytics Professional Certificate. It involves a fictional bike-share company's data of its customer's trip details over a 12 month period in the year of 2021.

**About the company**

Cyclistic, A fictional bike-share program that features many bicycles and docking stations. Cyclistic sets itself apart by also offering reclining bikes, hand tricycles, and cargo bikes, making bike-share more inclusive to people with disabilities and riders who can’t use a standard two-wheeled bike. The majority of riders opt for traditional bikes; about 8% of riders use the assistive options. Cyclistic users are more likely to ride for leisure, but about 30% use them to commute to work each day.

In 2016, Cyclistic launched a successful bike-share offering. Since then, the program has grown to a fleet of 5,824 bicycles that are geotracked and locked into a network of 692 stations across Chicago. The bikes can be unlocked from one station and returned to any other station in the system anytime.

Until now, Cyclistic’s marketing strategy relied on building general awareness and appealing to broad consumer segments. One approach that helped make these things possible was the flexibility of its pricing plans: single-ride passes, full-day passes, and annual memberships. Customers who purchase single-ride or full-day passes are referred to as casual riders. Customers who purchase annual memberships are Cyclistic members.

Cyclistic’s finance analysts have concluded that annual members are much more profitable than casual riders. Although the pricing flexibility helps Cyclistic attract more customers, it is believed that maximizing the number of annual members will be key to future growth. Rather than creating a marketing campaign that targets all-new customers, also there is a very good chance to convert casual riders into members. Because casual riders are already aware of the Cyclistic program and have chosen Cyclistic for their mobility needs.

Cyclistic has a clear goal; design marketing strategies aimed at converting casual riders into annual members. In order to do that, however, the marketing analyst team needs to better understand how annual members and casual riders differ, why casual riders would buy a membership, and how digital media could affect their marketing tactics. Cyclistic is interested in analyzing the Cyclistic historical bike trip data to identify trends.


**Processes for data analysis phases:

1-ASK

-How do annual members and casual riders use Cyclistic bikes differently?
-What is the difference between annual members and casual riders?
-Why casual riders would buy a membership?

2-PREPARE

I am using Divvy bike data sourced from the [Divvy Bike website](https://divvy-tripdata.s3.amazonaws.com/index.html)

The data was organized by month and saved as .csv files within .zip files, I downloaded each month to my local computer it was almost 1GB in total. I combined 12 months data to 1 csv file with a python script.(combined_csv.csv)

The data has following attributes:
    ride_id : a unique ID per ride
    rideable_type: the type of bicycle
    started_at: the date and time that the bicycle was taken
    ended_at: the date and time that the bicycle was dropped
    start_station_name: the name of start station
    start_station_id: a unique ID for the start station
    end_station_name: the name of the end station
    end_station_id : a unique ID for the end station
    start_lat: the latitude of the start station
    start_lng: the longitude of the start station
    end_lat: the latitude of the end station
    end_lng: the longitude of the end station
    member_casual: the type of membership

The data source is reliable, original, comprehensive, current and cited. The data has been made available under this [license] (https://ride.divvybikes.com/data-license-agreement).

All 2021 data was very big, I downloaded it to my local pc and combined them in to one .csv file with a python script [prepare_csv.py](prepare_csv.py). 
Checked for duplicates, there was none. In total there are: 5595064 rows Then .csv file is uploaded to kaggle. 

3-PROCESS

combined_csv.csv file uploaded to [www.kaggle.com](https://www.kaggle.com/bakiguher/google-data-analytics-certificate-course-capstone)
processing phase done in kaggle notebook. A copy of notebook file: [google-data-analytics-certificate-course-capstone.ipynb](google-data-analytics-certificate-course-capstone.ipynb)

