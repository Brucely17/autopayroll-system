
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_upload_image(client):
    response = client.post('/upload/image', json={'imageSrc': 'base64-encoded-image'})
    assert response.status_code == 200
    assert b'Image uploaded successfully' in response.data


