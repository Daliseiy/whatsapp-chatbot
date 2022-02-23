import os
from datetime import datetime
from  messages import *
from flask import Flask, request, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import exc
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
db_path = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user="user", pw="your_password", url="127.0.0.1:5432", db="insurecad")
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    whatsappno = db.Column(db.String, nullable=True, unique=True)
    token = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    age = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    lga = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)

    def asdict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            'token': self.token,
            'gender': self.gender,
            'age': self.age,
            'state': self.state,
            'lga': self.lga
        }


def process_text(string_list):
    new_string_list = []
    if len(string_list) != 0:


        for i in range(0, len(string_list)):
            text = string_list[i]
            index = int(text.index(':'))
            substring = text[0:index+1]
            b = text.replace(substring, '')
            new_string_list.append(b)

    return new_string_list



def strip_string(text):
    new_text = text.replace('whatsapp:', '')
    return new_text


def add_number_db(number):
    user = User(whatsappno=number)


    try:
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()

    except:
        print('There was another error')
        raise
    else:
        print('Everything is OK')


def get_final_reponse(number):
    user = User.query.filter_by(whatsappno=number).first()

    #recover last place of registration
    if user.name is None:
        return "Hello, Welcome to INSURECAD. Your number one provider of health insurance across Nigeria.😊\nWhat is your name ?"
    elif user.gender is None:
        return "Hello, Welcome to INSURECAD. Your number one provider of health insurance across Nigeria.😊\nAre you male or female ?"
    elif user.state is None:
        return "Hello, Welcome to INSURECAD. Your number one provider of health insurance across Nigeria.😊\nCan we know what state you are messaging us from ?"
    elif user.lga is None:
        return "Hello, Welcome to INSURECAD. Your number one provider of health insurance across Nigeria.😊\nAlright, what town\nare you messaging us from ?"
    elif user.email is None:
        return "Hello, Welcome to INSURECAD. Your number one provider of health insurance across Nigeria.😊\nWhat is your e-mail address ?"
    else:
        return "Hello, Welcome to INSURECAD. Your number one provider of health insurance across Nigeria.😊\nEnter the word *Service* to register for an insurance package ?"


def append_text_to_file(number, response):
    file = open(os.path.join("chats/",number+".txt"),'a')
    file.write("/n"+response)
    file.close()

def get_last_line(number):
    file = open(os.path.join("chats/",number+".txt"))
    lines = file.readlines()
    file.close()


    if(len(lines) == 0):
        return " "
    return lines[-1]


    
@app.route("/bot", methods=['POST'])
def bot():

    #create chat history file
    incoming_msg = request.values.get('Body', '').lower()
    text = strip_string(request.values.get('From', '').lower())


    if(os.path.isfile("chats/"+text+".txt")):
        pass
    else:
        file = open(os.path.join("chats/",text+".txt"),'w')
        file.close()



    #get last message sent
    last_msg  = get_last_line(text)
    add_number_db(text)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
   
    if  last_msg == name_question:
        name = incoming_msg
        user = User.query.filter_by(whatsappno=text).first()
        if user is None:
            pass
        else:
            user.name = name
            db.session.commit()
        response = "Great😊 Now " + name.capitalize() + \
                ".\nAre you male or female ?"
        msg.body(response)
        append_text_to_file(text,response)
        responded = True
        
    elif last_msg == gender_question:
        gender = incoming_msg
        user = User.query.filter_by(whatsappno=text).first()
        if user is None:
            pass
        else:
            user.gender = gender
            db.session.commit()
        response = "Alright😊.\nCan we know what state you are messaging us from ?"
        msg.body(response)
        append_text_to_file(text,response)
        responded = True

    elif last_msg == state_question:
        state = incoming_msg
        user = User.query.filter_by(whatsappno=text).first()
        if user is None:
            pass
        else:
            user.state = state
            db.session.commit()
        response = "What town in " + state.capitalize() + ".\nare you messaging us from ?"
        msg.body(response)
        append_text_to_file(text,response)
        responded = True

    elif last_msg == town_question:
        town = incoming_msg
        user = User.query.filter_by(whatsappno=text).first()
        if user is None:
            pass
        else:
            user.lga = town
            db.session.commit()
        response = "We are almost there🤗.\nWhat is your e-mail address ?"
        msg.body(response)
        append_text_to_file(text,response)
        responded = True

    elif last_msg == email_question:
        if '@' not in incoming_msg:
            response = "Please enter a valid e-mail address."
            msg.body(response)
        else:
            user = User.query.filter_by(whatsappno=text).first()
            if user is None:
                pass
            else:
                user.email = incoming_msg
                db.session.commit()
            response = "Great. You now have access to INSURECAD services.\nEnter the word *Service* to register for an insurance package ?"
            append_text_to_file(text,response)
            msg.body(response)
    elif 'service' in incoming_msg:
        response = "\n1️⃣ Health Insurace.\n2️⃣ Accident Insurance🤵🏽.\nChoose an Option."
        msg.body(response)
        append_text_to_file(text,response)
        responded = True

    elif last_msg == option_question:
        if '1' == incoming_msg or '2' == incoming_msg:
            response = "\nDo you have an Insurecad token ? (yes/no)"
            msg.body(response)
            append_text_to_file(text,response)
            responded = True

        elif '2' == incoming_msg:
            response = "\nDo you have an Insurecad token ? (yes/no)"
            msg.body(response)
            append_text_to_file(text,response)
            responded = True

        else:
            response = "\nIt seems like you sent a wrong response. Please reply with only 1 or 2 and not both."
            msg.body(response)
            append_text_to_file(text,response)

    elif last_msg == token_question:
        if 'yes' == incoming_msg:
            response = "Okay.\nPlease enter your token"
            msg.body(response)
            responded = True
            append_text_to_file(text,response)

        elif 'no' in incoming_msg:
            response = "Please follow the link ➡️ to make payment:🌍 www.paystack.com/developers"
            msg.body(response)
            append_text_to_file(text,response)
            responded = True

        else:
            response = "Please reply with only yes/no"
            msg.body(response)
            append_text_to_file(text,response)

    elif last_msg == collect_token:
        token = incoming_msg
        response = "\nToken received. Thank you for using INSURECAD\n"
        msg.body(response)
        append_text_to_file(text,response)

    else:
        response = get_final_reponse(text)
        msg.body(response)
        append_text_to_file(text,response)

    return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
    app.run()
