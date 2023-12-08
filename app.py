from flask import Flask, request, jsonify
from eon4injuries.injuries import InjuryRoller

app = Flask(__name__)
injuryroller = InjuryRoller()


@app.route('/injury_effects', methods=['GET'])
def calculate_injury_effects():
    injury_type = request.args.get('injury_type')
    damage = int(request.args.get('damage'))
    table_modifier = int(request.args.get('table_modifier', 0))
    verbose = request.args.get('verbose', 'true').lower() == 'true'

    try:
        results = injuryroller.injury_effects(damage, injury_type, table_modifier, verbose)
        return jsonify({
            'status': 'success',
            'data': results
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run()
