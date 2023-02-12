
note_name = ''
note_body = ''
record_time = ''
action = ''


def init(name, body, time):
    global note_name
    global note_body
    global record_time

    note_name = name
    note_body = body
    record_time = time


def init_criteria_name(name):
    global note_name

    note_name = name

def init_criteria_body(body):
    global note_body

    note_body = body


def init_time(date):
    global record_time

    record_time = date

def init_action(operation):
    global action

    action = operation


