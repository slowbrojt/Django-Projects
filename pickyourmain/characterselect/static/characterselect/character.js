document.addEventListener('DOMContentLoaded', function() {
	document.getElementById('biobtn').addEventListener('click', function() {
		document.getElementById('more').style.display='none'
		document.getElementById('description').style.display='block'
	})
	document.getElementById('morebtn').addEventListener('click', function() {
		document.getElementById('description').style.display='none'
		document.getElementById('more').style.display='block'
	})
})