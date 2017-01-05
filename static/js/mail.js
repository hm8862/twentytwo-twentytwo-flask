
function onSubmit() {
			var name = document.getElementById("item-name").textContent;
			// var size = document.getElementById("item-size").textContent.trim();
			var size = document.getElementById("item-size");
			var selected_size = size.options[size.selectedIndex].value;
			var colour = document.getElementById("item-colour");
			var selected_colour = colour.options[colour.selectedIndex].value;

			var mailto = document.getElementById("item-form");
			mailto.action = ("mailto:jessica@twentytwo-twentytwo.co.uk?" + "subject=" + encodeURIComponent("Purchase Enquiry: " + name + " | " + selected_size + " | " + selected_colour)
				// + "&body=" + encodeURIComponent("I would like to purchase the following item: \n\n Item: " + name + "\n Size: "
				// + size + "\n Colour: " + selected_colour + "\n\n Please let me know how to proceed!")
				);
}