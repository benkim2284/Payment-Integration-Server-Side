from flask import Flask, redirect, url_for
import Adyen
import json

app = Flask("test")

#global adyen object with our specific API key 
adyen = Adyen.Adyen()
adyen.payment.client.xapikey = "AQEihmfuXNWTK0Qc+iSEl3csg8K8YqMTcJ9fhw4C0nrVd2FXbRDBXVsNvuR83LVYjEgiTGAH-9aKXAeCSjUmFGqvrAyFSDMt7buy+msUTtt9/VSbFtzI=-,dN:D33xZIk4Evr%"
adyen.payment.client.platform = "test"  # Change the value to live for the live environment.


@app.route("/paymentMethods", methods= ["GET", "POST"])
def paymentMethods():
    request = {
        "merchantAccount":"TestDFGECOM",
        "countryCode":"PH",
        "shopperLocale":"en_US",
        "amount":{
            "currency":"PHP",
            "value":1000
            }
            }
    
    result = adyen.checkout.payments_api.payment_methods(request)
    
    formatted_response = json.loads(result.raw_response)

    return formatted_response["paymentMethods"]


    #return "<p><b>My name is BEN<b></p><p>ye this me</p>"
    #return redirect(url_for("userPage", name = "swe"))


@app.route("/paymentDetail", methods= ["GET", "POST"])
def paymentDetail():

    request = {"details": {"redirectResult":"X6XtfGC3!YFSHEIFSIW"}}
    
    result = adyen.checkout.payments_api.payments_details(request)
    
    formatted_response = json.dumps((json.loads(result.raw_response)))

    return formatted_response


@app.route("/")
def hello_world():
    return redirect(url_for("paymentMethods"))


@app.route("/payments", methods= ["GET", "POST"])
def payments():
    request = {
        "amount": {
            "currency": "USD",
            "value": 1000
            }, 
            "reference": "My first Adyen test payment with an API library/SDK",
            "paymentMethod": {
                "type": "visa",
                "encryptedCardNumber": "test_4111111111111111",
                "encryptedExpiryMonth": "test_03",
                "encryptedExpiryYear": "test_2030",
                "encryptedSecurityCode": "test_737"
                },
                "shopperReference": "343",
                "returnUrl": "https://google.com",
                "merchantAccount": "TestDFGECOM"
                }
    
    result = adyen.checkout.payments_api.payments(request)
    
    formatted_response = json.dumps((json.loads(result.raw_response)))

    return formatted_response

@app.route("/sessions", methods= ["GET", "POST"])
def sessions():
    request = {}
    request['amount'] = {"value": "1000", "currency": "USD"}
    request['reference'] = "550e8400-e29b-41d4-a716-446655440000"
    request['merchantAccount'] = "TestDFGECOM"
    request['returnUrl'] = "https://google.com"
    request['countryCode'] = "US"
    
    result = adyen.checkout.payments_api.sessions(request)

    formatted_response = json.dumps((json.loads(result.raw_response)))

    return formatted_response







