from flask_app.config.sql_connection import connectToMySQL
from flask_app import db
from flask import flash
from datetime import datetime
import math
from .user import User


class Message:
    
    def __init__(self,data):
        
        self.id=data['id']
        self.user_id=data['sender_id']
        self.reciver_id=data['reciver_id']
        self.content=data['content']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


# create message
    @classmethod
    def create_msg(cls,data):
        query="""
        INSERT INTO messages(sender_id,reciver_id,content,created_at)
        VALUES(%(sender_id)s,%(reciver_id)s,%(content)s,NOW());
        """
        return connectToMySQL(db).query_db(query,data)


# count nbr of message 
    @classmethod
    def get_nbr_of_msg(cls,data):
        query="""
        SELECT count(*) 
        FROM messages
        WHERE sender_id=%(id)s ;
        """
        result=connectToMySQL(db).query_db(query,data)
        print(result)
        return result[0]['count(*)']

# count nbr of message 
    @classmethod
    def get_nbr_of_msg_reciver(cls,data):
        query="""
        SELECT count(*) 
        FROM messages
        WHERE reciver_id=%(id)s;
        """
        result=connectToMySQL(db).query_db(query,data)
        print(result)
        return result[0]['count(*)']

# get all messages with senders
    @classmethod
    def get_all_messages(cls,data):
        query="""
        SELECT * FROM messages
        JOIN users ON users.id=messages.sender_id
        WHERE messages.reciver_id=%(id)s;
        """
        results=connectToMySQL(db).query_db(query,data)
        all_messages_nfo=[]
        for row in results:
            
            all_data={
                'id':row['id'],
                'sender_id':row['sender_id'],
                'reciver_id':row['reciver_id'],
                'content':row['content'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
                
                'id':row['id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password':'',
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at']
            }
            all_messages_nfo.append(all_data)
        return all_messages_nfo

# delete message
    @classmethod
    def delete_message(cls,data):
        query="""
        DELETE FROM messages WHERE id=%(id)s ;
        """
        return connectToMySQL(db).query_db(query,data)

# validation message
    @staticmethod
    def validate_msg(msg):
        is_valid=True
        if len(msg['content'])<3:
            flash("* Message at least contain 3 characters","warning_msg")
            is_valid=False
        return is_valid
    
# using OOP to get tha current time when creating message
def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"