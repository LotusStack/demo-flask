from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production

@app.route('/')
def index():
    """
    Main route - displays the home page
    """
    return render_template('index.html', title='Flask Demo App')

@app.route('/about')
def about():
    """
    About page route
    """
    return render_template('about.html', title='About')

@app.route('/api/hello')
def api_hello():
    """
    Simple API endpoint that returns a JSON response
    """
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success'
    })

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    """
    API endpoint that handles both GET and POST requests
    """
    if request.method == 'GET':
        # Return sample data
        return jsonify({
            'data': [
                {'id': 1, 'name': 'Item 1'},
                {'id': 2, 'name': 'Item 2'},
                {'id': 3, 'name': 'Item 3'}
            ]
        })
    elif request.method == 'POST':
        # A POST is done by sending data to this endpoint, usually as JSON.
        # Example using curl:
        # curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:5000/api/data
        data = request.get_json()
        if data:
            return jsonify({
                'message': 'Data received successfully',
                'received_data': data
            }), 201
        else:
            return jsonify({'error': 'No data provided'}), 400



if __name__ == '__main__':
    # Run the Flask development server
    # In production, use a proper WSGI server like Gunicorn
    app.run(debug=True, host='0.0.0.0', port=5000) 