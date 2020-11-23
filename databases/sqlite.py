from databases import SQL_LITE_PATH

from tortoise import Tortoise


TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.sqlite',
            'credentials': {
                'file_path': SQL_LITE_PATH,
            }
        }
    },
    'apps': {
        'lesson_schedule': {
            'models': ['lesson_schedule.models'],
            'default_connection': 'default',
        },
        'visit_scheduler': {
            'models': ['visit_scheduler.models'],
            'default_connection': 'default',
        }
    }
}


async def setup():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def shutdown():
    await Tortoise.close_connections()
