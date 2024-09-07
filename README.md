
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>vchatpy README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .note {
            background-color: #fff3cd;
            border-left: 6px solid #ffeeba;
            padding: 10px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

    <h1>vchatpy</h1>

    <p>vchatpy is a real-time video chat application built with Flask and Flask-SocketIO. This document provides instructions to set up and run the project.</p>

    <h2>Project Structure</h2>

    <pre><code>vchatpy/ (root directory)
  ├── templates/
  │   ├── invite.html
  │   ├── main.html
  │   └── room.html
  └── app.py
    </code></pre>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li>pip (Python package installer)</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository</strong>
            <pre><code>git clone https://github.com/yourusername/vchatpy.git
cd vchatpy
            </code></pre>
        </li>
        <li><strong>Create and Activate a Virtual Environment</strong>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
            </code></pre>
        </li>
        <li><strong>Install Required Packages</strong>
            <pre><code>pip install -r requirements.txt
            </code></pre>
            <div class="note">
                <p><strong>Note:</strong> Create a <code>requirements.txt</code> file with the following content:</p>
                <pre><code>Flask
Flask-SocketIO
                </code></pre>
            </div>
        </li>
    </ol>

    <h2>Running the Application</h2>
    <ol>
        <li><strong>Start the Flask Server</strong>
            <pre><code>python app.py
            </code></pre>
        </li>
        <li><strong>Open the Application</strong>
            <p>Open your web browser and navigate to <code>http://localhost:5000</code> to access the application.</p>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li><strong>Create a Room</strong>
            <p>Go to the main page and enter your name to create a unique room.</p>
        </li>
        <li><strong>Join a Room</strong>
            <p>Use the invite link or navigate to <code>/room/&lt;room_name&gt;</code> to join an existing room.</p>
        </li>
        <li><strong>In-Room Controls</strong>
            <ul>
                <li><strong>Microphone:</strong> Toggle your microphone on/off.</li>
                <li><strong>Camera:</strong> Toggle your camera on/off.</li>
                <li><strong>Share Screen:</strong> Share your screen or stop sharing.</li>
                <li><strong>End Call:</strong> End the call and return to the main page.</li>
            </ul>
        </li>
    </ol>

    <h2>Troubleshooting</h2>
    <ul>
        <li><strong>Video Not Showing:</strong> Ensure your browser has permissions for camera and microphone access.</li>
        <li><strong>InvalidStateError:</strong> Ensure that your signaling process properly handles SDP offers and answers.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
