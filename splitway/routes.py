from flask import render_template, url_for, flash, redirect, request
from splitway import app, db, bcrypt
from splitway.forms import RegistrationForm, LoginForm, SearchForm, EventForm
from splitway.models import User, Event
from flask_login import login_user, current_user, logout_user, login_required
import requests
import json
import urllib.request
import datetime

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/results")
def results():
    return render_template('results.html')

def getDistance(address1, address2):
    address1 = address1.replace(" ", "+")
    address2 = address2.replace(" ", "+")
    distanceURL = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + address1 + "&destinations=" + address2 + "&units=imperial&mode=walking&language=en-EN&key=AIzaSyANMkW7bIUZCJI1jNM2l5hl1CpmXzVCpJg"
    with urllib.request.urlopen(distanceURL) as url:
        data = json.loads(url.read().decode())
    distance = data["rows"][0]["elements"][0]["distance"]["value"]
    distance = distance / 1609.344
    return distance
@app.route("/search", methods=['GET', 'POST'])
def search():
    if current_user.is_authenticated == False:
        return redirect(url_for('login'))
    form = SearchForm()
    if form.validate_on_submit():
       #INSERT SEARCH ALGORITHM HERE
        eventList = []
        thisUserDestination = form.destination.data
        thisUserCurrenLocation = form.current_location.data
        thisUserTime = (str)(form.time.data)
        userYear = thisUserTime[0:4]
        userMonth = thisUserTime[5:7]
        userDay = thisUserTime[8:10]
        userHour = thisUserTime[11:13]
        userMinute = thisUserTime[14:16]
        userTime = int(userHour) * 60 + int(userMinute)
        query = Event.query.all()
        for event in query:
            eventCurrentAddress = event[4]
            eventDestinationAddress = event[5]
            eventTime = (str)(event[6])
            eventYear = eventTime[0:4]
            eventMonth = eventTime[5:7]
            eventDay = eventTime[8:10]
            eventHour = eventTime[11:13]
            eventMinute = eventTime[14:16]
            eventTime = int(eventHour) * 60 + int(eventMinute)
            time = abs(eventTime-userTime)
            currentDistance = getDistance(thisUserCurrenLocation, eventCurrentAddress)
            destinationDistance = getDistance(thisUserDestination, eventDestinationAddress)
            if currentDistance < .5 and destinationDistance < .5 and time < 15 and eventYear == userYear and eventMonth == userMonth and eventDay == userDay:
                eventList.add(event)
        eventListTruncate = []
        for i in range(4):
            eventListTruncate = eventList[i]
        return render_template('results.html', eventList = evenListTruncated)
    return render_template('search.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/addevent", methods=['GET', 'POST'])
def addevent():
    if current_user.is_authenticated == False:
        return redirect(url_for('login'))
    form = EventForm()
    if form.validate_on_submit():
        stringtime = str(form.time.data)
        event = Event(event_name=form.eventName.data, first_name=current_user.first_name, current_address=form.current_location.data, destination_address=form.destination.data, time=stringtime, email=(current_user.email))
        db.session.add(event)
        db.session.commit()
        flash('Your event has been created! People can now see your event and reach out.', 'success')
        return redirect(url_for('search'))
    return render_template('addevent.html', title='Add Event', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))