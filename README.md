# URL Routing

This assignemnt uses Flask URL routing. The main page is cities.html, where there are four images of cities. Each image is inside of an anchor tag, which links to /cities/[cityname]. For example, the New York picture has href="/cities/new-york." There is no such new-york.html file; rather, this route is handled in Flask, and renders the template city.html for the specfied city. This page shows the local translation for "Welcome!" in that city's language, and displays the image of that city. 

Note, it is not possible to directly navigate to the template (eg through something like localhost:5000/cities/city.html). Only routes that are handled in the server.py file are allowed. If a user tries to go to a city that is not among the specified four, such as localhost:5000/cities/austin, they will simily be redirected to the list of cities. 

## Screenshots

### Landing page
Nothing to see here... 

![Landing](/doc/index.png?raw=true "index.html")


### List of Cities
cities.html, showing the image hover effect on the Rome image.

![Cities](/doc/cities.png?raw=true "cities.html")


### City Page: Rome
![Rome](/doc/rome.png?raw=true "city=rome")


### City Page: Cairo
![Cairo](/doc/cairo.png?raw=true "city=cairo")
