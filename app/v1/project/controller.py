from app.v1.project import project


@project.post('/projects')
def post():
    print('post')
    return {'data': 'post success'}


@project.get('/projects')
def get():
    return {'data': 'get success'}
