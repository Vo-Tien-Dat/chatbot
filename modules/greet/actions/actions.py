from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionGreetWithInfor(Action):
    def name(self) -> Text:
        return "action_greet_with_infor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        personName = tracker.get_slot("slot_person_name")
        print(personName)

        return []