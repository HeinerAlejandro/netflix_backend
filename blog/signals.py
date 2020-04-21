def create_default_action(sender, **kwargs):

	entry_instance = kwargs.get('instance')

	if kwargs.get('created', False):
		
		link = reverse('entries:entry-detail', title = entry_instance.title)

		action = Action(
			title = 'LEER MAS',
			link = link
		)

		action.entries = entry_instance
		action.save()