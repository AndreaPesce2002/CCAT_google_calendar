import json
from cat.mad_hatter.decorators import tool, hook

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.

SCOPES = ['https://www.googleapis.com/auth/calendar']

@tool
def viewEventGoogle(tool_input, cat):  
    """to be used to view Google Calendar events"""
    
    try:
        settings = cat.mad_hatter.get_plugin().load_settings()
        
        # Assicuriamoci che ciò che passiamo a json.loads sia una stringa
        # Se "credentials" o "token" è una tupla, prendiamo il primo elemento
        credentials_info = json.loads(settings["credentials"][0] if isinstance(settings["credentials"], tuple) else settings["credentials"])
        token_info = json.loads(settings["token"][0] if isinstance(settings["token"], tuple) else settings["token"])
        
        # Crea le credenziali dai dizionari
        creds = Credentials.from_authorized_user_info(token_info, SCOPES)
        
        # Verifica la validità e rinfresca il token se necessario
        if not creds.valid:
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(credentials_info, SCOPES)
                creds = flow.run_local_server(port=0)
            # Aggiorna la tua stringa token con il token rinfrescato
            updated_token_json_str = json.dumps({
                'token': creds.token,
                'refresh_token': creds.refresh_token,
                'token_uri': creds.token_uri,
                'client_id': creds.client_id,
                'client_secret': creds.client_secret,
                'scopes': creds.scopes
            })
    
        service = build("calendar", "v3", credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + "Z"
        range = (datetime.datetime.utcnow() + datetime.timedelta(days=settings["range"])).isoformat() + "Z"
        events_result = service.events().list(
            calendarId="primary",
            timeMin=now,
            timeMax=range,
            singleEvents=True,
            orderBy="startTime",
        ).execute()
        events = events_result.get("items", [])

        if not events:
            return "Nessun evento prossimo trovato."
        else:
            events_list = []
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                events_list.append(f"{start}, {event['summary']}")
            return events_list
    except HttpError as error:
        return f"Si è verificato un errore: {error}"
    
    
@tool
def addEventGoogle(tool_input, cat):
    """
    to use to add or create google calendar events
    
    The input must be a dictionary with the following structure:
    {
        "summary": "Event title", # Short description of the event
        "location": "Location of the event", # Optional, can be left blank
        "description": "Detailed description of the event", # Optional, can be left blank
        "startDateTime": "2024-05-01T10:00:00", # Event start date and time, ISO 8601 format
        "endDateTime": "2024-05-01T12:00:00", # Event end date and time, ISO 8601 format
    }
    
    Make sure dates and times are provided in the correct format (ISO 8601) and reflect your time zone if you don't use UTC.
    """
    try:
        settings = cat.mad_hatter.get_plugin().load_settings()
        
        # Assicuriamoci che ciò che passiamo a json.loads sia una stringa
        credentials_info = json.loads(settings["credentials"][0] if isinstance(settings["credentials"], tuple) else settings["credentials"])
        token_info = json.loads(settings["token"][0] if isinstance(settings["token"], tuple) else settings["token"])
        
        # Crea le credenziali dai dizionari
        creds = Credentials.from_authorized_user_info(token_info, SCOPES)
        
        if not creds.valid:
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(credentials_info, SCOPES)
                creds = flow.run_local_server(port=0)
            
   
        if isinstance(tool_input, str):
            tool_input = json.loads(tool_input)
            
        service = build("calendar", "v3", credentials=creds)
        
        # Definisci l'evento da aggiungere
        event = {
            'summary': tool_input.get("summary", "Evento senza titolo"),
            'location': tool_input.get("location", ""),
            'description': tool_input.get("description", ""),
            'start': {
                'dateTime': tool_input["startDateTime"],
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': tool_input["endDateTime"],
                'timeZone': 'UTC',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        # Aggiungi l'evento al calendario
        event = service.events().insert(calendarId="primary", body=event).execute()
        return f"Evento creato: {event.get('htmlLink')}"
        
    except Exception as e:
        return f"Si è verificato un errore durante la creazione dell'evento di google calenar: {e}"