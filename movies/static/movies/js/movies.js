const getHeaderMovie = presentation => (
	createElement('div', null, {
		'class' : 'movie-header',
		'style' : `background:${presentation}; background-size:cover; background-position:center`
	})
)

const getBodyMovie = (...content) => {

	let titleElement = createElement('h3', content.title)
	let descriptionElement = createElement('p', content.description)

	let body = createElement('div', null, {'class' : 'movie-body'})

	return body.appendChild(titleElement)
			   .appendChild(descriptionElement)
}

const getFooterMovie = url => (
	createElement('button', 'SEE NOW', {
		'class' : 'footer-movie',
		'href' : url
	})
)

const setMoviesToSection = (id, movies) => (
	
	movies.map(

		movie => {

			const header = getHeaderMovie(movie.presentation)

			const body = getBodyMovie(
				movie.title,
				movie.description,
			)

			const footer = getFooterMovie(movie.url)

			querySelector('#' + id)
				.appendChild(header)
				.appendChild(body)
				.appendChild(footer)

		}
	)
)

const getMoviesByFilter = (idElement, filter = 'all') => {

	const url = HOST + 'series'
	const method = 'GET'

	fetch(url, dict(
		method = method
	)).then(movies => (
		setMoviesToSection(idElement, movies)
	))

}