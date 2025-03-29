function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function simulateShot() {
    let formData = new FormData(document.getElementById('shotForm'));
    fetch('/simulate_shot/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken()
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = "Shot Distance: " + data.distance + " yards";
    })
    .catch(error => console.error('Error:', error));
}