from flask import Flask,request
from flask.ext.cors import CORS
import json


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/scrumBoard',methods=['GET'])
def getScrumBoardList():
	temp= [{"id":1,"label":"Brand Control"},{"id":2,"label":"Media Buyer Portal"},{"id":3,"label":"PMP"},{"id":4,"label":"Audience"}]
	#temp=['Brand Control','Media Buyer Portal','PMP','Audience','PubConnect']
	return json.dumps(temp)

@app.route('/tickets/<int:idOfItem>',methods=['GET'])
def getTicketsfForScrumBoard(idOfItem):
	temp={}
	temp[1]=[{"id":"DSD-1234","name":"Asdasd","description":"asdasdasd"},{"id":"DSD-123","name":"Asdasd","description":"asdasdasd"}]
	temp[2]=[{"id":"BCD-123123","name":"Asdasd","description":"asdasdasd"},{"id":"BCD-1sda23234","name":"Asdasd","description":"asdasdasd"}]
	temp[3]=[{"id":"AUD-2323","name":"Asdasd","description":"asdasdasd"},{"id":"AUD-1234234234","name":"Asdasd","description":"asdasdasd"}]
	temp[4]=[{"id":"PMP-2323","name":"Asdasd","description":"asdasdasd"},{"id":"PMP-1234","name":"Asdasd","description":"asdasdasd"}]
	temp[5]=[{"id":"ASP-234234","name":"Asdasd","description":"asdasdasd"},{"id":"ASP-232","name":"Asdasd","description":"asdasdasd"}]
	return json.dumps(temp[idOfItem])

@app.route('/repos',methods=['GET'])
def getRepoList():
	tempList=['Dont Create','Mgmt','Inventory','Common']
	return json.dumps(tempList)

@app.route('/branches',methods=['POST'])
def createBranches():
	print request.data
	return "Success"



if __name__ == "__main__":
	app.run(debug=True)


