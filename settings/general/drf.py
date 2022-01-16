REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # Allow read-only access for unauthenticated users, but
        # for add, change and delete user to have the according permission
        # on the model
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
      'rest_framework.filters.SearchFilter',
    ],
}
