



# this is the "test/email_service_test.py" file...

from app.email_service import send_email


def test_email_sending():

    assert send_email() == 200 or send_email() == 202