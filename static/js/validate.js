
function isValidForm() {
	// get selected option
	var item_size = document.getElementById("item-size");
	var item_colour = document.getElementById("item-colour");

	var errors = 0

	if (item_size.options[item_size.selectedIndex].value == "") {
		errors += 1

		document.getElementById("size-error").textContent = "Please select a size."
	}

	if (item_colour.options[item_colour.selectedIndex].value == "") {
		errors += 1

		document.getElementById("colour-error").textContent = "Please select a colour."
	}

	if (errors > 0) {
		return false;
	}
}