from Pubnub import Pubnub


channels = [
    'torqueue-chat',
    'torqueue-notifications',
    'The Bastion',
    'Bergeren Colony',
    'The Harbinger',
    'The Shadowlands',
    'Jung Ma',
    'The Ebon Hawk',
    'Prophecy of the Five',
    'Jedi Covenant',
]


pubnub = Pubnub(
    publish_key='pub-c-41c97e9e-734f-461b-8a89-70bb9621e5bc',
    subscribe_key='sub-c-dd6b0e0a-08b9-11e5-a58c-02ee2ddab7fe'
)


def callback(message, channel):
    print(message)


def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")
    print pubnub.publish(
        channel='torqueue-notfications',
        message='Hello from the PubNub Python SDK'
    )


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

# pubnub.subscribe(
#     channels='torqueue-notifications', callback=callback, error=callback,
#     connect=connect, reconnect=reconnect, disconnect=disconnect
# )

pubnub.subscribe(
    channels='torqueue-notifications', callback=callback, error=callback,
)
