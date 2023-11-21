from tasklib import TaskWarrior
import logging


def addtj3_depend(current, parent):
    t = TaskWarrior()
    cur = t.get_task(uuid=f"{current}")
    tj3dep = cur['tj3depend']
    if tj3dep is None:
        tj3dep = ''
    if parent not in tj3dep.split():
        tj3dep += f" {parent}"
        cur['tj3depend'] = tj3dep
        cur.save()
        logging.info(f"{parent} {current} saved")
    else:
        logging.info(f"{parent} {current} not added")

