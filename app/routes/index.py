from operator import index

from flask import Blueprint, request, jsonify, render_template, redirect
from app.database.engine import db
from app.database.models import Product, Category

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index_func():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('main_index/index.html', products=products, categories=categories)