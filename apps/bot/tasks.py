from apps.bot.management.commands.bot import bot
from apps.bot.services.facebook import FacebookGroupRepository, FacebookKeywordRepository
from apps.bot.utils.broadcast import GroupBroadcasterService, KeywordBroadcasterService
from apps.customers.services.customers import CustomerService
from apps.customers.services.real_estate import RealEstateService
from config.celery import app


@app.task
def broadcast_group_task():
    group_broadcaster = GroupBroadcasterService(
        facebook_service=FacebookGroupRepository(),
        customer_service=CustomerService(),
        real_estate_service=RealEstateService(),
        bot=bot,
    )
    group_broadcaster.broadcast()


@app.task
def broadcast_keyword_task():
    keyword_broadcaster = KeywordBroadcasterService(
        facebook_service=FacebookKeywordRepository(),
        customer_service=CustomerService(),
        real_estate_service=RealEstateService(),
        bot=bot,
    )
    keyword_broadcaster.broadcast()
