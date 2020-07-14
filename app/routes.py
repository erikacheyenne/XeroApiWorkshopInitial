from flask import Flask,jsonify,request,abort,make_response
from app import app
from app import storage

locations = [
    {
        "name": "SofiasCustomAutomotive",
        "details": [
            {
                "address" : "P. 60 Sherman Wallaby Way, Sydney",
                "hours" : "9 A.M. to 5 P.M.",
                "phone number": "000-000-0000",
                "services":[

                          {
                            "servicetype":"regularmaintenance",
                            "details":[
                                {
                                    "price":5,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"bodyrepair",
                            "details":[
                                {
                                    "price":30,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"paintrepair",
                            "details":[
                                {
                                    "price":20,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"custompaint",
                            "details":[
                                {
                                    "price":20,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"framerepair",
                            "details":[
                                {
                                    "price":20,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"customemachining",
                            "details":[
                                {
                                    "price":0,
                                    "explanation":"unavailable at this time."
                                },
                            ]
                        }
                ]
            }
        ]
    }
]

services = [
   {
       "servicetype": "custommachining",
       "details":[
           {
               "price":"",
               "explanation of service":""
           }
       ]

   },
      {
       "servicetype": "framerepair",
       "details":[
           {
               "price":"",
               "explanation of service":""
           }
       ]

   }
]


jobs = [
    {
        "Order Number": ""
    }
]


# all my GET methods

@app.route('/')
def home():
    return "Hello World!"


@app.route('/locations', methods=['Get'], strict_slashes=False)
def get_locations():
    data = locations
    response = jsonify(data)
    response.status_code=200
    return response


@app.route('/locations/<string:name>', methods=['Get'], strict_slashes=False)
def get_location(name):


@app.route('/locations/<string:name>/services', methods=['Get'], strict_slashes=False)


@app.route('/service/<string:name>', methods=['Get'], strict_slashes=False)
@app.route('/services/<string:name>', methods =['Get'], strict_slashes=False)


@app.route('/Jobs', methods=['Get'], strict_slashes=False)
def get_jobs():
    return ""


# all my POST methods
@app.route('/locations/<string:name>/<string:service>', methods=['POST'], strict_slashes=False)
#The service needs to be added to a specific location, because this example assumes locations have different offerings. 
#Although there is a master list of all services that can be updated, this should be updated separately, 
# as locations can pick from master list.



# all my PUT methods
# PUT requests either create a new resource or modify an existing resource
@app.route('/services/<string:service_name>', methods=['PUT'], strict_slashes=False)
def put_service(service_name):


# all my DELETE methods

@app.route('/services/<string:service_name>', methods=['DELETE'], strict_slashes=False)

#app.run(port=5000,debug=True)
