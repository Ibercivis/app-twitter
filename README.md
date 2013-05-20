PyBossa demo application for Twitter

This application shows how you can import a set of Tweets with a given hashtag
and analyze them in a PyBossa application. This app shows how you can analyze
emotions posted on a tweet.

This application has four files:

*  createTasks.py: for creating the application in PyBossa, and fill it with some tasks.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: the tutorial that will be shown the first time a user
   participates.
*  long-description.html: the information page for the application.

Testing the application
=======================

To test the application, all you have to do is create a virtualenv in the
source folder, and run the following commands

```bash
    $ virtualenv env
    $ . env/bin/activate
    $ pip install -r requirements.txt
```
Then, you can follow the next steps:

*  Create an account in PyBossa
*  Copy under your account profile your API-KEY
*  Run python createTasks.py -u http://crowdcrafting.org -k API-KEY
*  Open with your browser the Applications section and choose the FlickrPerson app. This will open the presenter for this demo application.

**NOTE**: change the name and short name of the application in the file
app.json as there might be another application with the same name in the
system.

Please, check the full documentation here:

http://docs.pybossa.com/en/latest/user/create-application-tutorial.html

The thumbnail has been created using a photo from D. Sharon Pruitt (license CC BY 2.0). 
Check the original photo here: http://www.flickr.com/photos/pinksherbet/315127886/

**NOTE**: for further details on the research behind the emotions and feelings
see this [Etherpad](https://etherpad.mozilla.org/sentiment) (only in Spanish)
