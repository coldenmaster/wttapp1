from frappe import _
import click
import frappe

@click.command('wtt-command-test1')
@click.argument('state', type=click.Choice(['on', 'off']))
def wtt_command_test1(state):
    # from flags.utils import set_flags
    # set_flags(state=state)
    print(state)
    print(_("you can help me ?"))

@click.command('wtt-command-test2')
def wtt_command_test2():
    # from flags.utils import set_flags
    # set_flags(state=state)
    print(_("bench test2?"))

@click.command('wtt-command-test3')
def wtt_command_test3():
    # from flags.utils import set_flags
    # set_flags(state=state)
    long_job(1, 2)
    print(_("bench test3"))

@click.command('wtt-command-test4')
def wtt_command_test4():
    # from flags.utils import set_flags
    # set_flags(state=state)
    print(_("bench test4"))

def long_job(arg1, arg2):
    # frappe.publish_realtime('msgprint', 'Starting long job')
    print('this is long job !')
    print(arg1)
    print(arg2)
    # frappe.publish_realtime("msgprint", 'Ending long job...')

def enqueue_long_job(arg1, arg2):
    frappe.enqueue('wttapp1.wttapp1.article', arg1=arg1, arg2=arg2)

commands = [
    wtt_command_test1,
    wtt_command_test2,
    wtt_command_test3,
    wtt_command_test4,

]