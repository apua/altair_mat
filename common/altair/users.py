"""
Since given data may only part of keys or typo,
it has to be checked.
In fact, it is not necessary.
"""

def check_not_user_existed(self, username):
    """
    There is also REST API for checking username is existed or not
    """
    for user in self.get_users():
        if user['login_name']==username:
            raise Exception('user "{}" existed'.format(username))

def check_user_data_keys_correct(self, keys):
    valid_keys = ('login_name', 'password', 'full_name', 'roles',
                  'email', 'mobile_phone', 'office_phone')
    if not set(valid_keys).issuperset(keys):
        raise Exception('some keys are not present\n'
                        '  the possible keys: {}\n'
                        '  your keys: {}'.format(valid_keys, keys))

def check_roles_correct(self, roles):
    possible_roles = self._list_roles_and_associated().keys()
    if not set(possible_roles).issuperset(roles):
        raise Exception('some roles are not present in the appliance\n'
                        '  the possible roles: {}\n'
                        '  your roles: {}'.format(possible_roles, roles))
####

def gen_cleaned_data(self, data):
    user_data = {'userName': data['login_name'],
                 'fullName': data.get('full_name'),
                 'password': data['password'],
                 #'enabled': True, # not necessary ....= =a
                 'emailAddress': data.get('email'),
                 'mobilePhone': data.get('mobile_phone'),
                 'officePhone': data.get('office_phone')}
    roles = data['roles']
    return user_data, roles

####

def get_users(self):
    def remove_builtin_usernames(users):
        r"""
        Don`t know how to treat those special users yet,
        since they invisible at first, visible after modified,
        and no options talk about that.
        So, just ignore them now.
    
        The builtin usernames only appear in combined appliance.
        """
        builtin_usernames = ('paul','ralph','april','rheid')
        for idx in reversed(range(len(users))):
            if users[idx]['userName'] in builtin_usernames:
                del users[idx]

    def get_roles(user):
        return [m['roleName'] for m in self._retrieve_user_roles(user)['members']]

    users = self._list_users()['members']
    remove_builtin_usernames(users)
    return [{'login_name':   user['userName'],
             'password':     '......',
             'full_name':    user['fullName'],
             'roles':        get_roles(user['userName']),
             #'enabled':      users['enabled'], # useless?
             'email':        user['emailAddress'],
             'mobile_phone': user['mobilePhone'],
             'office_phone': user['officePhone']}
            for user in users]


def add_user(self, data):
    check_not_user_existed(self, data['login_name'])
    check_user_data_keys_correct(self, data.keys())
    check_roles_correct(self, data['roles'])

    user_data, roles = gen_cleaned_data(self, data)
    self._add_users(user_data)
    self._update_user_roles(user_data['userName'], roles)


def delete_user(self, username):
    self._delete_user(username)


def get_user_info(self, username):
    for user in self.get_users():
        if user['login_name']==username:
            return user


def update_user_info(self, data):
    check_user_data_keys_correct(self, data.keys())
    check_roles_correct(self, data['roles'])

    user_data, roles = gen_cleaned_data(self, data)
    self._update_user(user_data)
    self._update_user_roles(user_data['userName'], roles)


#def change_password(self, new_password):
#    self._update_user({'userName': self.username,
#                       'password': new_password,
#                       'currentPassword': self.password})
