import flask
from flask import jsonify, request, Response
from jsonpickle import json
from PenMap import PenMap
from Team import Team
from Parcel import Parcel, ParcelsHandler

app = flask.Flask(__name__)

#
# Model
#
teams = {}
robots_map = PenMap.simple_builder()
parcels_handler = ParcelsHandler(Parcel.simple_builder())
# end Model

@app.route("/")
def root():
    return Response(status=200)


@app.route("/robots/<team_id>", methods=['POST'])
def register_team(team_id):
    print "team_id %s" %team_id


    if teams.has_key(team_id):
        return "SORRY already registered!"
    else:
        # data = request.get_json(force=True)
        data = request.data
        print data
        if str(data).find("0x", 0, 2) is 0:
            teams[team_id] = Team(team_id, str(data))
            return Response(response="OK", status=200)
        else:
            return Response(response="SORRY", status=200)
            #
            # return jsonify(environment_configuration=environment_configuration, virtual_objects=a)



@app.route("/robots/<team_id>/<security_key>", methods=['DELETE'])
def delete_team(team_id, security_key):
    if teams.has_key(team_id):
        if teams[team_id].is_valid_security_key(security_key):
            teams.pop(team_id, None) # removes team from teams
            return Response(response="OK", status=200)
        else:
            return Response(response="SORRY", status=403)
    else:
        return Response(response="SORRY", status=404)

@app.route("/map", methods=['GET'])
def get_map():
    response_raw = robots_map.toJSON()
    return Response(status=200, response=response_raw)

@app.route("/parcels", methods=['GET'])
def get_parcels():
    response_raw = parcels_handler.toJSON()
    return Response(status=200, response=response_raw)


# @app.route("/virtualEnvironment", methods=['POST'])
# def add_object():
#     data = request.get_json(force=True)
#     if data:
#         processed_data = json.loads(data)
#         virtual_object_data = processed_data["cells"]
#         virtual_object_name = processed_data["name"]
#         if virtual_object_data:
#             vo = VirtualObject(virtual_object_data, virtual_object_name)
#             try:
#                 _virtual_environment.add_virtual_object(vo)
#             except ValueError as e:
#                 return Response(response=e, status=409)
#
#             return Response(status=200)
#
#     else:
#         return Response(status=400)
#
# @app.route("/virtualEnvironment", methods=['DELETE'])
# def delete_object():
#     data = request.get_json(force=True)
#     if data:
#         processed_data = json.loads(data)
#         virtual_object_data = processed_data["cells"]
#         virtual_object_name = processed_data["name"]
#         if virtual_object_data:
#             vo = VirtualObject(virtual_object_data, virtual_object_name)
#             if _virtual_environment.remove_virtual_object(vo):
#                 return Response(status=200)
#             else:
#                 return Response(response="Virtual Object Not found.", status=409)
#
#
#
#     else:
#         return Response(status=400)
#
# @app.route("/virtualEnvironment/reset", methods=['POST'])
# def reset_pose():
#     _set_reset_pose_true()
#     if get_reset_pose():
#         return Response(status=200)
#     else:
#         return Response(status=409)
#

if __name__ == "__main__":
    app.run(host="0.0.0.0")
