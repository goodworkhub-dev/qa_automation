import os

QA_ORGANIZER_PASSWORD = os.getenv("QA_ORGANIZER_PASSWORD")
QA_SUPERUSER_PASSWORD = os.getenv("QA_SUPERUSER_PASSWORD")
QA_SUBSCRIBER_PASSWORD = os.getenv("QA_SUBSCRIBER_PASSWORD")
QA_VOLUNTEER_PASSWORD= os.getenv("QA_VOLUNTEER_PASSWORD")

class LoginData:
    test_superuser_loginpage_data = [{"url":"https://goodworkhub.com/","email": "neeti@goodworkhub.com","password":QA_SUPERUSER_PASSWORD }]
    test_orguser_loginpage_data = [{"url": "https://educationforall.goodworkhub.com/signin", "email": "neeti+01@goodworkhub.com", "password":QA_ORGANIZER_PASSWORD }]
    test_subscriberuser_loginpage_data = [{"url": "https://yawentest.goodworkhub.com/signin", "email": "wangyawen12+suprt@gmail.com","password": QA_SUBSCRIBER_PASSWORD}]
    test_volunteeruser_loginpage_data = [{"url": "https://educationforall.goodworkhub.com/signin", "email": "neeti+03@goodworkhub.com","password": QA_VOLUNTEER_PASSWORD}]