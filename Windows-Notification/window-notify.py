from win10toast import ToastNotifier
import time

def alarm(message, minute):
    times = int(minute)
    # Set the notifier with ToastNotifier()
    notifier = ToastNotifier()
    notifier.show_toast("Alarm", f"System will remind you after {times} minutes", duration = 10)
    time.sleep(times * 10)
    notifier.show_toast(f"Alarm", message, duration = 10)

if __name__ == "__main__":
    minute = input('Please print your time reminder : ')
    message = input('Please enter your alarm message : ')
    alarm(message, minute)
