from typing import Type

class BaseWebhookHandler(object):
    """"""

    code: str

class WebhookHandlerV1(BaseWebhookHandler):
    """"""

    code = 'WebhookHandlerV1'

class WebhookHandlerV2(BaseWebhookHandler):
    """"""

    code = 'WebhookHandlerV2'

webhooks_registry: dict[str, Type[BaseWebhookHandler]] = {
    WebhookHandlerV1.code: WebhookHandlerV1,
    WebhookHandlerV2.code: WebhookHandlerV2,
}
