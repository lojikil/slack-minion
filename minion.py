from slackbot.bot import Bot, listen_to, respond_to, default_reply
import re
import logging
import random


LOG_FORMAT = '%(asctime)-15s %(message)s'
logger = None
announce = "Received direct tweet (@sae @brian @otherdavid @ken @tgiordonell0): {0} {1}"


@listen_to('#slack2tweet (.*) (.*)', re.IGNORECASE)
def slack_to_tweet(message, description=None, url=None):
    logging.info('received #slack2tweet: "{0}" {1}'.format(description, url))
    message.reply('... noted')
    message.react('+1')
    message._client.send_message('social-media-room',
                                 announce.format(description, url))


@respond_to('^#slack2tweet$')
@listen_to('^#slack2tweet$')
def missingtweetargs(message):
    message.reply("the format is: #slack2tweet [description] [url]")


@respond_to('tweet (.*) (.*)', re.IGNORECASE)
def tweet(message, description=None, url=None):
    logging.info("Received direct tweet: {0} {1}".format(description, url))
    message.reply("thank you and noted")
    message.react('+1')
    message._client.send_message('social-media-room',
                                 announce.format(description, url))


@respond_to('burninator$', re.IGNORECASE)
@respond_to('trogdor$', re.IGNORECASE)
@respond_to('burninator (.*)', re.IGNORECASE)
@respond_to('trogdor (.*)', re.IGNORECASE)
@listen_to('burninator$', re.IGNORECASE)
@listen_to('trogdor$', re.IGNORECASE)
@listen_to('burninator (.*)', re.IGNORECASE)
@listen_to('trogdor (.*)', re.IGNORECASE)
def trogdor(message, burning_the=None):
    message.react('trogdor')
    message.react('fire')
    if burning_the:
        message.reply('TROGDOR, BURNINATING THE {0} :trogdor:'.format(burning_the))
    else:
        message.reply('TROGDOR, BURNINATING ALL THE CLIENTS. :trogdor:')


@default_reply
def default(message):
    message.reply("I currently understand slack2tweet & tweet.")
    message.send("#slack2tweet [description] [url]")
    message.send("(as a direct message): tweet [description] [url]")


if __name__ == '__main__':
    logging.basicConfig(filename='slack.log',
                        level=logging.INFO,
                        format=LOG_FORMAT)
    bot = Bot()
    bot.run()
