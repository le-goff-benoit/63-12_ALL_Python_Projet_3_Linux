class InvHeader:
    def __init__(self):
        self.headers = [
            'INV',
            'Pac',
            'DaySum',
            'Status',
            'Pdc1',
            'Pdc2',
            'Udc1',
            'Udc2',
            'Temp',
            'Uac',
        ]
   

class MainHeader:
    inv = InvHeader()
    def __init__(self):
        self.headers = [
        '#Date',
        'Time',
        self.inv
    ]