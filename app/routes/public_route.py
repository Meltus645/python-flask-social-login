from flask import Blueprint
from app.views.public_view import home

public =Blueprint('public', __name__)
public.route('', methods =['GET'])(home)