class GlobalSession:
    def sessions(request):
        details = {
            'userid': request.session.get('userid'),
            'usertype': request.session.get('usertype'),
            'firstname': request.session.get('firstname'),
            'middlename': request.session.get('middlename'),
            'lastname': request.session.get('lastname'),
        }
        return details