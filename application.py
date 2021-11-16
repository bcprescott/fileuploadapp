from flask import Flask, render_template, request
from azure.storage.blob import BlobClient

app = Flask(__name__)

@app.route('/tmp/8d9a8ab196bca1c')
def upload_file():
   return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(f.filename)
#       storage_account_key = "LSRjcStHbWkkpPEVhtWdLfqj/LnhSQ52JEfTIRuXaHPDRESWTFUiurvqW2YZl6McnXoCQp1HVt28YDg3XC7k3A=="
#       storage_url = "https://mlstor.blob.core.windows.net/"
#       blob_client = BlobClient(storage_url, container_name="images", blob_name=f.filename, credential=storage_account_key)
#       with open(f.filename, "rb") as data:
#           blob_client.upload_blob(data)
#       return "File Uploaded Successfully"
		
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
