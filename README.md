QA-Project-2

https://trello.com/b/2sGJAUXw/project-2

This project consists of information a fortune telling app, which also provides the user with a lucky gemstone that they can cherish and research for themselves. The fortunes and the gems themselves are actually dependant on the time that the user has accessed the web app; during nighttime the fortunes become a lot more ominous! 
The initial server will perform a GET request, which will help to determine the two post requests. The final statement on the webpage will provide the user with a combination of a lucky gem and a fortune, depending on the time of day. Bad omens at night will force the app to provide the user from a selection of the most lucky gemstones. 

I initially wanted all three of the functions I created to be used as separate apis, however I soon realised this was not optimal during the project and managed to consolidate all three of the functions into the one app.py file. 

The web app for this project is more streamlined than the first, and possibly simpler, but there is a lot more happening in the backend of the app. 

I created two dictionaries, which are dependent on two keys, 'yin' and 'yang'. The app can be run via Docker, Jenkins, Ansible, and all three together, which helps to make the code and app more efficient. Docker in particular allows the use of replicas, which helps with the load balancing of the app. 

Nginx was implemented in order to assist with load balancing and swarm activity. Using multiple worker nodes with this application helps to ensure that any disconnections are reduced to a minimum. 

