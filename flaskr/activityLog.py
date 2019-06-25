from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
from flaskr.db import insert_event, query_events

bp = Blueprint('activityLog', __name__)


@bp.route('/activityLog', methods=('POST',))
#@login_required
def logEvent():
    if request.method == 'POST':
        event_type = request.form['type']
        user_id = request.form['user_id']
        time = request.form['time']
        data = request.form['data']
        source = request.form['source']
        error = None

        # if not user_id:
        # 	error = 'user_id is required'
        # if not event_type:
        #     error = 'type is required.'
        # if not time:
        # 	error = 'time is required'

        event = {
            'type': event_type,
            'source': source,
            'user_id': user_id,
            'time': time,

        }

        if error is not None:
            flash(error)
        else:
            insert_event(event)
            return True

    return

@bp.route('/activityLogs', methods=('GET',))
#@login_required
def queryEventLogs():
    if request.method == 'GET':
        # user_id = request.form['user_id']
        # start_time = request.form['start_time']
        # end_time = request.form['end_time']
        # filters = request.form['filters']
        error = None

        # if not user_id:
        # 	error = 'user_id is required'
        # if not event_type:
        #     error = 'type is required.'
        # if not time:
        # 	error = 'time is required'

        if error is not None:
            flash(error)
        else:
            params = {}# TODO: {'filters': filters}
            events = query_events(params)
            #events = [{'type': 'test', 'user_id': 1000, 'time': '00:00:00', 'data': {'other': 'unknown'}}]
            
            return render_template('activityLogs/history.html', events=events)


    return