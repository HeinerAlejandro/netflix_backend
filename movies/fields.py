from django.db.models import Field

def is_valid_time(**times):

	hours, minutes, seconds = times

	if hours < 0 or hours > 23 or minutes < 0 or minutes > 60 or seconds < 0 or seconds > 60:
		return False

	return True

class DurationTime:

	def __init__(self, hours, minutes, seconds):

		if hours and minutes and seconds:

			self.hours = hours
			self.minutes = minutes
			self.seconds = seconds

		elif not is_valid_time(hours, minutes, seconds):

			raise ValueError("Range of values, not is valid")

		else:

			raise AttributeError("You must set all parameters: hours, minutes and seconds")

	def get_representation(self):

		representation = '%d:%d:%d'%(self.hours, self.minutes, self.seconds)

		return representation


def parse_duration_string(value):

	list_times = value.split(':')

	duration = DurationTime(*list_times)

	return duration


class DurationField(Field):

	def __init__(self, *args, **kwargs):

		kwargs['max_length'] = 10

		super().__init__(*args, **kwargs)


	
	description = 'A representation of duration of serie or movie'

	def get_prep_value(self, value):

		return value.get_representation()


	def from_db_value(self, value, expression, connection):
		if value is None:
			return value

		return parse_duration_string(value)

	def to_python(self, value):

		if isinstance(value, DurationField):
			return value

		if value is None:
			return value

		return parse_duration_string(value)

	def to_representation(self, **data):
		pass