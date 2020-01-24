from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.http import request

class SeriesPermissions(BasePermission):
	"""
		View To Series of Netflix
	"""

	message = 'You not has the credential required to do this action'

	def has_permissions(self, request, view):

		if request.method in SAFE_METHODS:
			return True

		elif view.action == 'update' or view.action == 'create' or view.action == 'partial_update' or view.action == 'delete':
			return request.authenticate and request.user.is_superuser