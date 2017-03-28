from slackbot.bot import Bot, listen_to, respond_to, default_reply
import re
import logging
import random


LOG_FORMAT = '%(asctime)-15s %(message)s'
logger = None
commonwords = {
    'the': ['teh', 'thr', 'thw'],
    'this': ['thsi', 'ths', 'tis'],
    'your': ['yor', 'you'],
    'annual': 'anal',
    "you're": ["your", "youre"],
    "then": "than",
    "i'm": "im",
}


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


@respond_to('text2tim (.*)', re.IGNORECASE)
@listen_to('text2tim (.*)', re.IGNORECASE)
def text2tim(message, text):
    text = text.replace(u'ay', u'e$y').replace(u'ey', u'a$y')
    text = text.replace(u'ie', u'e$i').replace(u'ei', u'ie')
    text = text.replace(u'$', u'')

    words = text.lower().split(u' ')

    results = []
    print words
    for word in words:
        if word in commonwords:
            if type(commonwords[word]) is list:
                result = random.choice(commonwords[word])
            else:
                result = commonwords[word]

            r = random.randint(0,100)

            if r <= 50:
                result = result.replace(u'is', u'si')
                result = result.replace(u'ne', u'n')
                result = result.replace(u'ss', u's')
                result = result.replace(u'ed', u'd')
                result = result.replace(u"'t", u"t")
            elif r > 50 and r <= 75:
                result = result.replace(u'ea', 'ae')

            results.append(result)
        else:
            results.append(word)

    message.reply(u' '.join(results))


@default_reply
def timbothy(message):
    message.reply('<INSERT RANDOM TIMMERISH HERE>')


if __name__ == '__main__':
    logging.basicConfig(filename='slack.log',
                        level=logging.INFO,
                        format=LOG_FORMAT)
    bot = Bot()
    bot.run()
