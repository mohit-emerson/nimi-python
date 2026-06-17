# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_additional_enums = {
	'ReallocationPolicy': {
		'codegen_method': 'python-only',
		'values': [
			{
				'name': 'DO_NOT_REALLOCATE',
				'python_name': 'DO_NOT_REALLOCATE',
				'value': 0
			},
			{
				'name': 'TO_GROW',
				'python_name': 'TO_GROW',
				'value': 1
			}
		]
	}
}

