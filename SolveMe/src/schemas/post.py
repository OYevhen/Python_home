POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'title': {'type': 'string'} #, 'enum': ['POST']}
    },
    'required': ['id']
}

# {'id': 1, 'title': 'POST'}