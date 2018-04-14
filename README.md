# **HydraView**

######  A PhillyCodeFest2018 Project

####  Built With
* Python  
* SASS
* HTML5
* Google Maps Geo-Coding API
* Docker
* Amazon Web Services
* Apache Cassandra (Data Stax Enterprise)


## Contributors:
* John Zlotek
* Dakota Wessel
* Joseph Hines
* Matt Horger

***

### Elevator Pitch
> In the event of an emergency, HydraView provides first responders with the location of the nearest fire hyrdant.

### Challenge

Get the most accurate information to responders. Create an application that asks a user for their current location. Use this current location to find the nearest fire hydrant that is in service, display any critical notes that may be available.

### Existing systems

In the United States, there are various cities that provide open source data on the location of fire hydrants on streets. Such cities are Jacksonville, FL, Boulder, CO, and Providence, RI. These sources of data are valuable and critical for first responders in the event that the fire hydrants are needed for emergencies. But, not only are these locations useful for emergencies, but city water departments also benefit from the data in order to properly maintain the hydrants and the pipes surrounding the location to prevent bursts. 
Upon researching these existing systems, we decided to focus on Providence, RI. The data was most recently updated on February 25, 2016, and the data set seemed sufficient to work with. You can find the data in which we will be talking about here: https://data.providenceri.gov/Neighborhoods/Map-view-of-Providence-Fire-Hydrants/pna5-29w9/data
The data set had 9 categories:

* Hydrant ID
* Address Key
* Municipality
* Location Description
* Street Name
* Suffix
* City
* Plan Sheet
* Location

Using this data and their open portal, the city of Providence provides an interactive map with unique dots to show where fire hydrants are located. Each unique location could be searched, filtered, and visualized with different view controllers. In a city with a population of roughly 113,000, there are 3,224 fire hydrants (as of the recent metadata update in 2016) mapped in the dataset. 

***

### Business Case

To solve this presented challenge, we need a similar model like Providence and the other U.S. cities. However, it turns out that there exists no similar dataset on the fire hydrants located in the city of Philadelphia that is open source online. In this competition, we were provided a json file containing all the data points; each data point has the respective categories:

* Lat
* Lng
* OutOfService
* Critical
* CriticalNotes

While these data categories are great and useful for the purposes of this competition, we want to provide a much more comprehensive and long-term application similar to what Providence RI does. Therefore, we need some method of obtaining reliable information to effectively populate the remaining categories to be added to the provided dataset. We could have the Philadelphia Water Department pull up any locational data that they may have on the hydrants and the condition that they are in. However, this method may be too time-consuming for technicians to go through the thousands, possibly even ten thousands of fire hydrants. We could have each fire station in each neighborhood go to each hydrant and collect the data, but, like the water department, they have emergencies and other duties to perform.
Instead, we propose that the Philadelphia Parking Authority retrieve our data for us. Here is our pitch: agents for the parking authority walk down street blocks throughout the day. If we present them with a mobile application that has entry fields for each fire hydrant, they should be able to reliably popular a good 80% of the fire hydrants in the city.  Why the 80%? Well, we have to account for the fact that some streets aren’t covered by the PPA and some fire hydrant locations necessarily may not be on a street; they may be in a public/commercial plaza or in a drive within a business complex. However, once we obtain a bulk of the data, then we can rely on the PWD (water department) or the PFD (fire department) to provide us with the data for the remaining points. This way, we can gather tens of thousands of data points relatively quickly to supplement the dataset provided to us by American Water.


***

### Our Approach

Taking what exists in Providence, RI, and with our business case in mind, we want to model our application to effectively solve the challenge. However, Philadelphia, with a population of roughly 1.2 million, is bound to have drastically more fire hydrants. Therefore, we need to change how we store and manipulate the data. We still want to add various categories if time permits for our mobile application collection such as street, detailed location description, and hydrant id.
The data set itself must be larger as well. Instead of just storing all the data into a hashmap table, we want to use a data type called a quadtree. This allows for us to quickly and effectively store a bulk set of data and quickly retrieve a set of fire hydrants for a given input location. Here’s briefly how it will work:
Our application, for the purposes of this competition, will be modeled using the given dataset from American Water. However, as stated in our business case, we suggest that a much more detailed dataset be created, similar to what is established in Providence. We will take the JSON data and map it to a created quadtree. Then, our application will allow users to input their current location, or for the sake of having the flexibility, any given location, because we want users to also sit at the office and view conditions of any given fire hydrants. Then, the application will search through our dataset and return the unique object (or closest object) and some other points around it for a given radius. We think that this approach will prove very suitable as a solution to this challenge.

***

### Conclusion

In conclusion, we believe that by adopting similar existing systems already in place in the United States, such as Providence, RI, we can effectively provide an unique solution for first responders and water departments in Philadelphia to view fire hydrants and maintain their conditions. By doing so, they can view critical notes, see any currently in service, or view them on the fly for emergencies. By having the Philadelphia Parking Authority collect our fire hydrant locational data, we can quickly implement this improved dataset system here in the city and do it with efficiency with our improved data structure. Overall, we believe our solution is what Pennsylvania Water should adopt and model for their company to improve our wonderful city of Philadelphia and its’ infrastructure.