from flask import Flask, request, jsonify
from flask_cors import CORS
from eon4injuries.injuries import InjuryRoller
from eon4dice import roll
from random_target import get_table_result, get_subtarget

app = Flask(__name__)
CORS(app)
injuryroller = InjuryRoller()


@app.route('/api/get_random_target', methods=['GET'])
def random_target():
    injury_type = request.args.get('injury_type')
    aim = request.args.get('aim')

    if not injury_type or not aim:
        return jsonify({'status': 'error', 'message': 'Missing required parameters'}), 400

    # Construct the table string based on injury_type and aim
    table = f"{injury_type}_{aim}" if injury_type == "stick" else f"hugg_{aim}"

    try:
        target = get_table_result(table, roll('1t100'))
        return jsonify({
            'status': 'success',
            'random_target': target[1],
            'random_subtarget': target[2]
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/skadehantering/get_injury/', methods=['GET'])
def get_injury():
    injury_type = request.args.get('damage_type')
    damage = int(request.args.get('damage_value'))
    table_modifier = int(request.args.get('table_modifier', 0))
    target = request.args.get('target', None)
    subtarget = request.args.get('subtarget', None)

# Hantering av vänster/höger arm/ben
    if target is not None:
        if len(target.split()) > 1:
            target = target.split()[1]

    if injury_type == 'burn':
        table = 'Brännskada'
    elif injury_type == 'kross':
        table = injury_type + 'kada mot ' + target
    elif injury_type == 'slag':
        table = injury_type + 'smålsskada mot ' + target
    else:
        table = injury_type + 'skada mot ' + target

    if subtarget == 'okänt':
        subtarget_table = f"{injury_type}_normalt" if injury_type == "stick" else f"hugg_normalt"
        subtarget = get_subtarget(subtarget_table, target)

    print('subtarget:', subtarget)

    try:
        results = injuryroller.injury_effects(damage, table, table_modifier, verbose=True)
        print(results)


        return jsonify({
            'status': 'success',
            'utmattning': results[0],
            'dodsslag': results[1],
            'beskrivning': results[2],
            'area_hit': target,
            'subtarget': subtarget
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
