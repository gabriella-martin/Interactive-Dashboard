<h1 align="center">Interactive Dashboard</h1>


To view the dashboard with dummy data for privacy, please go to this [link](https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/)


<h4 align="left">Languages and Technologies</h4>

<div align="left">
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" height="60" width="60"   />
	 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="60" width="60"  />
	<img src="https://toppng.com/uploads/preview/rest-api-icon-rest-api-icon-11553510526uqs2ynyga2.png" alt="html5" width="40" height="40"/>
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apple/apple-original.svg"  width="60" height="60"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="60" width="60"   />
    <img src="https://avatars.githubusercontent.com/u/45109972?s=280&v=4" height="60" width="60"   />
    <img src="https://cdn.theorg.com/39deb29f-6dae-4ac1-940c-39515deac1e5_medium.jpg" height="60" width="60"   /> </div>

<h4 align="left">API's Leveraged</h4>

<div align="left">
	<img src="https://pbs.twimg.com/profile_images/413637612419555328/i0FUzkwi_400x400.png" height="40" width="40"   />
	 <img src="https://upload.wikimedia.org/wikipedia/fr/a/a2/Logo_withings.png" height="40" width="120"  />
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/ICloud_logo.svg/2560px-ICloud_logo.svg.png" alt="html5" width="60" height="40"/>
	<img src="https://trackingtime.co/wp-content/uploads/2022/09/TrackingTime-logo-complete.png"  width="140" height="30"/>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQra-BSlYIkhhuSxGEZ6rYVqoJojLDL-3wuXPEtul4U5lnHooSGaR4JtcNEk_57eIuj5jI&usqp=CAU" height="40" width="40"   />
    <img src="https://www.airtable.com/images/newsroom/newsroom_image-1_1x.png" height="50" width="60"   />
    <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png" height="40" width="100"   /> 
	<img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Todoist_logo.png" alt="html5" width="100" height="40"/>
	<img src="https://api-sports.io/assets/img/home1/hero-banner.png"  width="60" height="60"/>
    <img src="https://camo.githubusercontent.com/2fbe9828475e6b419546ec47be120a0e6e8dfc6e3d8d3c433463817a57c0e977/68747470733a2f2f626c6f672e74666c2e676f762e756b2f77702d636f6e74656e742f75706c6f6164732f323031382f30352f63726f707065642d6c6f676f5f726f756e64656c2d322e706e67" height="60" width="60"   />
    <img src="https://blog.weatherapi.com/wp-content/uploads/2020/02/Asset-62.png" height="60" width="130"   /></div>



<h2 align="left">Introduction</h2>

As someone who loves collecting data on my daily life, I was motivated by the need to simplify the often cumbersome process of accessing and analyzing data that plays a crucial role in my daily life. Before creating this dashboard, I found myself frequently jumping between multiple apps and sources of information just to gather the data I needed to make informed decisions about my health, work, and other important aspects of my life.

Not only was this approach inefficient and time-consuming, but it also made it difficult to get a complete and holistic view of the data I was dealing with. It was a challenge to track trends over time, identify patterns, and draw meaningful insights from the information at my disposal. In short, the lack of a centralized, user-friendly platform for managing my personal data was hindering my ability to live a more organized, productive, and fulfilling life.

That's where the motivation for this app comes in. By consolidating all of my personal data in one place and presenting it in a visually appealing manner, this dashboard has made it much easier for me to monitor my progress, identify areas for improvement, and stay on top of the things that matter most to me; this app has become an indispensable tool for helping me stay organized, focused, and in control of my life.

I began by brainstorming the metrics I wanted to track and decided on four core categories; general, health, personal and productivity. I dedicated a page to each of these categories in my dashboard.

**Dashboarding Software**

Streamlit is a Python library that I chose to use for building my dashboard because of its simplicity, flexibility, and ease of use. I also chose to use Streamlit because I wanted to focus on improving my backend development skills while still being able to create a polished and user-friendly frontend for my dashboard. Streamlit provided an ideal solution to this challenge by enabling me to quickly build a professional-looking dashboard without requiring extensive knowledge of front-end development. This allowed me to focus more on the data processing and analysis that is critical to my project while still delivering a polished and responsive user experience. Streamlit offers a community cloud hosting option at no cost for website hosting. While it's suitable for my needs, with it being free results in slightly slower performance. Check streamlit out [here]( https://docs.streamlit.io/).

---
<h2 align="left">Welcome Data</h2>

*The full code for my welcome page pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/instant_pipelines/welcome_pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Welcome.py). All code on the home page is pulled once the page is loaded to ensure it is in accurate in real-time*

The homepage of my dashboard provides a snapshot of key information that I need to track on a daily basis. It includes the weather, upcoming football games, my to-do list, current tube status, and recently listened to music. The purpose of the homepage is to give me a quick and easy overview of the most important information I need to know at a glance. This enables me to plan my day efficiently and stay on top of my tasks and goals. 

![alt text](resources/welcome.png)

**NASA Image of the Day**: NASA have multiple [API's](https://api.nasa.gov/), my favourite being the image of the day. As the name suggests, the API returns a different space related picture each day.

**Recent Music**: As part of my dashboard's welcome page, I have integrated Spotify's [API](https://developer.spotify.com/documentation/web-api/) to provide information on my music listening habits. The API seamlessly integrates with the welcome page, displaying the track that I am currently listening to. If I am not listening to anything at the moment, the API instead pulls information on the most recently played track. The ability to grab album artwork adds a visually appealing touch to the dashboard. Spotify's REST-API uses OAuth 2.0 to authenticate which was fun to code.

**Current Weather**: I added a weather section to the welcome page of my dashboard to provide quick and easy access to the current weather conditions. I retrieve the current temperature, current condition -formatted into an emoji, sunrise and sunset. There are many options for a free weather API but I use this [one](https://www.weatherapi.com/).

**Tube Status**: As I rely on the DLR for my daily commute, it is important for me to have up-to-date information on the current tube status to ensure that I can plan my journey efficiently. By retrieving this information via an API and formatting it with a corresponding emoji, it provides a quick and easy way for me to stay informed about any potential disruptions or delays that may affect my commute. TFL have a variety of [API's](https://api.tfl.gov.uk/), but for my purposes I only wish to retrieve the [line status](https://api.tfl.gov.uk/swagger/ui/index.html?url=/swagger/docs/v1#!/Line/Line_MetaModes).


**Todays Work Tasks**: In my personal dashboard, I rely on ToDoist to retrieve my work-related tasks for the day. Unlike the personal section, which shows the percentage of completed tasks, ToDoist's [API](https://developer.todoist.com/guides/) is called each time the page loads to provide me with an up-to-date list of work-related tasks. By retrieving the content of each task, I get a clear overview of the specific work-related tasks that I need to complete, helping me stay organized and focused throughout the day. This is achieved by creating a unique project within ToDoist and retrieving the contents of the tasks via their API.

**Next United Game**: As a lifelong fan of Manchester United, I never want to miss any of their games. To ensure that I am always up-to-date with the important information about the next match - including the date, time, whether it is a home or away game, the opponent, and the league - I use this football [API](https://rapidapi.com/api-sports/api/api-football/). This information is automatically retrieved and displayed as soon as the page is loaded, allowing me to stay on top of the latest fixtures.

**Data Pipeline Visualisation**

![alt text](resources/welcomepipeline.png)

---
####Data Processing 

Instead of real-time data streaming, I run the pipeline once nightly in a batch process for this page and subsequent pages. Since it's crucial for me to monitor progress over time, I utilized Streamlit's interactive features and incorporated a date range slider into my code. This slider enables me to view yesterday's data (compared to the day before %), a three-day average (compared to the 3-day before average %), or a seven-day average (compared to the 7-day before average %), thereby allowing me to track progress visually across different short-term intervals. The statistics are generated using this [script](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/important_metrics.py) and are displayed on each page. To visualize long-term data, I utilize pandas and plotly in Streamlit to plot graphs that illustrate the complete dataset and enable me to track trends and gain insights over the long-term.

<h2 align="left">Health Data</h2>

*The full code for my health data pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/batch_pipelines/health_pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/pages/2%20_%F0%9F%A4%8D_Health.py)*

<div align="center">
	<img src="resources/health.png"/>
 </div>


##### Pipeline One: Retrieving Steps, Active Calories, Total Calories Burned, Exercise, VO₂ Max & Diet

My apple watch tracks my movement and VO2 max but currently there is no easy direct access to automatically retrieve this data so I figured a work-around. Starting with [this app](https://www.healthexportapp.com/) and an iOS Shortcut that runs once nightly. I use [MyFitnessPal](https://www.myfitnesspal.com/) to track my diet. Although they have their own [API](https://myfitnesspalapi.com/), they are selective of who they give out API keys to; I have applied but am yet to receive a response. Nevertheless, Apple Health can connect to it for some basic metrics which is sufficient for my needs. I chose the most important diet metrics to me and included these in the nightly data extraction. The auto-export shortcut process collects these specific datapoints and then saves it as a CSV file in my iCloud Drive. 


<div align="center">
	<img src="resources/automatingshortcut.PNG" height =350  />
	 <img src="resources/shortcut.PNG" height="350"  />
 </div>

The next step is to gain access to this file in my Python script, for this I use [PyiCloud]( https://github.com/picklepete/pyicloud). Once the file is accessible, I use python to extract and process the data. This data alongside the other health metrics is then added to my database CSV file ready to be visualised with Streamlit and Pandas.


##### Pipeline Two: Retrieving Sleep

Although in theory the above process should work for sleep data, I found it very buggy, 50% of the time the sleep data was empty. However, I found that what I use for my mood-tracker, [Exist]( https://exist.io/), has integrations with Apple Health, and getting sleep from their [API]( https://developer.exist.io/) was much more successful. When my python script runs each day, I use their REST API to get my sleep time, which goes directly to my CSV ready for visualisation.

##### Pipeline Three: Retrieving Body Metrics

For retrieval of my body measurements, I use a [Withings Smart-Scale]( https://www.withings.com/uk/en/scales) coupled with their [API]( https://developer.withings.co.uk/). I do a daily weigh-in which my Python script retrieves each night via their API. The data is then added to my CSV database for visualisation.

**Data Pipeline Visualisation**


<div align="left">
	<img src="resources/healthpipeline.png"/>
 </div>

---
<h2 align="left">Productivity Data</h2>

*The full code for my productivity data pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Batch_Pipelines/Productivity-Data-Pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/pages/3%20_%F0%9F%A4%8D_Productivity.py)*

<div align="center">
	<img src="resources/productivity.png"/>
 </div>


##### Pipeline One: Retrieving Working & Reading Hours

For tracking my working and reading time I use [Tracking Time](https://trackingtime.co/), other viable options with API’s include [RescueTime](https://www.rescuetime.co.uk/) or [Toggl](https://toggl.co.uk/), but I prefer the interface of Tracking Time. Nightly my Python script connects to their [API]( https://api.trackingtime.co/doc/index.html) and with a bit of processing, I can retrieve the time spent that day on reading and working respectively. This data is then added to my CSV and visualised with Streamlit and Pandas.

##### Pipeline Two: Retrieving Coding Hours

For a clearer picture on my productivity I installed [WakaTime]( https://wakatime.co.uk/) into my IDE to get the hours spent actually coding (which is a subset of my time spent working). Nightly my Python script speaks to their [API]( https://wakatime.co.uk/developers) and adds this data to my CSV.

##### Pipeline Three: Retrieving GitHub Contributions

GitHub do have their own [API]( https://docs.github.co.uk/en/graphql) capable of retrieving this data but as I only care about commits at this moment, the [Exist]( https://exist.io/) – GitHub integration suffices. As above, my Python script connects to their [API]( https://developer.exist.io/) each night, retrieves this data and adds it to my CSV database.

**Data Pipeline Visualisation**


<div align="left">
	<img src="resources/productivitypipeline.png"/>
 </div>

---

<h2 align="left">Personal Data</h2>

*The full code for my personal data pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Batch_Pipelines/Personal-Data-Pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/pages/4%20_%F0%9F%A4%8D_Personal.py)*

<div align="center">
	<img src="resources/personal.png"/>
 </div>


##### Pipeline One: Retrieving ToDo's Done Data

I organise my daily life with [ToDoist]( https://todoist.com/), who have a great [API]( https://developer.todoist.com/guides/) where each night my Python script retrieves the percentage of tasks in each ToDoist section I have completed that day. I separate the task into sections by creating projects in ToDoist.  As the majority of my tasks are recurring, some manipulation with Python is necessary to accurately retrieve what has been completed today. These daily percentages are then added to my CSV database file for visualisation with Streamlit & Pandas.


##### Pipeline Three: Retrieving Book Data

I have been an avid user of [Goodreads]( https://www.goodreads.com/user/show/108711145-gabriella-martin) to track my reading progress but although they did have a solid API, they have discontinued it and are no longer issuing keys. However, I use [Airtable]( https://airtable.com/) to store much of my personal data and began to add my book tracking data. I then could use their [API]( https://airtable.com/developers/web/api/introduction) to get my most recently read and currently reading books. Rather than being added daily to a CSV, this is instead called whenever the page is loaded in order to get an automatic update

##### Pipeline Four: Retrieving Listening Data

To retrieve this data I again use the Spotify [API]( https://developer.spotify.com/documentation/web-api/). Here I pull my current top tracks so I can see what I have had on repeat recently. This is also not added to the CSV database and is instead pulled automatically when the page is loaded

**Data Pipeline Visualisation**
<div align="left">
	<img src="resources/personalpipeline.png"/>
 </div>

**Financial**: Currently a work in progress, I aim to add an authentication layer (due to the sensitive information) like the one featured [here](https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/) and leverage the [Monzo Personal API](https://docs.monzo.com/#introduction). This involves moving over my primary banking to Monzo, something I have wanted to for a while. 

**Library**: On this page I am able to view all the books I have read, which is served by the AirTable API I have previously used for book data.