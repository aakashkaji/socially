from blue.user.signin import user_blueprint


@user_blueprint.route('/access')
def access_page():

    return 'hello access page return'


