import datetime
import json
import os

from chainerui.database import db
from chainerui.logging import logger
from chainerui.models.argument import Argument
from chainerui.models.command import Command
from chainerui.models.log import Log
from chainerui.models.snapshot import Snapshot
from chainerui.utils import is_numberable


def load_result_json(result_path, json_file_name):
    """load_result_json."""
    json_path = os.path.join(result_path, json_file_name)

    _list = []
    if os.path.isfile(json_path):
        with open(json_path) as json_data:
            try:
                _list = json.load(json_data)
            except ValueError as err:
                logger.error(
                    'Failed to load json: {}, {}'.format(json_path, err))

    return _list


def crawl_result_path(result_path, include_log):
    """crawl_result_path."""
    result = {
        'logs': [],
        'args': [],
        'commands': [],
        'snapshots': []
    }

    if os.path.isdir(result_path):
        if include_log:
            result['logs'] = load_result_json(result_path, 'log')
        result['args'] = load_result_json(result_path, 'args')
        result['commands'] = load_result_json(result_path, 'commands')

        snapshots = [
            x for x in os.listdir(result_path) if x.count('snapshot_iter_')
        ]
        snapshots.sort()
        result['snapshots'] = snapshots

    return result


def _check_log_updated(result):
    log_json_path = os.path.join(result.path_name, 'log')
    if not os.path.isfile(log_json_path):
        # log file is removed, so don't have to update
        return False

    current_modified_at = result.log_modified_at
    modified_at = datetime.datetime.fromtimestamp(
        os.path.getmtime(log_json_path))
    if current_modified_at is None or current_modified_at != modified_at:
        result.log_modified_at = modified_at
        return True

    return False


def crawl_result(result, force=False, commit=True):
    """crawl_results."""
    now = datetime.datetime.now()

    if (not force) and (now - result.updated_at).total_seconds() < 4:
        return result

    # if log file is not updated, not necessary to get log contents
    is_updated = _check_log_updated(result)
    crawled_result = crawl_result_path(result.path_name, is_updated)

    if is_updated:
        current_log_idx = len(result.logs)
        if len(crawled_result['logs']) < current_log_idx:
            current_log_idx = 0
            result.logs = []
            result.args = None
        for log in crawled_result['logs'][current_log_idx:]:
            result.logs.append(Log(log))

    if result.args is None:
        result.args = Argument(json.dumps(crawled_result['args']))

    # commands list includes new commands and already registered commands.
    # registered commands can be get response, so need to update
    current_cmd_idx = len(result.commands)
    if len(crawled_result['commands']) < current_cmd_idx:
        current_cmd_idx = 0
        result.commands = []
        result.snapshots = []
    for cmd in crawled_result['commands'][current_cmd_idx:]:
        result.commands.append(Command(**cmd))
    for i, cmd in enumerate(crawled_result['commands'][:current_cmd_idx]):
        result.commands[i].update(cmd.get('response', None))

    # snapshots file list are sorted but not natural order, for example,
    # 'iter_900' set latter than 'iter_1000', so need to check the file
    # is registered or not.
    registered_snapshot_keys = [ss.iteration for ss in result.snapshots]
    for i, snapshot in enumerate(crawled_result['snapshots']):
        number_str = snapshot.split('snapshot_iter_')[1]
        if not is_numberable(number_str):
            continue
        number = int(number_str)
        if number in registered_snapshot_keys:
            continue
        result.snapshots.append(Snapshot(snapshot, number))

    result.updated_at = datetime.datetime.now()
    if commit:
        db.session.commit()

    return result
