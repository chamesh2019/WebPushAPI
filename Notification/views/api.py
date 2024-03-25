from rest_framework.response import Response
from rest_framework.decorators import api_view

from Notification.models import UserDevice
from LMS.settings import VAPID_PRIVATE_KEY, VAPID_PUBLIC_KEY

import requests
from webpush import WebPush, WebPushSubscription

@api_view(["POST"])
def subscribe(request):
    print(request.data)
    user = request.data.get("user")
    subscription = request.data.get("subscription")
    # UserDevice.objects.(user=user, subscription=subscription)
    # create or update UserDivice accordingly to user
    if UserDevice.objects.filter(user=user).exists():
        UserDevice.objects.filter(user=user).update(subscription=subscription)
    else:
        UserDevice.objects.create(user=user, subscription=subscription)
    return Response({"status": "success"})


@api_view(["GET"])
def get_subscriptions(request):
    subscriptions = UserDevice.objects.all()

    subs = [(sub.user, sub.subscription) for sub in subscriptions]

    
    wp = WebPush(private_key='pwa/private', public_key='pwa/public', subscriber="admin@mail.com",)
    subscription = WebPushSubscription.model_validate(subs[0][1])
    message = wp.get(message='Hello, world!', subscription=subscription)

    res = requests.post(str(subscription.endpoint), data=message.encrypted, headers=message.headers) # type-ignore
    print(res.status_code, res.reason, res.text)
    return Response({"subscriptions": subs})





