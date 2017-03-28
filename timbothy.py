from slackbot.bot import Bot, listen_to, respond_to, default_reply
import re
import json
import logging


LOG_FORMAT = '%(asctime)-15s %(message)s'
logger = None


@listen_to('#slack2tweet (.*) (.*)', re.IGNORECASE)
def slack_to_tweet(message, description=None, url=None):
    logging.info('received #slack2tweet: "{0}" {1}'.format(description, url))
    message.reply('... noted')
    message.react('+1')


@respond_to('tweet (.*) (.*)', re.IGNORECASE)
def tweet(message, description=None, url=None):
    logging.info("Received direct tweet: {0} {1}".format(description, url))
    message.reply("... you're not my dad")
    message.react('+1')


@respond_to('calcutron (.*)', re.IGNORECASE)
@listen_to('calcutron (.*)', re.IGNORECASE)
def calc(message, calc=None):
    logging.info("I ain't your calculator.")
    message.reply(':thinking_face:')


@default_reply
def timbothy(message):
    message.reply('<INSERT RANDOM TIMMERISH HERE>')


if __name__ == '__main__':
    logging.basicConfig(filename='slack.log', level=logging.INFO, format=LOG_FORMAT)
    bot = Bot()
    bot.run()
