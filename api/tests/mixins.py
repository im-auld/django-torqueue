from factories import UserFactory, CharacterFactory, ServerFactory


class UserFixtureMixin(object):
    def setUp(self):
        self.user = UserFactory()
        self.user.save()


class NewUserFixtureMixin(object):
    def setUp(self):
        self.user = UserFactory()


class CharacterFixtureMixin(UserFixtureMixin):
    def setUp(self):
        super(CharacterFixtureMixin, self).setUp()
        self.character = CharacterFactory()
        self.server = ServerFactory()
        self.server.save()
