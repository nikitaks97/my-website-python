from flask import Flask
import sys
import os
import pytest

# Ensure the app module can be imported in CI/CD and local environments
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Website' in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Us' in response.data

def test_contact(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact Us' in response.data