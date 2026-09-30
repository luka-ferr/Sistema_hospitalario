from Observer.cita import Cita
from Observer.email import EmailObserver
from Observer.sms import SMSObserver

if __name__ == "__main__":

    cita = Cita(
        "Luis",
        "Dr. Chapatin",
        "31 de diciembre del 2500 a las 11:00 PM"
    )

    email = EmailObserver(cita)
    sms = SMSObserver(cita)

    cita.register_observer(email)
    cita.register_observer(sms)

    cita.confirmar()
