from typing import Any, Text, Dict, List
from rasa_sdk.interfaces import Action
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from . import  weather

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []


class ActionWeather(Action):
    def name(self) -> Text:
        return 'action_weather'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = tracker.get_slot("place")
        msg = ""
        # current_place = next(tracker.get_latest_entity_values("place"), None)
        # print("test", current_place )
        if(place is not None): 
            temp = weather.weather_location(place = place)
            temp = (temp-32)/1.8
            temp = round(temp,1)
            msg = f"It's {temp} in {place}"
        else: 
            msg = "No find place"
        dispatcher.utter_message(text= msg)
        return []

class ActionScore(Action):
    def name(self) -> Text:
        return 'action_score'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="score is very good")

        return []
    
class ActionAdmission(Action): 
    def name(self) -> Text:
        return 'ask_admission_crieteria'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []
    

class ActionScholarship(Action):
    def name(self) -> Text: 
        return 'check_scholarship'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text]]: 
        return []