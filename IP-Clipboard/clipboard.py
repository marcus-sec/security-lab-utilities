from flask import Flask, render_template_string


app = Flask(__name__)


# HTML Template with 5 text boxes and copy buttons + robust clipboard + toast
html_template = """
<!DOCTYPE html>
<html>
<head>
<title>IP Clipboard App</title>
<style>
body { font-family: Arial, sans-serif; margin: 40px; }
.ip-box { margin-bottom: 20px; }
input { padding: 8px; font-size: 16px; width: 250px; }
button { padding: 8px 12px; font-size: 16px; margin-left: 10px; cursor: pointer; }


/* Toast notification styling */
#toast {
visibility: hidden;
min-width: 200px;
margin-left: -100px;
background-color: #333;
 color: #fff;
 text-align: center;
 border-radius: 5px;
 padding: 10px;
 position: fixed;
 z-index: 1;
 left: 50%;
 bottom: 30px;
 font-size: 16px;
 }


 #toast.show {
 visibility: visible;
 animation: fadein 0.5s, fadeout 0.5s 2.5s;
 }


 @keyframes fadein {
 from { bottom: 0; opacity: 0; }
 to { bottom: 30px; opacity: 1; }
 }


 @keyframes fadeout {
 from { bottom: 30px; opacity: 1; }
 to { bottom: 0; opacity: 0; }
 }
 </style>
</head>
<body>
 <h2>IP Clipboard Tool</h2>
 {% for i in range(1, 6) %}
 <div class="ip-box">
 <input type="text" id="ip{{i}}" placeholder="Enter IP Address...">
 <button onclick="copyToClipboard('ip{{i}}')">Copy</button>
 </div>
 {% endfor %}


 <div id="toast"></div>


 <script>
 function copyToClipboard(elementId) {
 var copyText = document.getElementById(elementId);
 navigator.clipboard.writeText(copyText.value).then(function() {
 showToast("Copied: " + copyText.value);
 }, function(err) {
 showToast("Failed to copy!");
 });
 }


 function showToast(message) {
 var toast = document.getElementById("toast");s
 toast.innerText = message;
 toast.className = "show";
 setTimeout(function(){ toast.className = toast.className.replace("show", ""); }, 3000);
 }
 </script>
</body>
</html>
"""


@app.route("/")
def index():
 return render_template_string(html_template)


if __name__ == "__main__":
 app.run(debug=True, host="0.0.0.0", port=5000)