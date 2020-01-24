const HOST = 'http://localhost:8000/'

const createElement = (tag, text = null, attributes = null) => {

	let element = document.createElement(
		tag
	)

	if(text) element.innerHTML = text
	if(attributes)
		Object.keys(attributes).map(name => {
			element.setAttribute(name, attributes[name])
		})

	return element
}