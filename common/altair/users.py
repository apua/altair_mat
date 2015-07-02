"""
CURD for Altair users

keys: login_name, full_name, email, mobile_phone, office_phone
all keys: keys | password | roles

add user:        Dict[login_name, password, roles, *] -> None
update user:     Dict[login_name, *] -> None
change password: password, (username) -> None
get users:       None -> List[ Dict[all keys] ]
get user:        username -> Dicst[all keys]
delete user:     username -> None
"""

#### Some functions for checking
valid_keys = ('login_name', 'password', 'full_name', 'roles', 'email', 'mobile_phone', 'office_phone')
possible_roles = []
namemap = {'userName': 'login_name',
           'fullName': 'full_name',
           'password': 'password',
           #'enabled' -- not necessary
           'emailAddress': 'email',
           'mobilePhone': 'mobile_phone',
           'officePhone': 'office_phone'}
namemap_ = {v:k for k,v in namemap.items()}

def user_existed(self, username):
    for user in self.get_users():
        if user['login_name']==username:
            return True
    else:
        return False

def keys_invalid(self, keys):
    return not set(valid_keys).issuperset(keys)

def user_roles_incorrect(self, roles):
    if not possible_roles:
        possible_roles.extend(self._list_roles_and_associated().keys())
    return not set(possible_roles).issuperset(roles)

def has_necessary_keys(self, keys, nece_keys):
    return set(keys).issuperset(nece_keys)

#### Create

def add_user(self, user):
    given_keys = ('login_name', 'password', 'roles')
    if not has_necessary_keys(self, user.keys(), given_keys):
        raise Exception('some keys are not present\n'
                        '  the necessary keys: {}\n'
                        '  your keys: {}'.format(given_keys, user.keys()))

    if user_existed(self, user['login_name']):
        raise Exception('user "{}" existed'.format(user['login_name']))

    if keys_invalid(self, user.keys()):
        raise Exception('some keys are not present\n'
                        '  the possible keys: {}\n'
                        '  your keys: {}'.format(valid_keys, user.keys()))

    if user_roles_incorrect(self, user['roles']):
        raise Exception('some roles are not present in the appliance\n'
                        '  the possible roles: {}\n'
                        '  your roles: {}'.format(possible_roles, user['roles']))

    nece_keys = valid_keys
    data = dict.fromkeys(nece_keys, '')
    data.update(user)
    info = {namemap_[k]:v for k,v in data.items() if k!='roles'}
    roles = data['roles']
    self._add_users(info)
    self._update_user_roles(data['login_name'], roles)

#### Read

def get_users(self):
    def get_roles(username):
        return [m['roleName'] for m in self._retrieve_user_roles(username)['members']]

    def generate_cleaned_user(user):
        data = {namemap[k]: v for k,v in user.items() if k!='enabled'}
        data['roles'] = get_roles(data['login_name'])
        return data

    users = self._list_users()['members']

    # remove built-in usernames
    #
    #    Don`t know how to treat those special users yet,
    #    since they invisible at first, visible after modified,
    #    and no options talk about that.
    #    So, just ignore them now.
    #
    #    The builtin usernames only appear in combined appliance.
    builtin_usernames = ('paul','ralph','april','rheid')
    for idx in reversed(range(len(users))):
        if users[idx]['userName'] in builtin_usernames:
            del users[idx]

    return list(map(generate_cleaned_user, users))

def get_user_info(self, username):
    raise NotImplementedError

def get_user(self, username):
    # not implement with REST API yet
    for user in self.get_users():
        if user['login_name']==username:
            return user
    else:
        raise Exception('no such user')

#### Update

def update_user_info(self, data):
    raise NotImplementedError

def update_user(self, data):
    """
    Update user information except password
    """
    if keys_invalid(self, data.keys()):
        raise Exception('some keys are not present\n'
                        '  the possible keys: {}\n'
                        '  your keys: {}'.format(valid_keys, user.keys()))

    user = self.get_user(data['login_name'])
    user.update(data)

    info = {namemap_[k]:v for k,v in user.items() if k!='roles'}
    roles = user['roles']

    # update user information
    info['password'] = None
    self._update_user(info)

    # update role
    if user['login_name'].lower()!='administrator':
        self._update_user_roles(user['login_name'], roles)

def change_password(self, new_password, username=None):
    """
    Change password with different new password

    It will be refined to set password even if newpassword is same as old one in the future.
    """
    if username and username!=self.username:
        if not user_existed(self, username):
            raise Exception('user "{}" not existed'.format(username))
        self._update_user({'userName': username,
                           'password': new_password})
    else:
        self._update_user({'userName': self.username,
                           'password': new_password,
                           'currentPassword': self.password})

def change_own_password(self, new_password):
    raise NotImplementedError

#### Delete

def delete_user(self, username):
    self._delete_user(username)
