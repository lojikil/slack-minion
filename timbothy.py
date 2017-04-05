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


@respond_to('^#slack2tweet$')
@listen_to('^#slack2tweet$')
def missingtweetargs(message):
    message.reply("ya dun goofed and forgot ta add the arguments: #slack2tweet [description] [url]")


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
    crumb = None
    for word in words:
        if word in commonwords:
            if type(commonwords[word]) is list:
                result = random.choice(commonwords[word])
            else:
                result = commonwords[word]
        else:
             result = word

        r = random.randint(0, 100)

        if r <= 10:
            tmp = random.randint(0, len(result) - 1)
            if tmp == len(result) - 1:
                swapidx = tmp - 1
            else:
                swapidx = tmp + 1
            ws = list(result)
            t = ws[tmp]
            ws[tmp] = ws[swapidx]
            ws[swapidx] = t
            result = ''.join(ws)
        elif r <= 50:
            result = result.replace(u'is', u'si')
            result = result.replace(u'ne', u'n')
            result = result.replace(u'ss', u's')
            result = result.replace(u'ed', u'd')
            result = result.replace(u"'t", u"t")
        elif r > 50 and r <= 75:
            result = result.replace(u'ea', 'ae')
        elif r > 75:
            crumb = result[-1]
            result = result[0:-1]

        if crumb is not None:
            result = crumb + result
            crumb = None

        results.append(result)

    message.reply(u' '.join(results))


@default_reply
def timbothy(message):
    text2tim(message, message.body[u'text'])


if __name__ == '__main__':
    logging.basicConfig(filename='slack.log',
                        level=logging.INFO,
                        format=LOG_FORMAT)
    bot = Bot()
    bot.run()
