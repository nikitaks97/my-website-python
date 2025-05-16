from flask import Flask
import pytest
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