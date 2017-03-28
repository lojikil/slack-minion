from slackbot import Bot, listen_to, respond_to
import re
import json


@listen_to('#slack2tweet (.*) (.*)', re.IGNORECASE)
def slack_to_tweet(message, description=None, url=None):
    print "Recvieved: {0} {1}".format(description, url)
    message.reply('... noted')
    message.react('+1')


@respond_to('tweet (.*) (.*)', re.IGNORECASE)
def tweet(message, description=None, url=None):
    print "Recvieved: {0} {1}".format(description, url)
    message.reply("... you're not my dad")
    message.react('+1')


@default_reply
def timbothy(message):
    message.reply('<INSERT RANDOM TIMMERISH HERE>')


if __name__ == '__main__':
    bot = Bot()
    bot.run()
