from flask import Flask , render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/chatbot',methods=('POST','GET'))
def chatbot():
    req = request.get_json(force=True)

    print(req['queryResult']['intent']['displayname'])

    if req['queryResult']['intent']['displayname'] == 'pizzemenu':

        print(req)
        #return jsonify(fulfillmentText = '챗봇 접속 성공')
        return jsonify(fulfillment_messages=[
            {
                "payload":{
                    "richContent" : [
                        [
                            {
                                "type" : "image" ,
                                "rawUrl" : "https://www.yyg.go.kr/www/citizen_participation/publicity/ybmodule.file/board_www/www_company_pr/300x1/1642656888.jpeg"
                            },
                            {
                                "type": "info",
                                "title": "피자메뉴",
                                "subtitle": "피자메뉴판",
                                "actionLink": "https://www.yyg.go.kr"
                            }
                        ]
                    ]
                }
            }
        ])


if __name__=='__main__':
    app.run('0.0.0.0',port=5001, debug=True)
