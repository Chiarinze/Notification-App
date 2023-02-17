from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import notification
import datetime


class RoutineNotificationApp(App):
    
    # Definition of the notification messages for each day of the week
    routines = {
    0: {"title": "Monday Notification",
        "message": "Happy New Week! Don't forget your classes for today, and you are to be in church at 17:30 for Charismatic hour. Have a blessed day.",
        "time": datetime.time(6, 0)
    },
    1: {"title": "Tuesday Notification",
        "message": "Don't forget your classes for today.",
        "time": datetime.time(6, 0)
    },
    2: {"title": "Wednesday Notification",
        "message": "Don't forget your classes for today.",
        "time": datetime.time(6, 0)
    },
    3: {"title": "Thursday Notification",
        "message": "Don't forget your classes for today.",
        "time": datetime.time(6, 0)
    },
    4: {"title": "Friday Notification",
        "message": "TGIF! Don't forget your classes for today, and you are to be in church at 17:30 for Charismatic hour.",
        "time": datetime.time(6, 0)
    },
    5: {"title": "Saturday Notification",
        "message": "Happy Weekend. You have evangelism this morning and fellowship set up later in the evening.",
        "time": datetime.time(6, 0)
    },
    6: {"title": "Sunday Notification",
        "message": "Rise and Shine, it's another Sunday morning!",
        "time": datetime.time(6, 0)
    },
}
    
    
     #The Layout
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Start Notification Service')
        btn.bind(on_press=self.start_service)
        layout.add_widget(btn)

        self.notification_label = Label(text='No notifications yet')
        layout.add_widget(self.notification_label)

        return layout
    
    #What happens when you click the button
    def start_service(self, instance):
        self.notify_routine()
        self.notification_label.text = 'Notifications started'
        
        
    def notify_routine(self):
        today = datetime.datetime.today().weekday()    # Getting the current day of the week (0 = Monday, 1 = Tuesday, etc.)
        if today in self.routines:
            routine = self.routines[today]   # Geting the routine details for today
            alarm_time = datetime.datetime.combine(datetime.date.today(), routine["time"]) # Create a datetime object with today's date and the specified time
            Clock.schedule_once(lambda dt: self.show_notification(routine), (alarm_time - datetime.datetime.now()).total_seconds()) # Schedule the notification to be shown at the specified time
            now = datetime.datetime.now().time()   # Geting the routine details for today
            if now >= routine["time"]:
                self.show_notification(routine)
            else:
                self.notification_label.text = "It's not yet time."
                
    def show_notification(self, routine):
        notification.notify(
            title=routine["title"],
            message=routine["message"],
            timeout=5
        )
        self.notification_label.text = routine["message"]
    
    
if __name__ == '__main__':
    RoutineNotificationApp().run()
    
