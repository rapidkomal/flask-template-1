
from app.lib.rabbitmq.publisher import Publisher
from app.v1.project import project
from app.v1.project.models.project import Project
from extensions import db
# from app.common.exceptions import resource_not_found


@project.post('/projects')
def post():
    # Publisher.add('test')
    db.session.add(Project(name='apoorv'))
    # db.session.commit()

    # result = add_together.delay(1,2)
    # print(result)
    # return {'data': 'post success'}
    return 'asd'

@project.get('/projects')
def get():
    return {'data': 'get success'}
