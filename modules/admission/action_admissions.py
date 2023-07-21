from typing import Any, Text, Dict, List
from rasa_sdk.interfaces import Action
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from . import  weather


class ActionAdmission(Action): 
    def name(self) -> Text:
        return 'ask_admission_crieteria'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []
    
