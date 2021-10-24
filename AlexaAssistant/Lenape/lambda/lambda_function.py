# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import datetime
from dateutil.relativedelta import relativedelta
import re
from icalendar import Calendar, Event, vDatetime
import urllib.request
import certifi

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
import icalendar

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

states = {
    "SEARCHMODE": "_SEARCHMODE",
    "DESCRIPTION": "_DESKMODE"
}

# URL to get the .ics
URL = "https://lenapecalendar.s3.amazonaws.com/icalfeed.ics"

# Skills name 
skillName = "Lenape:"

# Message when the skill is first called
welcomeMessage = "You can ask for the events today. Search for events by date. or say help. What would you like? "

# Message for help intent
HelpMessage = "Here are some things you can say: Is there an event today? Is there an event on the 18th of July? What are the events next week? Are there any events tomorrow?  What would you like to know?"

descriptionStateHelpMessage = "Here are some things you can say: Tell me about event one"

# Used when there is no data within a time period
NoDataMessage = "Sorry there aren't any events scheduled. Would you like to search again?"

# Used to tell user skill is closing
shutdownMessage = "Ok see you again soon."

# Message used when only 1 event is found allowing for difference in punctuation 
oneEventMessage = "There is 1 event "

# Message used when more than 1 event is found allowing for difference in punctuation 
multipleEventMessage = "There are {:n} events "

# text used after the number of events has been said
scheduledEventMessage = "scheduled for this time frame. I've sent the details to your Alexa app: "

firstThreeMessage = "Here are the first {:n}. "

# the values within the {} are swapped out for variables
eventSummary = "The {} event is, {} on {} "

# Only used for the card on the companion app
cardContentSummary = "{} on {} "

# More info text
haveEventsRepromt = "Give me an event number to hear more information."

# Error if a date is out of range
dateOutOfRange = "Date is out of range please choose another date"

# Error if a event number is out of range
eventOutOfRange = "Event number is out of range please choose another event"

# Used when an event is asked for
descriptionMessage = "Here's the description "

# Used when an event is asked for
killSkillMessage = "Ok, great, see you next time."

eventNumberMoreInfoText = "You can say the event number for more information."

# used for title on companion app
cardTitle = "Events"

# output for Alexa
output = ""

# stores events that are found to be in our date range
relevantEvents = []

def getCalendar(calendarUrl, callback):
    calendarData = urllib.request.urlopen(calendarUrl,cafile=certifi.where()).read()
    return callback(calendarData)

def readCalendar(calendarData):
    eventsData = []
    showCalHome = Calendar.from_ical(calendarData)
    for event in showCalHome.walk('VEVENT'):
        event = {
                        "summary": event.get('summary'),
                        "start": datetime.date(event.get('dtstart').dt.year,event.get('dtstart').dt.month,event.get('dtstart').dt.day).strftime('%m/%d/%Y')
                    }
        # Add the newly created object to an array for use later.
        eventsData.append(event)

    return eventsData


# Used to work out the dates given week numbers
def w2date(year, week, day) :
    Date = datetime.date(int(year), 1, 1) + relativedelta(weeks=+int(week))
    Date = Date + datetime.timedelta(days=int(day))
    return Date

# Remove HTML tags from string
def removeTags(str):
    if (str):
        return re.sub(r"/<(?:.|\n)*?>/gm","",str)

# Given a week number return the dates for both weekend days
def getWeekendData(res):
    if (len(res) == 3):
        saturdayIndex = 1
        sundayIndex = 2
        weekNumber = res[1][1:]

        weekStart = w2date(res[0], weekNumber, saturdayIndex)
        weekEnd = w2date(res[0], weekNumber, sundayIndex)

        Dates = {
            "startDate" : weekStart,
            "endDate" : weekEnd,
        }

        return Dates

# Given a week number return the dates for both the start date and the end date
def getWeekData(res):
    if (len(res) == 2):

        mondayIndex = -4
        sundayIndex = 2

        weekNumber = res[1][1:]

        weekStart = w2date(res[0], weekNumber, mondayIndex)
        weekEnd = w2date(res[0], weekNumber, sundayIndex)

        Dates = {
            "startDate" : weekStart,
            "endDate" : weekEnd,
        }

        return Dates

# Loops though the events from the iCal data, and checks which ones are between our start data and out end date
def getEventsBeweenDates(startDate, endDate, eventList):

    start = datetime.strptime(startDate, '%m/%d/%Y')
    end = datetime.strptime(endDate, '%m/%d/%Y')
    data = []

    for i in range(0,len(eventList),1):
        if (start <= eventList[i].start and end >= eventList[i].start):
            data.add(eventList[i])

    print("FOUND " + len(data) + " events between those times")

    return data

def getDateFromSlot(rawDate):
    # try to parse data
    date = None
    eventDate = [] 
    try:
        date = datetime.strptime(rawDate, '%Y-%m-%d')
    except:
        pass

    # if could not parse data must be one of the other formats
    if (date is None):
        # to find out what type of date this is, we can split it and count how many parts we have see comments above.
        res = rawDate.split("-")
        # if we have 2 bits that include a 'W' week number
        if (len(res) == 2 and res[1].index('W') > -1):
            dates = getWeekData(res)
            eventDate["startDate"] = dates.startDate.strftime('%m/%d/%Y')
            eventDate["endDate"] = dates.endDate.strftime('%m/%d/%Y')
            # if we have 3 bits, we could either have a valid date (which would have parsed already) or a weekend
        elif (len(res) == 3):
            dates = getWeekendData(res)
            eventDate["startDate"] = dates.startDate.strftime('%m/%d/%Y')
            eventDate["endDate"] = dates.endDate.strftime('%m/%d/%Y')
            # anything else would be out of range for this skill
        else:
            eventDate["error"] = dateOutOfRange
        # original slot value was parsed correctly
    else:
        eventDate["startDate"] = date.strftime('%m/%d/%Y')
        eventDate["endDate"] = (date + datetime.timedelta(hours=24)).strftime('%m/%d/%Y')

    return eventDate


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        parent = self
        parent.state = states['SEARCHMODE']

        speak_output = "Welcome, I can tell you the events in your school. You can say, What are the events tomorrow?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class SearchEventsIntentHandler(AbstractRequestHandler):
    """Handler for Search Event Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SearchEvents")(handler_input)

    def handle(self, handler_input):
        parent = self

        slots = handler_input.request_envelope.request.intent.slots

        if (slots is not None):
            slotValue = slots["EVENT_DATE"].value

            if (slotValue is not None):
                # Read the Icalendar File here....
                eventList = getCalendar(URL, readCalendar)
                
                # Check we have data
                if (len(eventList) > 0):
                    # Read slot data and parse out a usable date 
                    eventDate = getDateFromSlot(slotValue)

                    # Check we have both a start and end date
                    if (eventDate.startDate and eventDate.endDate):
                        # initiate a new array, and this time fill it with events that fit between the two dates
                        relevantEvents = getEventsBeweenDates(eventDate.startDate, eventDate.endDate, eventList)

                        if (len(relevantEvents)> 0):
                            # change state to description
                            parent.state = states['DESCRIPTION']

                            # Create output for both Alexa and the content card
                            cardContent = ""
                            output = oneEventMessage;
                            if (len(relevantEvents) > 1):
                                output = multipleEventMessage.format(len(relevantEvents))
                        
                            output += scheduledEventMessage;

                            if (len(relevantEvents) > 1):
                                output += firstThreeMessage.format(firstThreeMessage, x = 3 if (len(relevantEvents) > 3 ) else len(relevantEvents))
                        
                            if (relevantEvents[0] is not None):
                                date =  datetime.strptime(relevantEvents[0].start, '%Y%m%d')
                                output += eventSummary.format(eventSummary, "First", relevantEvents[0].summary, date.strftime('%A, %d. %B %Y') + ".");
                        
                            if (relevantEvents[1]):
                                date =  datetime.strptime(relevantEvents[1].start, '%Y%m%d')
                                output += eventSummary.format(eventSummary, "Second", relevantEvents[1].summary, date.strftime('%A, %d. %B %Y') + ".");
                            
                            if (relevantEvents[2]):
                                date =  datetime.strptime(relevantEvents[3].start, '%Y%m%d')
                                output += eventSummary.format(eventSummary, "Third", relevantEvents[2].summary, date.strftime('%A, %d. %B %Y') + ".");
                            
                            for i in range(0,len(relevantEvents), 1):
                                date = datetime.strptime(relevantEvents[i].start, '%Y%m%d')
                                cardContent += cardContentSummary.format(cardContentSummary, relevantEvents[i].summary, date.strftime('%A, %d. %B %Y') + "\n\n");
                        
                            output += eventNumberMoreInfoText;

                            return (
                                handler_input.response_builder
                                    .withSimpleCard(cardTitle,cardContent)
                                    .speak(output)
                                    .ask(haveEventsRepromt)
                                    .response
                                )  
                        else:
                            output = NoDataMessage
                            return (
                                handler_input.response_builder
                                    .ask(output)
                                    .response
                                )
                    else:
                        output = NoDataMessage
                        return (
                                handler_input.response_builder
                                    .ask(output)
                                    .response
                                )
                else:
                    output = NoDataMessage
                    return (
                            handler_input.response_builder
                                .ask(output)
                                .response
                            )
            else:
             return (
                    handler_input.response_builder
                        .ask("I'm sorry.  What day did you want me to look for events?", "I'm sorry.  What day did you want me to look for events?")
                        .response
                    )
        else:
             return (
                    handler_input.response_builder
                        .ask("I'm sorry.  What day did you want me to look for events?", "I'm sorry.  What day did you want me to look for events?")
                        .response
                    )
       
class ReadEventIntentHandler(AbstractRequestHandler):
    """Handler for Read Event Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ReadEvent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        eventDate = slots["EVENT_NAME"].value

        # type: (HandlerInput) -> Response
        speak_output = "I recognized your Read Event Intent"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response

class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(SearchEventsIntentHandler())
sb.add_request_handler(ReadEventIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()