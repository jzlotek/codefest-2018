# **HydraView**

######  A PhillyCodeFest2018 Project

####  Built With
* Python  
- Flask
* SASS
* HTML5
* Google Maps Geo-Coding API
* Amazon Web Services


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

American Water provided us with a JSON file that contained information about various groups of fire hydrants within New Jersey. The file gave us the latitude and longitude, wether the hydrant was operational or not, and if the hydrant needs to be upgraded.  

***

### Business Case

In this competition, we were provided a json file containing all the data points; each data point has the respective categories:

* Lat
* Lng
* OutOfService
* Critical
* CriticalNotes

With this data set we want to provide first responders with an application that will direct them to the most optimal fire hydrant for the location that they are heading towards potentially recovering additional live saving seconds.

***

### Our Approach

Taking what exists in Providence, RI, and with our business case in mind, we want to model our application to effectively solve the challenge. However, Philadelphia, with a population of roughly 1.2 million, is bound to have drastically more fire hydrants. Therefore, we need to change how we store and manipulate the data. We still want to add various categories if time permits for our mobile application collection such as street, detailed location description, and hydrant id.
The data set itself must be larger as well. Instead of just storing all the data into a hashmap table, we want to use a data type called a quadtree. This allows for us to quickly and effectively store a bulk set of data and quickly retrieve a set of fire hydrants for a given input location. Here’s briefly how it will work:
Our application, for the purposes of this competition, will be modeled using the given dataset from American Water. However, as stated in our business case, we suggest that a much more detailed dataset be created, similar to what is established in Providence. We will take the JSON data and map it to a created quadtree. Then, our application will allow users to input their current location, or for the sake of having the flexibility, any given location, because we want users to also sit at the office and view conditions of any given fire hydrants. Then, the application will search through our dataset and return the unique object (or closest object) and some other points around it for a given radius. We think that this approach will prove very suitable as a solution to this challenge.

***

### Conclusion

In conclusion, we believe that by utilizing the provided data we can effectively provide an unique solution for first responders and water departments to view fire hydrants and maintain their conditions. By doing so, they can view critical notes, see any currently in service, or view them on the fly for emergencies. Overall, we believe our solution is what should be adopted to increase the effectiveness of our first responders.
