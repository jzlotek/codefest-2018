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

Our web application currently takes the given data set which persists of ~2500 fire hydrants in the NJ area. The user is asked for the address of the fire when an address is inputted into our API, we make HTTP GET calls to our Flask server with the address of the fire as a query parameter. We return the address's decimal degree coordinates and a list of the closest, n fire hydrants to that address (another query parameter).

An example query:
http://ec2-52-207-219-213.compute-1.amazonaws.com/getClosestHydrants?address=Address&num=X
Address is the address, X is the number of hydrants to find

A map will then be displayed for the user with fire hydrant pins that user can select.

Future improvements include implementing a quad tree as a way of storing data. This would allow the application to scale and still have quick lookups regardless of the data size.

***

### Conclusion

In conclusion, we believe that by utilizing the provided data we can effectively provide an unique solution for first responders and water departments to view fire hydrants and maintain their conditions. By doing so, they can view critical notes, see any currently in service, or view them on the fly for emergencies. Overall, we believe our solution is what should be adopted to increase the effectiveness of our first responders.
